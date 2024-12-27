from PyQt6 import QtCore, QtGui, QtWidgets
from app.domain.effect import Effect


class ApplicationTimerEffect(Effect):
    def __init__(self):
        super().__init__()

        self.window = QtWidgets.QWidget()
        self.window.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.window.setGeometry(200, 200, 1000, 600)

        self.label = QtWidgets.QLabel(self.window)
        self.label.setStyleSheet("font-size: 40px;")
        self.label.maximumSize()
        self.time = None

    def __call__(self, *args, **kwargs):
        self.time = kwargs['time']
        self.window.show()

    def on_time(self, time: int):
        self.label.setText(f'{int((self.time - time) / 60_000)}: {int((self.time - time) / 1000) % 60}')
        self.label.adjustSize()

    def stop(self):
        self.window.close()
