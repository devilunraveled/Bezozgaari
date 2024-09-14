from PIL.Image import open as OpenImage
from .utils import parseURL
from pytesseract import pytesseract as Tesseract

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

        return Tesseract.image_to_string(self.image)
