from app.domain.effect import Effect
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt


class BlackMonitorEffect(Effect):
    def __call__(self, *args, **kwargs):
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.window.setStyleSheet("background-color: black;")
        self.window.showMaximized()
        self.window.show()

    def stop(self):
        self.window.close()
        self.window = None
