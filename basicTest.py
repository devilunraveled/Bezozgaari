# %%
from typing import Dict
import pandas as pd
import os

# %%
DATASET_FOLDER = './dataset/'
TRAIN_FILE = 'train.csv'
IMAGE_FOLDER = "./imgs/"

trainData = pd.read_csv(os.path.join(DATASET_FOLDER, TRAIN_FILE))

print(trainData.columns)
trainData.head()

trainData['datapoint_id'] = trainData.index

imageMap : Dict[str, int] = { image : id for id, image in enumerate(trainData['image_link'].unique()) }
trainData['image_id'] = trainData['image_link'].map(lambda x : imageMap.get(x, -1))

from src.utils import extractPossibleAnswer
from src.image import Image

# %%
for index ,datapoint in trainData.iterrows():
    imageLink = datapoint['image_link']
    targetMetric = str(datapoint['entity_name']).split('_')[1]
    image = Image(str(imageLink), str(datapoint['image_id']))
    print( extractPossibleAnswer(image.readTextFrom(), targetMetric) )
