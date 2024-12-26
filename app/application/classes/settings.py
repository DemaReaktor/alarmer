from dataclasses import dataclass


@dataclass(init=True)
class TimersSettings:
    job_time: int
    break_time: int


@dataclass(init=True)
class BreakSettings:
    show_timer: bool
    wait_activity: bool
