import os
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QTimer
from app.domain.effects.printer import PrinterEffect, PS
from app.application.effects_executer import EffectsExecuter
from app.presentation.ui_storage import UIStorage
from app.presentation.windows.main import MainWindow

if __name__ == "__main__":
    # loop = get_loop()
    # loop.call_soon(create_task, pr2())
    app = QtWidgets.QApplication(sys.argv)
    # dialog = QtWidgets.QMainWindow()
    # uic.loadUi(os.path.dirname(os.path.abspath(__file__)) + '\\presentation\\ui\\main.ui', dialog)
    # dialog.show()
    # dialog.start_button: QtWidgets.QPushButton
    # dialog.start_button.clicked.connect()
    # g = EffectsExecuter()
    # g.effects.append(PrinterEffect(PS('1')))
    # g.effects.append(PrinterEffect(PS('2')))
    # timer = QTimer(dialog)
    # timer.timeout.connect(g)
    # timer.timeout.connect(timer.stop)
    # timer.start(1000)
    window = MainWindow()
    window.show()
    exit(app.exec())
