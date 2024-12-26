from PyQt6 import QtWidgets
from app.presentation.ui_storage import UIStorage
from app.application.classes.settings import TimersSettings


class TimerDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        UIStorage.loadUI('timer', self)
        self.ok_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.close)
        self.settings = None

    def accept_clicked(self):
        self.answer = self.settings
        self.close()

    # dialog.show()
    # dialog.start_button: QtWidgets.QPushButton
    # g = EffectsExecuter()
    # g.effects.append(PrinterEffect(PS('1')))
    # g.effects.append(PrinterEffect(PS('2')))
    # timer = QTimer(dialog)


UIStorage.ui_windows['timer'] = TimerDialog
