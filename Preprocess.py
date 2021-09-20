from PIL import Image

class Preprocess:
    """Class to preprocess user images"""

    def __init__(self, filename):
        self.filename = filename

    def user_img(filename):
        try:
            user_img = Image.open(filename)
        except IOError:
            pass

    def get_size(filename):
        with Image.open(filename) as image:
            width, height = image.size

    def resize(filename):
        if filename.get_size(filename) != 28:
            """resize imgage width here"""
