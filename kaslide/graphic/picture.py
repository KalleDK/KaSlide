from . import sprite
from .entity import Entity, Point, Plane
from . import image


def create_sprite(img) -> sprite.Sprite:
    return sprite.Sprite(img=image.load(img))


def create_plane(width, height) -> Plane:
    return Plane(width=width, height=height)


class Picture(Entity):

    def __init__(self, plane, img):
        self._plane = plane
        self._sprite = create_sprite(img)
        sprite.fit_to_plane(self._sprite, self._plane)

    def set_image(self, img):
        old_sprite = self._sprite
        self._sprite = create_sprite(img)
        sprite.fit_to_plane(self._sprite, self._plane)
        if old_sprite:
            old_sprite.delete()

    def resize(self, plane):
        self._plane = plane
        sprite.fit_to_plane(self._sprite, self._plane)

    def draw(self):
        sprite.draw(self._sprite)
