from app.domain.effects_executer import EffectsExecuter
from app.application.effects.application_timer import ApplicationTimerEffect
from app.application.effects.black_monitor import BlackMonitorEffect
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

    # def start(self):
    #     self.executor.effects.append(BlackMonitorEffect())
    #     # executor.effects.append(StopMouseEffect())
    #     self.executor.effects.append(ApplicationTimerEffect())
    #     self.executor(parent=self.window, time=self.timer_settings.job_time * 60_000)
    #     timer = QTimer(self)
    #     start_time = datetime.now()
    #     timer.timeout.connect(lambda: self.on_time(timer, self.executor, start_time))
    #     timer.start(1_000)

    def start_timer(self, job_time: bool = True):
        if not job_time:
            self.executor(parent=self.window, time=self.timer_settings.break_time * 60_000)
        timer = QTimer(self)
        start_time = datetime.now()
        timer.timeout.connect(lambda: self.on_time(timer, start_time,
            self.executor if not job_time else None))
        timer.start(1_000)

    def on_job_time(self, timer: QTimer, start_time: datetime):
        now_time = datetime.now()
        difference = int((now_time - start_time).total_seconds() * 1_000)
        if difference >= self.timer_settings.job_time * 60_000:
            timer.stop()
            self.timer_out(True)

    def on_break_time(self, timer: QTimer, start_time: datetime, effect_executor: EffectsExecuter):
        now_time = datetime.now()
        difference = int((now_time - start_time).total_seconds() * 1_000)
        effect_executor.on_time(difference)
        if difference >= self.timer_settings.break_time * 60_000:
            effect_executor.stop()
            timer.stop()
            self.timer_out(False)
