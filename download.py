import pandas as pd
import os
from src.utils import download_images

# %%
DATASET_FOLDER = './dataset/'
TRAIN_FILE = 'train.csv'
IMAGE_FOLDER = "./imgs/"

# %%
trainData = pd.read_csv(os.path.join(DATASET_FOLDER, TRAIN_FILE))

download_images(image_links = trainData['image_link'], download_folder = IMAGE_FOLDER)
