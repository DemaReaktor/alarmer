from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(init=True)
class EffectSettings:
    pass


class Effect[Settings: EffectSettings](ABC):
    def __init__(self, settings: Settings):
        self.settings = settings

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def stop(self):
        pass
