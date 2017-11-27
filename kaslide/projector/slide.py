class SlideImage:
    def __init__(self, filename, fp=None):
        self.filename = filename
        self.fp = fp


class SlideText:

    style = None

    def __init__(self, text):
        self.text = text


class Slide:

    timeout = 0

    def __init__(self, image: SlideImage, text: SlideText):
        self.image = image
        self.text = text

#
# Slide types
#


class SlideNormal(Slide):

    timeout = 1

    def __init__(self, filename, text):
        super().__init__(SlideImage(filename), SlideText(text))
