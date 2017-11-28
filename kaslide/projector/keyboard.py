import pyglet


class Keyboard:
    def __init__(self, projector):
        self.projector = projector

        projector.push_handlers(on_key_press=self.on_key_press)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.projector.display_previous_slide()

        if symbol == pyglet.window.key.RIGHT:
            self.projector.display_next_slide()

        if symbol == pyglet.window.key.P:
            self.projector.toggle_pause()

        if symbol == pyglet.window.key.S:
            self.projector.toggle_stop()

        if symbol == pyglet.window.key.SPACE:
            self.projector.toggle_fullscreen()
