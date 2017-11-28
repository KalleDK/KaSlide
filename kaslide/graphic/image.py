import pyglet.image


def load(image):
    return pyglet.image.load(str(image.path))


class Image:
    def __init__(self, path, fp=None):
        self.path = path
        self.fp = fp

    def __str__(self):
        return "Image(path=" + self.path + ", fp=" + str(self.fp) + ")"
