from PyQt6 import QtWidgets
from app.presentation.ui_storage import UIStorage
from app.application.classes.settings import TimersSettings


class TimerDialog(QtWidgets.QDialog):
    def __init__(self, settings: TimersSettings | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        UIStorage.loadUI('timer', self)
        self.ok_button.clicked.connect(self.accept_clicked)
        self.cancel_button.clicked.connect(self.close)
        self.settings = settings
        self.job_text.setText(str(self.settings.job_time))
        self.break_text.setText(str(self.settings.break_time))
        self.timer_box.setChecked(self.settings.show_timer)

    def accept_clicked(self):
        self.settings = TimersSettings(float(self.job_text.text().replace(',', '.')),
                float(self.break_text.text().replace(',', '.')),
            self.timer_box.isChecked())
        self.close()
