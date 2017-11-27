import pyglet
from .wheel import SlideWheel


class SlideShow(pyglet.event.EventDispatcher):
    def __init__(self, display, slide_wheel: SlideWheel, keypad):
        self.display = display
        self.wheel = slide_wheel
        self.keypad = keypad
        self.running = False

        display.push_handlers(on_key_press=self.key_press, on_close=self.close)

        if self.keypad:
            self.keypad.assign(self)

    def slide_schedule(self, timeout):
        pyglet.clock.schedule_once(self.display_callback, timeout)

    def slide_unschedule(self):
        pyglet.clock.unschedule(self.display_callback)

    def display_callback(self, dt):
        if self.running:
            slide = self._display_next_slide()
            self.slide_schedule(slide.timeout)

    def display_next_slide(self):
        if self.running:
            self.slide_unschedule()
        slide = self._display_next_slide()
        if self.running:
            self.slide_schedule(slide.timeout)

    def display_previous_slide(self):
        if self.running:
            self.slide_unschedule()
        slide = self._display_previous_slide()
        if self.running:
            self.slide_schedule(slide.timeout)

    def _display_current_slide(self):
        slide = self.wheel.get_slide()
        img = pyglet.image.load(slide.image.filename)
        self.display.set_picture(img)
        self.display.set_label(slide.text.text)
        return slide

    def _display_next_slide(self):
        self.wheel.rotate_left()
        slide = self._display_current_slide()
        return slide

    def _display_previous_slide(self):
        self.wheel.rotate_right()
        slide = self._display_current_slide()
        return slide

    def resume(self):
        self.running = True
        slide = self._display_current_slide()
        self.slide_schedule(slide.timeout)

    def pause(self):
        self.running = False
        self.slide_unschedule()

    def toggle_fullscreen(self):
        self.display.toggle_fullscreen()

    def key_press(self, symbol, modifiers):
        self.dispatch_event('on_key_press', symbol, modifiers)

    def close(self):
        if self.running:
            self.pause()
        self.dispatch_event('on_close')

    def on_close(self):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def start(self):
        self.resume()
        pyglet.app.run()


SlideShow.register_event_type('on_key_press')
SlideShow.register_event_type('on_close')