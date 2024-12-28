from PyQt6 import QtCore, QtGui, QtWidgets
from app.domain.effect import Effect


class ApplicationTimerEffect(Effect):
    def __init__(self):
        super().__init__()

        self.window = QtWidgets.QWidget()
        self.window.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(self.window)
        self.label.setStyleSheet("font-size: 40px;")
        self.label.setText('00:00:00')
        self.label.adjustSize()
        self.time = None
        self.window.adjustSize()
        screen = QtGui.QGuiApplication.screens()[0].size()
        self.window.setGeometry(screen.width() - self.window.width(),
            screen.height() - self.window.height(), self.window.width(), self.window.height())

    def __call__(self, *args, **kwargs):
        self.time = kwargs['time']
        self.on_time(0)
        self.window.show()

    def on_time(self, time: int):
        self.label.setText(f'{int((self.time - time) / 60_000)}: {int((self.time - time) / 1000) % 60}')

    def stop(self):
        self.window.close()
