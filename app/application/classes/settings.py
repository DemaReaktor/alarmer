from dataclasses import dataclass


@dataclass(init=True)
class TimersSettings:
    job_time: int = 30
    break_time: int = 5
    show_timer: bool = False


@dataclass(init=True)
class BreakSettings:
    wait_activity: bool = True


@dataclass(init=True)
class EffectsSettings:
    black_monitor: bool = True
    mouse_stop: bool = True
    timer: bool = False
