from .sprite import Sprite, draw, fit_to_plane
from .entity import Entity, Plane
from . import image
import pyglet


def create_sprite(img) -> Sprite:
    return Sprite(img=image.load(img))


def create_plane(width, height) -> Plane:
    return Plane(width=width, height=height)


class Picture(pyglet.event.EventDispatcher):

    def __init__(self, plane, img):
        self._plane = plane
        self._sprite = create_sprite(img)
        self.resize_sprite()

    def set_image(self, img):
        old_sprite = self._sprite
        self._sprite = create_sprite(img)
        self.resize_sprite()
        if old_sprite:
            old_sprite.delete()

    def resize(self, plane):
        self._plane = plane
        self.resize_sprite()

    def resize_sprite(self):
        self.dispatch_event('on_sprite_resize', self._sprite, self._plane)

    def draw(self):
        draw(self._sprite)

    def on_sprite_resize(self, sprite, plane):
        fit_to_plane(sprite, plane)

Picture.register_event_type('on_sprite_resize')
