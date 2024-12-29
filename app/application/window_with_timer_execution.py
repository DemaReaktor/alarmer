from PyQt6 import QtWidgets
from typing import Callable


class WindowWithTimerExecution(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_timer_state_action_list: list[Callable[[bool], None]] = []
        self.is_timer_executed: bool = False

    def execute_timer(self):
        self.change_timer_state(True)

    def stop_timer(self):
        self.change_timer_state(False)

    def change_timer_state(self, executing: bool):
        self.is_timer_executed = executing
        for action in self.change_timer_state_action_list:
            action(executing)
