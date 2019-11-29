import sys

from PyQt5.QtWidgets import QApplication
from control import ctl_app

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ctl_app.MainWindow()
    sys.exit(app.exec())