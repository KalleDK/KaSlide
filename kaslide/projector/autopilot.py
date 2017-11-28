import pyglet


class AutoPilot:
    def __init__(self, slide_show):
        self.slide_show = slide_show
        self.running = False

        slide_show.push_handlers(on_slide_changed=self.on_slide_changed, on_close=self.on_close)

    def display_next(self, dt):
        self.slide_show.display_next_slide()

    def schedule(self):
        pyglet.clock.schedule_once(self.display_next, self.slide_show.current_slide.timeout)

    def unschedule(self):
        pyglet.clock.unschedule(self.display_next)

    def start(self):
        self.running = True
        self.schedule()

    def stop(self):
        self.running = False
        self.unschedule()

    def toggle_stop(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def on_slide_changed(self):
        if self.running:
            self.unschedule()
            self.schedule()

    def on_close(self):
        self.stop()
