from .. import graphic


class SlideText:

    style = None

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "SlideText(text=" + self.text + ")"


class Slide:

    timeout = 0

    def __init__(self, image: graphic.Image, text: SlideText):
        self.image = image
        self.text = text

    def __str__(self):
        return "Slide(image=" + str(self.image) + ", text=" + str(self.text) + ")"

#
# Slide types
#


class SlideFromFile(Slide):
    def __init__(self, path, text):
        super().__init__(graphic.Image(path=path), SlideText(text=text))
