from .sprite import Sprite
from .entity import Entity, Point


class Picture(Entity):
    def __init__(self, width, height, img):
        self.width = width
        self.height = height
        self._sprite = self._create_sprite(img)

    def _calculate_dimensions(self, img):
        point = Point(0, 0)
        scale = 1
        return point, scale

    def _create_sprite(self, img) -> Sprite:
        point, scale = self._calculate_dimensions(img)
        return Sprite(img=img, x=point.x, y=point.y, scale=scale)

    def _update_sprite(self):
        point, scale = self._calculate_dimensions(self._sprite.image)
        self._sprite.update(x=point.x, y=point.y, scale=scale)

    def set_image(self, img):
        self._sprite = self._create_sprite(img)

    def resize(self, width, height):
        self.width = width
        self.height = height
        self._update_sprite()

    def draw(self):
        self._sprite.draw()


class PictureFitWindow(Picture):
    def _calculate_dimensions(self, image):
        window_width = self.width
        window_height = self.height
        image_width = image.width
        image_height = image.height

        scale = min(window_width / image_width, window_height / image_height)

        x = (window_width - (image_width * scale)) / 2
        y = (window_height - (image_height * scale)) / 2

        return Point(x, y), scale
