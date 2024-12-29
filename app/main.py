import sys

from PyQt6 import QtWidgets
from app.presentation.windows.background_mode_window import BackgroundModeWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    background_window = BackgroundModeWindow()
    background_window.parent_window.stop_timer()
    background_window.show()
    sys.exit(app.exec())
