import re


def cleanAnwer(answer : str) -> str:
	"""
	Expecting: the answer will contain a number (possibly with a decimal) followed by a unit.
	"""
	regex = r"(\d+\.?\d*)\s*(\w+)"

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print(res)

import pandas as pd
from typing import Dict

trainDf = pd.read_csv('./dataset/train.csv')
imageMap : Dict[str, int] = { image : id for id, image in enumerate(trainDf['image_link'].unique()) }
trainDf['image_id'] = trainDf['image_link'].map(lambda x : imageMap.get(x, -1))
from alive_progress import alive_bar as aliveBar
from src.image import Image
from src.utils import extractPossibleAnswer, conversionFactor
from src.constants import entity_unit_map

def isCorrect(expected, output):
    try :
        expectedValue, expectedUnit = expected.strip().split()
        outputValue, outputUnit = output.strip().split()

        if float(expectedValue) == float(outputValue) and expectedUnit == outputUnit:
            return True
        else :
            return False
    except Exception :
        return False

with aliveBar(len(trainDf), force_tty=True) as bar:
	accuracy = 0
	trueAccuracy = 0
	for index, row in trainDf.iterrows():
		try:
			image = Image(row['image_link'], row['image_id'])
			image.getImage()
			context = image.readTextFrom()
		except:
			context = ""

		question = f"What is the item {(row['entity_name'].split('_'))[-1]}?"
		if context == "":
			context = "No context available."

		res = nlp(question=question, context=context)

		# print(res, context)
		value = res['answer'].split()
		if(len(value) == 0):
			value = " "
		else:
			value = value[0]

		targetMetric = row['entity_name']
		standardUnit = list(entity_unit_map[targetMetric])[0]
		output = extractPossibleAnswer(res['answer'].lower(), targetMetric)
		# finalOutput = f"model output: {res['answer']}"
		try:
			if len(output) > 1:
				maxOutput = max(output, key=lambda x: x[0]*conversionFactor(standardUnit, x[1]))
			elif len(output) == 1:
				maxOutput = output[0]
			finalOutput = f"{maxOutput[0]} {maxOutput[1]}"
			value = maxOutput[0]
		except Exception as e:
			finalOutput = f"model output: {res['answer']}"
			value = ""

		print(f"QUESTION: {question}\nANSWER: {finalOutput}\nCORRECT ANSWER: {row['entity_value']}\nOUTPUT: {output}\nMODEL OUTPUT: {res['answer']}")

		accuracy += isCorrect(row['entity_value'], finalOutput)
		trueAccuracy += (finalOutput== row['entity_value'])

		# Accuracy: {accuracy}/{index + 1} = {(accuracy / (index + 1) * 100):.3f}%\n
		bar.text(f"Accuracy: {accuracy}/{index + 1} = {(accuracy / (index + 1) * 100):.3f}%\nTrue Acc.: {trueAccuracy}/{index + 1} = {(trueAccuracy / (index + 1) * 100):.3f}%")
		bar()