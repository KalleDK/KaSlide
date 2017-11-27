import pyglet


class SlideShowKeyboard(pyglet.event.EventDispatcher):
    def __init__(self):
        self.slide_show = None

    def assign(self, slide_show):
        self.slide_show = slide_show
        self.slide_show.push_handlers(self.on_key_press)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.slide_show.display_previous_slide()

        if symbol == pyglet.window.key.RIGHT:
            self.slide_show.display_next_slide()

        if symbol == pyglet.window.key.P:
            if self.slide_show.running:
                self.slide_show.pause()
            else:
                self.slide_show.resume()

        if symbol == pyglet.window.key.SPACE:
            self.slide_show.toggle_fullscreen()
