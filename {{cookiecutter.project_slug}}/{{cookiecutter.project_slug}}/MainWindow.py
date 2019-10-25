import sys
from PyQt5 import uic

from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog,
                             QLabel, QMainWindow, QVBoxLayout, QCheckBox,
                             QButtonGroup, QAbstractButton, QPushButton, QRadioButton)

from {{cookiecutter.project_slug}}.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        """Initialize the components of the main window."""
        self.ui = Ui_MainWindow()
        # uic.loadUi('MainWindow.ui', self)
        self.ui.setupUi(self)

        self.show()


def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
