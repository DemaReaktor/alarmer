import sys

from PyQt6.QtWidgets import QMenu, QSystemTrayIcon
from PyQt6.QtGui import QIcon
import os
from app.presentation.windows.main import MainWindow


class BackgroundModeWindow(QSystemTrayIcon):
    pause_text = ('зупинити', 'почати')

    def __init__(self):
        super().__init__()

        self.parent_window = MainWindow()
        self.parent_window.change_timer_state_action_list.append(self.change_pause_text)

        self.setIcon(QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "images",
            "icon.png"))))

        menu = QMenu()
        menu.addAction(' ')
        self.pause = menu.addAction(self.pause_text[0])
        self.pause.triggered.connect(lambda: self.parent_window.change_timer_state(
            not self.parent_window.is_timer_executed))

        open_button = menu.addAction('відкрити програму')
        open_button.triggered.connect(self.open_window)

        exit_button = menu.addAction('закрити програму')
        exit_button.triggered.connect(sys.exit)

        self.setContextMenu(menu)
        self.activated.connect(self.on_click)

    def on_click(self, value):
        if value == QSystemTrayIcon.ActivationReason.Trigger:
            self.open_window()

    def open_window(self):
        self.parent_window.show()

    def change_pause_text(self, state):
        self.pause.setText(self.pause_text[0] if state else self.pause_text[1])
