from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(init=True)
class EffectSettings:
    pass


class Effect[Settings: EffectSettings](ABC):
    def __init__(self, settings: Settings | None = None):
        self.settings = settings

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def on_time(self, time: int):
        pass
