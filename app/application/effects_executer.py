from app.domain.effect import Effect


class EffectsExecuter:
    def __init__(self):
        self.effects: list[Effect] = []

    def __call__(self, *args, **kwargs):
        for effect in self.effects:
            effect(*args, **kwargs)

    def stop(self):
        for effect in self.effects:
            effect.stop()
