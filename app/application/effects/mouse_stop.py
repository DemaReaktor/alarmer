from app.domain.effect import Effect
from pynput.mouse import Listener, Controller


class StopMouseEffect(Effect):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.listener = Listener(
            on_move=lambda x, y: self.on_move(x, y),
        )
        
    def on_move(self, x, y):
        self.controller.move(x - self.lock_x, y - self.lock_y)

    def __call__(self, *args, **kwargs):
        self.lock_x = self.controller.position[0]
        self.lock_y = self.controller.position[1]
        self.listener.start()

    def stop(self):
        self.listener.stop()
