from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)
print(res)

import pandas as pd
from typing import Dict
from alive_progress import alive_bar as aliveBar
import csv

from src.image import Image
from src.utils import extractPossibleAnswer, conversionFactor
from src.constants import entity_unit_map

testDf = pd.read_csv('./dataset/test.csv')
# trainDf = pd.read_csv('./dataset/train.csv')
imageMap : Dict[str, int] = { image : id for id, image in enumerate(testDf['image_link'].unique()) }
testDf['image_id'] = testDf['image_link'].map(lambda x : imageMap.get(x, -1))

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

startIndex = 0
endIndex = min(10535, len(testDf) - 1)

tesseract_text_file = f"tesseract_text/tesseract_text_{startIndex}_{endIndex}.csv"
tesseractDf = pd.read_csv(tesseract_text_file)
print(len(tesseractDf))

filename = f"roberta_results_{startIndex}_{endIndex}.csv"
csvfile = open(filename, 'a', newline='')
writer = csv.writer(csvfile)
writer.writerow(['index', 'prediction'])
with aliveBar(endIndex - startIndex + 1) as bar:
	for index, row in testDf[startIndex:endIndex+1].iterrows():
		try:
			image = Image(row['image_link'], row['image_id'])
			image.getImage()
			context = image.readTextFrom()
		except:
			context = ""
		if context == "":
			context = "No context available."
		
		# print(context)

		question = f"What is the item {(row['entity_name'].split('_'))[-1]}?"

		res = nlp(question=question, context=context)

		value = ""
		targetMetric = row['entity_name']
		standardUnit = list(entity_unit_map[targetMetric])[0]
		output = extractPossibleAnswer(res['answer'].lower(), targetMetric)
		try:
			if len(output) > 1:
				maxOutput = max(output, key=lambda x: x[0]*conversionFactor(standardUnit, x[1]))
			elif len(output) == 1:
				maxOutput = output[0]
			finalOutput = f"{maxOutput[0]} {maxOutput[1]}"
			value = maxOutput[0]
		except Exception as e:
			finalOutput = ""
			value = ""

		writer.writerow([row['index'], finalOutput])
		print(f"QUESTION: {question}\nANSWER: {finalOutput}\nOUTPUT: {output}\nMODEL OUTPUT: {res['answer']}")
		bar()

csvfile.close()