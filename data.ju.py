# %%
# %load_ext autoreload
# %autoreload 2

# %%
from typing import Dict
import pandas as pd
import numpy as np
import os

# %%
DATASET_FOLDER = './dataset/'
TRAIN_FILE = 'train.csv'
IMAGE_FOLDER = "./imgs/"

# %%
trainData = pd.read_csv(os.path.join(DATASET_FOLDER, TRAIN_FILE))

# %%
print(trainData.columns)
trainData.head()

# %%
trainData['datapoint_id'] = trainData.index

# %% [md] 
"""
## Assigning Images an ID
"""

# %%
imageMap : Dict[str, int] = { image : id for id, image in enumerate(trainData['image_link'].unique()) }
trainData['image_id'] = trainData['image_link'].map(lambda x : imageMap.get(x, -1))

# %%
from src.image import Image

# %%
index = 10
sampleImage = Image(trainData['image_link'][index], trainData['image_id'][index])

# %%
sampleImage.getImage()

# %%
print(sampleImage.readTextFrom())
