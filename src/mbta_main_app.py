import logging
import signal
import sys

from PyQt5 import Qt, QtGui, QtWidgets

from src.backend.mbta import MBTA
from src.ui.ui_main_window import MBTAMainWindow

_logger = logging.getLogger(__name__)


class MainAppWindow(QtWidgets.QMainWindow):

    def __init__(self):
        self.mbta = MBTA()
        self.mbta.fetch_routes()
        super(MainAppWindow, self).__init__()
        self.ui = MBTAMainWindow(self.mbta)
        self.ui.setupUi(self)


# Method to quit the application if TERM or INT kill signals are sent through to the application
def terminate_signal_handler():
    Qt.QApplication.quit()


def start_ui(signal_handlers):
    control_app = Qt.QApplication(sys.argv)
    control_app.setWindowIcon(QtGui.QIcon('resources/images/1000px-MBTA.png'))

    # Load main application window
    ui_application = MainAppWindow()

    # Handle termination signals
    signal.signal(signal.SIGINT, signal_handlers)
    signal.signal(signal.SIGTERM, signal_handlers)

    # Show main application window
    ui_application.show()
    return control_app, ui_application


def main():
    app, ui = start_ui(terminate_signal_handler)

    # Application is closed normally
    app.aboutToQuit.connect(ui.ui.quitting)
    sys.exit(app.exec())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as error:
        _logger.critical("Something went wrong with the app\n", error)
