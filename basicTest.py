# %%
from typing import Dict
import pandas as pd
import os

# %%
DATASET_FOLDER = './dataset/'
TRAIN_FILE = 'train.csv'

# testData = pd.read_csv(os.path.join(DATASET_FOLDER, TEST_FILE))
#
# testData['datapoint_id'] = testData.index
#
# imageMap : Dict[str, int] = { image : id for id, image in enumerate(testData['image_link'].unique()) }
# testData['image_id'] = testData['image_link'].map(lambda x : imageMap.get(x, -1))

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
    # correct = 0
    # total = 0
    # trueCorrect = 0
    predictions : list[tuple[int,str]] = []
    
    print(f"Running from {startIndex} to {endIndex - 1}")

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
                    
                    # answer = datapoint['entity_value']
                    output = extractPossibleAnswer(image.readTextFrom(), targetMetric)
                    maxOutput = max(output, key=lambda x: x[0]*conversionFactor(standardUnit, x[1]))
                    output = [f"{value} {unit}" for value, unit in output]
                    
                    # # Is answer contained.
                    # for posAns in output :
                    #     if isCorrect(answer, posAns):
                    #         correct += 1
                    #         break
                    # total += 1
                    # 
                    # if len(output) >= 1 and isCorrect(answer, output[0]):
                    #     trueCorrect += 1

                    predictions.append((int(datapoint['image_id']), f'{maxOutput[0]} {maxOutput[1]}'))
                    # else :
                    #     print(f"Image Index : {index}\nAnswer : {answer}\nPredicted : {maxOutput}\nOutput : {output}")
                    # 
                    # bar.text = f"Correct : {correct}/{total} True Correct : {trueCorrect}/{total}"
                    bar()
                except Exception:
                    # total += 1
                    # bar.text = f"Correct : {correct}/{total} True Correct : {trueCorrect}/{total}"
                    predictions.append((int(datapoint['image_id']), '10 gram'))
                    bar()
                    continue
    except Exception as e:
        print(e)
    finally :
        with open(f'result_{startIndex}_{endIndex}.pkl', 'wb') as f:
            import pickle
            pickle.dump(predictions, f)

        onlyPredictions = [prediction[1] for prediction in predictions]
        with open(f'result_{startIndex}_{endIndex}.csv', 'w', encoding='utf-8') as f:
            f.write("index, prediction\n")
            for i, prediction in enumerate(onlyPredictions):
                f.write(f"{i},{prediction}\n")


def createDataPoints(startIndex, endIndex, data):
    import csv
    from typing import Dict
    from alive_progress import alive_bar

    from src.image import Image

    imageMap : Dict[str, int] = { image : id for id, image in enumerate(data['image_link'].unique()) }
    data['image_id'] = data['image_link'].map(lambda x : imageMap.get(x, -1))

    fileName = f"tesseract_text_{startIndex}_{endIndex}.csv"
    csvfile = open(fileName, 'a', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['image_id', 'image_link', 'group_id', 'entity_name', 'text'])

    with alive_bar(endIndex - startIndex + 1) as bar:
        for i in range(startIndex, endIndex + 1):
            image = Image(data['image_link'][i], data['image_id'][i])
            image.getImage()
            text = image.readTextFrom()

            writer.writerow([data['image_id'][i], data['image_link'][i], data['group_id'][i], data['entity_name'][i], text])
            bar()

    csvfile.close()



# getResult(0, batchSize, testData)
# getResult(batchSize, batchSize*2, testData)
# getResult(batchSize*2, batchSize*3, testData)
# getResult(batchSize*3, batchSize*4, testData)
# getResult(batchSize*4, batchSize*5, testData)
# getResult(batchSize*5, batchSize*6, testData)
# getResult(batchSize*6, batchSize*7, testData)
# getResult(batchSize*7, batchSize*8, testData)
# getResult(batchSize*8, batchSize*9, testData)
# getResult(batchSize*9, len(testData), testData)

def runAChunk():
    trainData = pd.read_csv(os.path.join(DATASET_FOLDER, TRAIN_FILE))
    chunks = 15
    totalDataPoints = len(trainData)
    batchSize = totalDataPoints//chunks
    
    i = int(input(f'Enter chunk number(1-{chunks}) : '))
    if i < 1 or i > chunks:
        raise Exception
    
    start = batchSize*(i-1)
    end = batchSize*i if i != chunks else len(trainData)
    
    createDataPoints(start, end, trainData)

def concatenateFiles(batchSize, chunks, data):
    files = [ pd.read_csv(f"./result_{batchSize*i}_{batchSize*(i+1)}.csv") for i in range(chunks - 1) ] + [pd.read_csv(f"./result_{batchSize*(chunks - 1)}_{len(data)}.csv")]
    result = pd.concat(files)
    result.to_csv("./results.csv", index=False)

runAChunk()
# concatenateFiles()
