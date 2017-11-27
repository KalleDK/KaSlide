from . import graphic
from . import projector


def create_slideshow(fullscreen, debug, wheel):
    keyboard = projector.SlideShowKeyboard()
    return projector.SlideShow(graphic.Display(fullscreen=fullscreen, debug=debug), wheel, keyboard)
