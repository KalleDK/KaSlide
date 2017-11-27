from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


class Entity:

    def draw(self):
        pass

    def resize(self, width, height):
        pass

