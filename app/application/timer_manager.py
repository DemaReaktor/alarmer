from app.domain.effects_executer import EffectsExecuter
from PyQt6.QtCore import QTimer
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow
from app.application.classes.settings import TimersSettings, BreakSettings, EffectsSettings
from typing import Callable


class TimerManager:
    def __init__(self, window: QMainWindow,
            timer_settings: TimersSettings,
    ):
        self.timer_settings = timer_settings
        self.window = window
        self.executor = EffectsExecuter()
        self.timer_out: Callable[[bool], None] | None = None
        self.timer = None
        self.pause_effects: bool = False

    def start_timer(self, job_time: bool = True):
        full_time = (self.timer_settings.job_time if job_time else self.timer_settings.break_time) * 60_000
        self.executor(parent=self.window, time=full_time)
        self.timer = QTimer(self.window)
        start_time = datetime.now()
        self.timer.timeout.connect(lambda: self.on_time(job_time, start_time))
        self.timer.start(1_000)

    def on_time(self, job_time: bool, start_time: datetime):
        now_time = datetime.now()
        difference = int((now_time - start_time).total_seconds() * 1_000)
        self.executor.on_time(difference)
        full_time = (self.timer_settings.job_time if job_time else self.timer_settings.break_time) * 60_000
        if difference >= full_time:
            self.stop()
            self.timer_out(job_time)

    def stop(self):
        if self.timer is not None:
            self.timer.stop()
            self.timer = None
        self.executor.pause()
        if not self.pause_effects:
            self.stop_effects()

    def stop_effects(self):
        self.executor.stop()
        self.executor.clear()
