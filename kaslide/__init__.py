from . import graphic
from . import projector


def create_wheel(slides):
    return projector.Wheel(slides=slides)


def create_plane(width, height):
    return graphic.Plane(width=width, height=height)


def create_projector(fullscreen, resizable, default_image, default_text, debug, wheel, plane=graphic.Plane(800, 600)):
    display = graphic.Display(
        default_image=default_image,
        default_text=default_text,
        plane=plane,
        fullscreen=fullscreen,
        resizable=resizable,
        debug=debug
    )
    return projector.Projector(display, wheel)
