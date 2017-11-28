import pyglet
from . import entity


class Window(pyglet.event.EventDispatcher):
    def __init__(self, fullscreen=False, debug=False):
        self._window = pyglet.window.Window(fullscreen=fullscreen)

        if debug:
            self._window.push_handlers(pyglet.window.event.WindowEventLogger())

        self._window.push_handlers(on_draw=self.draw, on_resize=self.resize, on_close=self.close, on_key_press=self.key_press)

    @property
    def width(self):
        return self._window.width

    @property
    def height(self):
        return self._window.height

    @property
    def fullscreen(self):
        return self._window.fullscreen

    def register_figure(self, figure):
        self.push_handlers(on_draw=figure.draw, on_resize=figure.resize)

        figure.resize(entity.Plane(self.width, self.height))

    def set_fullscreen(self, fullscreen):
        self._window.set_fullscreen(fullscreen=fullscreen)

    def toggle_fullscreen(self):
        self.set_fullscreen(not self.fullscreen)

    # Event
    def key_press(self, symbol, modifiers):
        self.dispatch_event('on_key_press', symbol, modifiers)

    def close(self):
        self.dispatch_event('on_close')

    def draw(self):
        self._window.clear()
        self.dispatch_event('on_draw')

    def resize(self, width, height):
        self.dispatch_event('on_resize', entity.Plane(width=width, height=height))

Window.register_event_type('on_close')
Window.register_event_type('on_draw')
Window.register_event_type('on_resize')
Window.register_event_type('on_key_press')
