from app.domain.effect import Effect
from dataclasses import dataclass
from app.domain.effect import EffectSettings
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor


class BlackMonitorEffect(Effect):
    def __call__(self, *args, **kwargs):
        self.window = QtWidgets.QMainWindow()
        self.window.setStyleSheet("background-color: black;")
        self.window.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.window.showMaximized()
        self.window.show()

    def stop(self):
        self.window.close()
