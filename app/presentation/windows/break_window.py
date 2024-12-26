from PyQt6 import QtWidgets
from app.presentation.ui_storage import UIStorage
from app.application.classes.settings import BreakSettings


class BreakDialog(QtWidgets.QDialog):
    def __init__(self, settings: BreakSettings | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        UIStorage.loadUI('break', self)
        self.ok_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.close)
        self.settings = settings
        self.stop_box.setChecked(self.settings.wait_activity)
        
    def accept_clicked(self):
        self.settings = BreakSettings(self.stop_box.isChecked())
        self.close()
