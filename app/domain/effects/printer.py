from app.domain.effect import Effect
from dataclasses import dataclass
from app.domain.effect import EffectSettings


@dataclass(init=True)
class PS(EffectSettings):
    data: str


class PrinterEffect(Effect[PS]):
    def __call__(self, *args, **kwargs):
        # print(self.settings.data)
        print(self.settings.data)

    def stop(self):
        pass
