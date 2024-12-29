from PyQt6 import QtWidgets, QtGui
from app.presentation.ui_storage import UIStorage
from app.application.settings import EffectsSettings
import os


class EffectsDialog(QtWidgets.QDialog):
    def __init__(self, settings: EffectsSettings | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        UIStorage.loadUI('effects', self)
        self.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "images",
            "icon.png"))))
        self.ok_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.close)
        self.settings = settings
        self.black_box.setChecked(self.settings.black_monitor)
        self.mouse_box.setChecked(self.settings.mouse_stop)
        self.pause_box.setChecked(self.settings.pause)

    def accept_clicked(self):
        self.settings = EffectsSettings(
            mouse_stop=self.mouse_box.isChecked(),
            black_monitor=self.black_box.isChecked(),
            pause=self.pause_box.isChecked()
        )
        self.close()
