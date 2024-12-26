from PyQt6 import QtWidgets
from app.presentation.ui_storage import UIStorage


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        UIStorage.loadUI('main', self)
        self.timer_button.clicked.connect(lambda x: UIStorage.find('timer'))


    # dialog.show()
    # dialog.start_button: QtWidgets.QPushButton
    # g = EffectsExecuter()
    # g.effects.append(PrinterEffect(PS('1')))
    # g.effects.append(PrinterEffect(PS('2')))
    # timer = QTimer(dialog)
