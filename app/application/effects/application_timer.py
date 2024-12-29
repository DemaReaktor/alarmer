from PyQt6 import QtCore, QtGui, QtWidgets
from app.domain.effect import Effect


class ApplicationTimerEffect(Effect):
    def __init__(self):
        super().__init__()

        self.window = QtWidgets.QWidget()
        self.window.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.labels = [QtWidgets.QLabel(self.window) for _ in range(5)]
        for index, label in enumerate(self.labels):
            label.setStyleSheet("font-size: 40px; font-weight: bold;")
            if index != 4:
                x = 5 if index % 2 == 0 else -5
                y = 5 if index > 1 else -5
                label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
                    blurRadius=10, xOffset=x, yOffset=y, color=QtGui.QColor('black')))
                label.setText('00:00:00')
                label.adjustSize()
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
        for label in self.labels:
            label.setText(f' {int((self.time - time) / 60_000)}: {int((self.time - time) / 1000) % 60} ')

    def pause(self):
        self.window.close()
        self.window = None
        self.time = None

    def stop(self):
        pass
