import pyglet

from .picture import PictureFitWindow
from .label import LabelWithShadow
from .window import Window


class Display(pyglet.event.EventDispatcher):
    def __init__(self, fullscreen=False, debug=False):
        super().__init__()

        self.window = Window(fullscreen=fullscreen, debug=debug)

        self.label = LabelWithShadow(self.window.width, self.window.height)
        self.window.register_figure(self.label)

        self.picture = PictureFitWindow(self.window.width, self.window.height,
                                        img=self.create_default_image())
        self.window.register_figure(self.picture)

        self.window.push_handlers(on_close=self.close, on_key_press=self.key_press)

    def create_default_image(self, color=(0, 0, 0, 0)):
        return pyglet.image.SolidColorImagePattern(color=color).create_image(self.window.width, self.window.height)

    def set_label(self, text):
        self.label.set_text(text)

    def set_picture(self, img):
        self.picture.set_image(img)

    def toggle_fullscreen(self):
        self.window.toggle_fullscreen()

    def close(self):
        self.dispatch_event('on_close')

    def key_press(self, symbol, modifiers):
        self.dispatch_event('on_key_press', symbol, modifiers)


Display.register_event_type('on_close')
Display.register_event_type('on_key_press')

