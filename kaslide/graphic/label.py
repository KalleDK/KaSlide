import pyglet
from .entity import Entity, Point


class Label(Entity):
    def __init__(self, width, height, x=0.1, y=0.1, font_size=0.1, anchor_x='right', anchor_y='bottom', dpi=96, **kwargs):
        self.width = width
        self.height = height
        self.offset_x = x
        self.offset_y = y
        self.font_size = font_size
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.dpi = dpi

        point, font_size = self.calculate_dimensions()

        kwargs['x'] = point.x
        kwargs['y'] = point.x
        kwargs['font_size'] = font_size
        kwargs['dpi'] = dpi or 96
        kwargs['anchor_x'] = anchor_x
        kwargs['anchor_y'] = anchor_y

        self._label = pyglet.text.Label(**kwargs)

    def calculate_dimensions(self):
        if self.anchor_x == 'left':
            x = self.width * self.offset_x
        elif self.anchor_x == 'right':
            x = self.width - self.width * self.offset_x
        else:
            x = self.width / 2

        if self.anchor_y == 'top':
            y = self.height - self.height * self.offset_y
        elif self.anchor_y == 'bottom':
            y = self.height * self.offset_y
        else:
            y = self.height / 2

        font_size = self.height * self.font_size * self.font_scale

        return Point(x, y), font_size

    def set_text(self, text):
        self._label.text = text

    def resize(self, width, height):
        self.width = width
        self.height = height
        point, font_size = self.calculate_dimensions()
        self._label.font_size = font_size
        self._label.x = point.x
        self._label.y = point.y

    def draw(self):
        self._label.draw()

    @property
    def font_scale(self):
        return 72 / self.dpi


class LabelWithShadow(Entity):
    def __init__(self, width, height, text="",
                 x=0.1, y=0.1, size=0.1,
                 anchor_x='right', anchor_y='bottom',
                 font_name='Times New Roman',
                 front_color=(255, 255, 255, 255),
                 shadow_color=(0, 0, 0, 255),
                 shadow_offset=0.002
                 ):
        self._front = Label(width, height, text=text, x=x, y=y, font_size=size, color=front_color, font_name=font_name,
                            anchor_x=anchor_x, anchor_y=anchor_y)
        self._shadow = Label(width, height, text=text, x=x-shadow_offset, y=y-shadow_offset, font_size=size,
                             color=shadow_color, font_name=font_name, anchor_x=anchor_x, anchor_y=anchor_y)

    def set_text(self, text):
        self._shadow.set_text(text)
        self._front.set_text(text)

    def resize(self, width, height):
        self._shadow.resize(width, height)
        self._front.resize(width, height)

    def draw(self):
        self._shadow.draw()
        self._front.draw()
