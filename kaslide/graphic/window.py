import pyglet
from . import entity

from pyglet.window import Window


class Resize:
    def __init__(self, resize):
        self.resize = resize

    def __call__(self, width, height):
        self.resize(entity.Plane(width=width, height=height))


def register_entity(window: Window, ent: entity.Entity):
    window.push_handlers(on_draw=ent.draw, on_resize=Resize(ent.resize))
    ent.resize(entity.Plane(window.width, window.height))
