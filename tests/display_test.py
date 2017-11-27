import pyglet
import kaslide

SlideNormal = kaslide.projector.SlideNormal

slides = [
    SlideNormal("default.png", ""),
    SlideNormal("test1.jpg", "Test1"),
    SlideNormal("test2.jpg", "Test2"),
    SlideNormal("test3.jpg", "Test3")
]

wheel = kaslide.projector.SlideWheel(slides)

default_img = pyglet.image.SolidColorImagePattern().create_image(800, 600)

uut = kaslide.create_slideshow(fullscreen=False, debug=False, wheel=wheel)
uut.start()
