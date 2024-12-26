import time

from PyQt6 import QtWidgets
from app.presentation.ui_storage import UIStorage
from app.presentation.windows.timer import TimerDialog
from app.presentation.windows.break_window import BreakDialog
from app.presentation.windows.effects import EffectsDialog
from app.application.classes.settings import TimersSettings, BreakSettings, EffectsSettings
from app.application.effects_executer import EffectsExecuter
from app.domain.effects.black_monitor import BlackMonitorEffect


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        UIStorage.loadUI('main', self)
        self.showMaximized()
        self.timer_button.clicked.connect(self.open_timer)
        self.break_button.clicked.connect(self.open_break)
        self.effects_button.clicked.connect(self.open_effects)
        self.timer_settings = TimersSettings()
        self.break_settings = BreakSettings()
        self.effects_settings = EffectsSettings()
        self.start_button.clicked.connect(self.start)

    def start(self):
        executor = EffectsExecuter()
        executor.effects.append(BlackMonitorEffect())
        executor()
        time.sleep(2)
        executor.stop()

    def open_effects(self):
        dialog = EffectsDialog(self.effects_settings)
        dialog.setParent(self)
        dialog.show()
        dialog.closeEvent = lambda x: self.on_close_effects(dialog)

    def open_break(self):
        dialog = BreakDialog(self.break_settings)
        dialog.setParent(self)
        dialog.show()
        dialog.closeEvent = lambda x: self.on_close_break(dialog)

    def open_timer(self):
        dialog = TimerDialog(self.timer_settings)
        dialog.setParent(self)
        dialog.show()
        dialog.closeEvent = lambda x: self.on_close_timer(dialog)

    def on_close_timer(self, dialog):
        if dialog.settings is not None:
            self.timer_settings = dialog.settings

    def on_close_break(self, dialog):
        if dialog.settings is not None:
            self.break_settings = dialog.settings

    def on_close_effects(self, dialog):
        if dialog.settings is not None:
            self.effects_settings = dialog.settings
