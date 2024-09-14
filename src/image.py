from PIL.Image import open as OpenImage
from .utils import parseURL

class Image:
    def __init__(self, imageURL : str, imageID : str):
        self.imageURL = imageURL
        self.imageID = imageID
        self.image = None

    def getImage(self):
        if self.image == None:
            self.image = OpenImage(parseURL(self.imageURL).raw)
        return self.image
