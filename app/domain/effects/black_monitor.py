from app.domain.effect import Effect
from dataclasses import dataclass
from app.domain.effect import EffectSettings
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPalette, QColor


class BlackMonitorEffect(Effect):
    def __call__(self, *args, **kwargs):
        self.window = QtWidgets.QMainWindow()
        self.window.showMaximized()
        # TODO: black
        self.window.palette().window().setColor(QColor(0))
        self.window.show()

    def stop(self):
        self.window.close()

