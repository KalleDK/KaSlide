import pyglet

from .picture import Picture
from .label import Label
from .window import Window

from . import entity
from . import window


class Display(pyglet.event.EventDispatcher):

    def __init__(self, default_image, default_text, plane, fullscreen=False, resizable=False, debug=False):
        super().__init__()

        self._default_image = default_image
        self._default_text = default_text
        self._window = Window(width=plane.width, height=plane.height, fullscreen=fullscreen, resizable=resizable)
        self._label = Label(plane=self.plane, text=self._default_text)
        self._picture = Picture(plane=self.plane, img=self._default_image)
        self._debug = debug

        window.register_entity(self._window, self._label)
        window.register_entity(self._window, self._picture)

        self._window.push_handlers(on_close=self.on_window_close,
                                   on_key_press=self.on_window_key_press,
                                   on_draw=self.on_window_draw)

        if self._debug:
            self.fps_display = pyglet.window.FPSDisplay(self._window)
            self._window.push_handlers(pyglet.window.event.WindowEventLogger())

    @property
    def plane(self):
        return entity.Plane(width=self._window.width, height=self._window.height)

    def set_label(self, text):
        self._label.set_text(text)
        self._window.set_caption(text)

    def remove_label(self):
        self.set_label(self._default_text)

    def set_picture(self, img):
        self._picture.set_image(img)

    def remove_picture(self):
        self.set_picture(self._default_image)

    def toggle_fullscreen(self):
        self._window.set_fullscreen(not self._window.fullscreen)

    def close(self):
        self._window.close()

    def on_window_draw(self):
        self._window.clear()
        if self._debug:
            self.fps_display.draw()

    def on_window_close(self):
        self.dispatch_event('on_close')

    def on_window_key_press(self, symbol, modifiers):
        self.dispatch_event('on_key_press', symbol, modifiers)


Display.register_event_type('on_close')
Display.register_event_type('on_key_press')

