from PyQt6 import QtWidgets
from app.presentation.ui_storage import UIStorage
from app.application.classes.settings import EffectsSettings


class EffectsDialog(QtWidgets.QDialog):
    def __init__(self, settings: EffectsSettings | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        UIStorage.loadUI('effects', self)
        self.ok_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.close)
        self.settings = settings
        self.black_box.setChecked(self.settings.black_monitor)
        self.timer_box.setChecked(self.settings.timer)
        self.mouse_box.setChecked(self.settings.mouse_stop)

    def accept_clicked(self):
        self.settings = EffectsSettings(
            mouse_stop=self.mouse_box.isChecked(),
            timer=self.timer_box.isChecked(),
            black_monitor=self.black_box.isChecked(),
        )
        self.close()