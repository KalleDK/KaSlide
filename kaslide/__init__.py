from . import graphic
from . import projector
from .graphic import entity


def create_projector(fullscreen, default_image, default_text, debug, wheel, plane=entity.Plane(800, 600)):
    display = graphic.Display(
        default_image=default_image,
        default_text=default_text,
        plane=plane,
        fullscreen=fullscreen,
        debug=debug
    )
    return projector.Projector(display, wheel)
