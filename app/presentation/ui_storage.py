from PyQt6 import uic, QtWidgets
import os


class UIStorage:
    ui_path: str = os.path.dirname(os.path.abspath(__file__)) + '\\ui\\'

    @classmethod
    def loadUI(cls, name: str, window: QtWidgets.QMainWindow | QtWidgets.QDialog):
        uic.loadUi(cls.ui_path + name + '.ui', window)
