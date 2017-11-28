import pyglet
from .wheel import Wheel
from .autopilot import AutoPilot
from .keyboard import Keyboard

from .. import graphic


def rotate_forward(wheel: Wheel):
    wheel.rotate_right()


def rotate_backward(wheel: Wheel):
    wheel.rotate_left()


def display_default(display: graphic.Display):
    display.remove_picture()
    display.remove_label()


def display_slide(display: graphic.Display, slide):
    display.set_picture(slide.image)
    display.set_label(slide.text.text)


def display_current_slide(display: graphic.Display, wheel: Wheel):
    display_slide(display, wheel.current_slide)


def display_next_slide(display: graphic.Display, wheel: Wheel):
    rotate_forward(wheel)
    display_current_slide(display, wheel)


def display_previous_slide(display: graphic.Display, wheel: Wheel):
    rotate_backward(wheel)
    display_current_slide(display, wheel)


class Projector(pyglet.event.EventDispatcher):
    def __init__(self, display, slide_wheel: Wheel):
        self.display = display
        self.wheel = slide_wheel
        self.autopilot = AutoPilot(self)
        self.keyboard = Keyboard(self)
        self.running = False

        display.push_handlers(on_key_press=self.on_display_key_press, on_close=self.on_display_close)

    @property
    def current_slide(self):
        return self.wheel.current_slide

    def display_current_slide(self):
        display_slide(self.display, self.wheel.current_slide)
        self.dispatch_event('on_slide_changed')

    def display_next_slide(self):
        display_next_slide(self.display, self.wheel)
        self.dispatch_event('on_slide_changed')

    def display_previous_slide(self):
        display_previous_slide(self.display, self.wheel)
        self.dispatch_event('on_slide_changed')

    def toggle_fullscreen(self):
        self.display.toggle_fullscreen()

    def close(self):
        self.display.close()

    def resume(self):
        self.autopilot.start()

    def pause(self):
        self.autopilot.stop()

    def toggle_pause(self):
        self.autopilot.toggle_stop()

    def start(self):
        self.running = True
        self.resume()
        display_current_slide(self.display, self.wheel)

    def stop(self):
        self.running = False
        self.pause()
        display_default(self.display)

    def toggle_stop(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def on_display_close(self):
        self.dispatch_event('on_close')

    def on_display_key_press(self, symbol, modifiers):
        self.dispatch_event('on_key_press', symbol, modifiers)

    def on_close(self):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_slide_changed(self):
        pass


Projector.register_event_type('on_key_press')
Projector.register_event_type('on_close')
Projector.register_event_type('on_slide_changed')


