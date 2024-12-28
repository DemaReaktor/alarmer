from app.domain.effects_executer import EffectsExecuter
from PyQt6.QtCore import QTimer
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow
from app.application.classes.settings import TimersSettings, BreakSettings, EffectsSettings
from typing import Callable


class TimerManager:
    def __init__(self, window: QMainWindow,
            timer_settings: TimersSettings,
            break_settings: BreakSettings,
            effects_settings: EffectsSettings,
    ):
        self.timer_settings = timer_settings
        self.break_settings = break_settings
        self.effects_settings = effects_settings
        self.window = window
        self.executor = EffectsExecuter()
        self.timer_out: Callable[[bool], None] | None = None

    def update_settings(self, timer_settings: TimersSettings,
            break_settings: BreakSettings,
            effects_settings: EffectsSettings):
        self.timer_settings = timer_settings
        self.break_settings = break_settings
        self.effects_settings = effects_settings

    def start_timer(self, job_time: bool = True):
        full_time = (self.timer_settings.job_time if job_time else self.timer_settings.break_time) * 60_000
        self.executor(parent=self.window, time=full_time)
        timer = QTimer(self.window)
        start_time = datetime.now()
        timer.timeout.connect(lambda: self.on_time(job_time, timer, start_time, self.executor))
        timer.start(1_000)

    def on_time(self, job_time: bool, timer: QTimer, start_time: datetime, effect_executor: EffectsExecuter):
        now_time = datetime.now()
        difference = int((now_time - start_time).total_seconds() * 1_000)
        effect_executor.on_time(difference)
        full_time = (self.timer_settings.job_time if job_time else self.timer_settings.break_time) * 60_000
        if difference >= full_time:
            effect_executor.stop()
            timer.stop()
            del timer
            effect_executor.clear()
            self.timer_out(job_time)
