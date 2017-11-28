import pyglet
from . import entity


def pixel_per_pp(dpi):
    return 72 / dpi


def fit_to_plane(label: pyglet.text.Label, plane: entity.Plane):
    label.font_size = plane.height * 0.1 * pixel_per_pp(label.dpi)
    label.anchor_x = 'right'
    label.anchor_y = 'bottom'
    label.font_name = 'Times New Roman'


def fit_front_to_plane(label: pyglet.text.Label, plane: entity.Plane):
    fit_to_plane(label, plane)
    label.x = plane.width - plane.width * 0.1
    label.y = plane.height * 0.1
    label.color = (255, 255, 255, 255)


def fit_shadow_to_plane(label: pyglet.text.Label, plane: entity.Plane):
    fit_to_plane(label, plane)
    label.x = plane.width - plane.width * 0.098
    label.y = plane.height * 0.098
    label.color = (0, 0, 0, 255)


def draw(label: pyglet.text.Label):
    label.draw()


class Label(entity.Entity):

    fit_front_to_plane = staticmethod(fit_front_to_plane)
    fit_shadow_to_plane = staticmethod(fit_shadow_to_plane)

    def __init__(self, plane, text):
        self._plane = plane
        self._front = pyglet.text.Label(text=text)
        self._shadow = pyglet.text.Label(text=text)

        self.fit_front_to_plane(self._front, self._plane)
        self.fit_shadow_to_plane(self._shadow, self._plane)

    def set_text(self, text):
        self._front = pyglet.text.Label(text=text)
        self._shadow = pyglet.text.Label(text=text)

        self.fit_front_to_plane(self._front, self._plane)
        self.fit_shadow_to_plane(self._shadow, self._plane)

    def resize(self, plane: entity.Plane):
        self._plane = plane
        self.fit_front_to_plane(self._front, self._plane)
        self.fit_shadow_to_plane(self._shadow, self._plane)

    def draw(self):
        draw(self._shadow)
        draw(self._front)
