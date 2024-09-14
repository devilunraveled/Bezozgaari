# %%
from typing import Dict
import pandas as pd
import os

# %%
DATASET_FOLDER = './dataset/'
TRAIN_FILE = 'train.csv'

trainData = pd.read_csv(os.path.join(DATASET_FOLDER, TRAIN_FILE))

print(trainData.columns)
trainData.head()

trainData['datapoint_id'] = trainData.index

imageMap : Dict[str, int] = { image : id for id, image in enumerate(trainData['image_link'].unique()) }
trainData['image_id'] = trainData['image_link'].map(lambda x : imageMap.get(x, -1))

from src.utils import extractPossibleAnswer
from src.image import Image
from src.constants import conversion_factor, entity_unit_map
from alive_progress import alive_bar


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

def conversionFactor(units, baseUnits):
    return conversion_factor[units][baseUnits]

def getResult(startIndex, endIndex, data ):
    correct = 0
    total = 0
    trueCorrect = 0
    predictions : list[tuple[int,str]] = []
    
    data = data[startIndex:endIndex]
    try :
        with alive_bar(len(data)) as bar:
            for _ ,datapoint in data.iterrows():
                try:
                    imageLink = datapoint['image_link']
                    targetMetric = str(datapoint['entity_name'])
                    standardUnit = list(entity_unit_map[targetMetric])[0]
                    
                    image = Image(str(imageLink), str(datapoint['image_id']))
                    image.getImage()
                    
                    answer = datapoint['entity_value']
                    output = extractPossibleAnswer(image.readTextFrom(), targetMetric)
                    maxOutput = max(output, key=lambda x: x[0]*conversionFactor(standardUnit, x[1]))
                    output = [f"{value} {unit}" for value, unit in output]
                    
                    # Is answer contained.
                    for posAns in output :
                        if isCorrect(answer, posAns):
                            correct += 1
                            break
                    total += 1
                    
                    if len(output) >= 1 and isCorrect(answer, output[0]):
                        trueCorrect += 1

                    predictions.append((int(datapoint['image_id']), f'{maxOutput[0]} {maxOutput[1]}'))
                    # else :
                    #     print(f"Image Index : {index}\nAnswer : {answer}\nPredicted : {maxOutput}\nOutput : {output}")
                    
                    bar.text = f"Correct : {correct}/{total} True Correct : {trueCorrect}/{total}"
                    bar()
                except Exception:
                    total += 1
                    bar.text = f"Correct : {correct}/{total} True Correct : {trueCorrect}/{total}"
                    predictions.append((int(datapoint['image_id']), '10 gram'))
                    bar()
                    continue
    except Exception as e:
        print(e)
    finally :
        # with open(f'result_{startIndex}_{endIndex}.pkl', 'wb') as f:
        #     import pickle
        #     pickle.dump(predictions, f)

        onlyPredictions = [prediction[1] for prediction in predictions]
        print(onlyPredictions)
        with open(f'result_{startIndex}_{endIndex}.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(onlyPredictions))

getResult(40, 60, trainData)
