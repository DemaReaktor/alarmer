from PyQt6 import QtWidgets, QtGui
from app.presentation.ui_storage import UIStorage
from app.application.settings import BreakSettings
import os


class BreakDialog(QtWidgets.QDialog):
    def __init__(self, settings: BreakSettings | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        UIStorage.loadUI('break', self)
        self.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "images",
            "icon.png"))))
        self.ok_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.close)
        self.settings = settings
        self.stop_box.setChecked(self.settings.wait_activity)
        self.timer_box.setChecked(self.settings.show_timer)

    def accept_clicked(self):
        self.settings = BreakSettings(self.stop_box.isChecked(), self.timer_box.isChecked())
        self.close()
