import re
from .constants import *
import os
import requests
import pandas as pd
import multiprocessing
import time
from time import time as timer
from tqdm import tqdm
import numpy as np
from pathlib import Path
from functools import partial
import requests
import urllib
from PIL import Image

def parseURL( url : str ):
    response = requests.get(url, stream = True)
    return response

def common_mistake(unit):
    if unit in allowed_units:
        return unit
    if unit.replace('ter', 'tre') in allowed_units:
        return unit.replace('ter', 'tre')
    if unit.replace('feet', 'foot') in allowed_units:
        return unit.replace('feet', 'foot')
    return unit

def parse_string(s):
    s_stripped = "" if s==None or str(s)=='nan' else s.strip()
    if s_stripped == "":
        return None, None
    pattern = re.compile(r'^-?\d+(\.\d+)?\s+[a-zA-Z\s]+$')
    if not pattern.match(s_stripped):
        raise ValueError("Invalid format in {}".format(s))
    parts = s_stripped.split(maxsplit=1)
    number = float(parts[0])
    unit = common_mistake(parts[1])
    if unit not in allowed_units:
        raise ValueError("Invalid unit [{}] found in {}. Allowed units: {}".format(
            unit, s, allowed_units))
    return number, unit


def create_placeholder_image(image_save_path):
    try:
        placeholder_image = Image.new('RGB', (100, 100), color='black')
        placeholder_image.save(image_save_path)
    except Exception as e:
        return

def download_image(image_link, save_folder, retries=3, delay=3):
    if not isinstance(image_link, str):
        return

    filename = Path(image_link).name
    image_save_path = os.path.join(save_folder, filename)

    if os.path.exists(image_save_path):
        return

    for _ in range(retries):
        try:
            urllib.request.urlretrieve(image_link, image_save_path)
            return
        except:
            time.sleep(delay)
    
    create_placeholder_image(image_save_path) #Create a black placeholder image for invalid links/images

def download_images(image_links, download_folder, allow_multiprocessing=True):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    if allow_multiprocessing:
        download_image_partial = partial(
            download_image, save_folder=download_folder, retries=3, delay=3)

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            list(tqdm(pool.imap(download_image_partial, image_links), total=len(image_links)))
            pool.close()
            pool.join()
    else:
        for image_link in tqdm(image_links, total=len(image_links)):
            download_image(image_link, save_folder=download_folder, retries=3, delay=3)
       

def extract_numeric_value(string):
    # Use regex to find numbers (both integers and decimals)
    try :
        match = re.search(r'\d+(\.\d+)?', string)
        return float(match.group(0)) if match else None
    except Exception :
        return None

def extractInteger(string):
    # Use regex to find integers
    try :
        if string.isnumeric():
            return int(string)
        else :
            return None
    except Exception :
        return None

def exactMatchUnits(imageContent : str, targetUnit : str, outputUnit : str):
    """
    Return all occurences of the exact match in the imageContent.
    Returns the float value it found prior to the unit.
    """

    # Split the imageContent wherever we find the matching targetUnit ( with a space )
    possibleAnswers = imageContent.split(f'{targetUnit}')
    
    values = set()
    if not imageContent.endswith(targetUnit):
        possibleAnswers = possibleAnswers[:-1]

    for possibleAnswer in possibleAnswers:
        # Split based on space to the last part beyond which the unit was mentioned.
        possibleAnswer = possibleAnswer.strip()
        if len(possibleAnswer) == 0:
            continue
        possibleAnswer = possibleAnswer.split()[-1]

        # Check if the last part is an integer
        integerValue = extractInteger(possibleAnswer)
        if integerValue != None :
            values.add((integerValue, outputUnit))
            continue

        # Check if it is a float
        value = extract_numeric_value(possibleAnswer)
        if value != None :
            values.add((value, outputUnit))


    # Return the values
    return values

def extractPossibleAnswer(imageContent : str , targetMetric : str ):
    targetUnits = entity_unit_map[targetMetric]
    
    possibleAnswers = set()
    for targetUnit in targetUnits:
        for possibleUnit in aliases.get(targetUnit, [targetUnit]):
            # print(f"Searching for {targetMetric} in {possibleUnit}")
            possibleAnswers.update(exactMatchUnits(imageContent, possibleUnit, targetUnit))

    return list(possibleAnswers)
