import collections


class Wheel:
    def __init__(self, slides):
        self._slides = collections.deque(slides)

    def rotate_right(self):
        self._slides.rotate(-1)

    def rotate_left(self):
        self._slides.rotate(1)

    @property
    def current_slide(self):
        return self._slides[0]

    def get_slide(self):
        return self._slides[0]
