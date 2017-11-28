from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])

Plane = namedtuple('Plane', ['width', 'height'])


class Entity:

    def draw(self):
        pass

    def resize(self, plane):
        pass



