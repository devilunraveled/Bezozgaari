from PIL.Image import open as OpenImage
from .utils import parseURL
from pytesseract import pytesseract as Tesseract
import keras_ocr as kr

pipeline = kr.pipeline.Pipeline()

def detectText(image):
    prediction = pipeline.recognize([image])[0]
    return prediction

def getCenters(prediction):
    centers = []
    for text in prediction:
        center = (0, 0)
        for point in text[1]:
            center = (center[0] + point[0], center[1] + point[1])
        center = (center[0] / len(text[1]), center[1] / len(text[1]))
        centers.append((text[0], center))
    return centers

def distinguishLines(prediction, thresh=15):
    lines = []
    for text, center in prediction:
        if len(lines) == 0:
            lines.append([(text, center)])
            continue
        added = False
        for line in lines:
            if abs(line[0][1][1] - center[1]) <= thresh:
                line.append((text, center))
                added = True
                break
        if not added:
            lines.append([(text, center)])
    lines = [sorted(line, key=lambda x: x[1][0]) for line in lines]
    lines = sorted(lines, key=lambda x: x[0][1][1])
    return lines


def getImgString(prediction):
    lines = distinguishLines(prediction)
    lines = [" ".join([text[0] for text in line]) for line in lines]
    return "\n".join(lines)


class Image:
    def __init__(self, imageURL : str, imageID : str):
        self.imageURL = imageURL
        self.imageID = imageID
        self.image = None

    def getImage(self):
        if self.image is None:
            self.image = OpenImage(parseURL(self.imageURL).raw)
        return self.image

    def readTextFrom(self):
        if self.image is None:
            raise Exception("Image not loaded")
        
        prediction = detectText(self.imageURL)
        prediction = getCenters(prediction)
        prediction = getImgString(prediction)

        return prediction
