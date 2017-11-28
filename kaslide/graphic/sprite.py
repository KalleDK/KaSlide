from pyglet.sprite import Sprite
from .entity import Plane


def fit_to_plane(sprite: Sprite, plane: Plane):
    scale = min(plane.width / sprite.image.width, plane.height / sprite.image.height)

    x = (plane.width - (sprite.image.width * scale)) / 2
    y = (plane.height - (sprite.image.height * scale)) / 2

    sprite.update(x=x, y=y, scale=scale)


def draw(sprite: Sprite):
    sprite.draw()
