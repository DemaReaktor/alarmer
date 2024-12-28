from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from app.presentation.ui_storage import UIStorage
from app.presentation.windows.timer import TimerDialog
from app.presentation.windows.break_window import BreakDialog
from app.presentation.windows.effects import EffectsDialog
from app.application.classes.settings import TimersSettings, BreakSettings, EffectsSettings
from app.application.effects.application_timer import ApplicationTimerEffect
from app.application.effects.black_monitor import BlackMonitorEffect
from app.application.effects.mouse_stop import StopMouseEffect
from app.application.settings_storage import SettingsStorage
from app.application.timer_manager import TimerManager


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        UIStorage.loadUI('main', self)
        self.showMaximized()
        self.timer_button.clicked.connect(self.open_timer)
        self.break_button.clicked.connect(self.open_break)
        self.effects_button.clicked.connect(self.open_effects)
        self.timer_settings = SettingsStorage.try_load('timer.json', TimersSettings)
        self.break_settings = SettingsStorage.try_load('break.json', BreakSettings)
        self.effects_settings = SettingsStorage.try_load('effects.json', EffectsSettings)
        self.start_button.clicked.connect(lambda: self.start())
        self.timer_manager = TimerManager(self, self.timer_settings, self.break_settings, self.effects_settings)
        self.timer_manager.timer_out = lambda job: self.time_out(job)
        self.label = None
        self.stop_break = None

    def start(self, job_time: bool = True):
        self.timer_manager.update_settings(self.timer_settings, self.break_settings, self.effects_settings)
        self.timer_manager.executor.effects.clear()
        if job_time and self.timer_settings.show_timer:
            self.timer_manager.executor.effects.append(ApplicationTimerEffect())
        if not job_time:
            if self.effects_settings.black_monitor:
                self.timer_manager.executor.effects.append(BlackMonitorEffect())
            if self.timer_settings.show_timer:
                self.timer_manager.executor.effects.append(ApplicationTimerEffect())
            if self.effects_settings.mouse_stop:
                self.timer_manager.executor.effects.append(StopMouseEffect())
        self.timer_manager.start_timer(job_time)

    def time_out(self, job_time: bool):
        if job_time:
            self.start(False)
            return

        if not self.break_settings.wait_activity:
            self.start()
            return

        self.stop_break = QtWidgets.QWidget()
        self.stop_break.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.stop_break.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(self.stop_break)
        self.label.setStyleSheet("font-size: 30px;")
        self.label.setText('Перерва закінчилась, можете продовжити (достатньо навести на цей текст)')
        self.label.adjustSize()
        self.stop_break.adjustSize()
        self.label.mouseMoveEvent = lambda x: self.stop_waiting()
        self.label.setMouseTracking(True)
        self.stop_break.show()

    def stop_waiting(self):
        self.label.setMouseTracking(False)
        self.stop_break.close()
        self.label = None
        self.stop_break = None
        self.start()

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
            SettingsStorage.save(self.timer_settings, 'timer.json')

    def on_close_break(self, dialog):
        if dialog.settings is not None:
            self.break_settings = dialog.settings
            SettingsStorage.save(self.break_settings, 'break.json')

    def on_close_effects(self, dialog):
        if dialog.settings is not None:
            self.effects_settings = dialog.settings
            SettingsStorage.save(self.effects_settings, 'effects.json')
