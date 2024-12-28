from app.domain.effect import Effect
from pynput.keyboard import Key, Controller


class PauseEffect(Effect):
    def __init__(self):
        super().__init__()
        self.controller = Controller()

    def __call__(self, *args, **kwargs):
        self.controller.press(Key.media_play_pause)

    def stop(self):
        self.controller.press(Key.media_play_pause)
