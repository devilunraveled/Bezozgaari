import pandas as pd
import pickle
from typing import Dict
from alive_progress import alive_bar

from src.image import Image

df = pd.read_csv('dataset/test.csv')
imageMap : Dict[str, int] = { image : id for id, image in enumerate(df['image_link'].unique()) }
df['image_id'] = df['image_link'].map(lambda x : imageMap.get(x, -1))

startIndex = 10001
endIndex = min(20000, len(df) - 1)

fileName = f"tesseract_text/tesseract_text_{startIndex}_{endIndex}.pkl"

# imageTexts = pd.DataFrame(columns=['image_link', 'text'])
imageTexts = {} # link : text

with alive_bar(endIndex - startIndex + 1) as bar:
	for i in range(startIndex, endIndex + 1):
		if df['image_link'][i] in imageTexts:
			continue
		
		try:
			image = Image(df['image_link'][i], df['image_id'][i])
			# text = detectText(df['image_link'][i])
			image.getImage()
			text = image.readTextFrom()
		except:
			text = "No context available."

		imageTexts[df['image_link'][i]] = text

		if (i - startIndex) % 100 == 0:
			with open(fileName, 'wb') as f:
				pickle.dump(imageTexts, f)

		bar()
