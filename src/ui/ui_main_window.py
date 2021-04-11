# -*- coding: utf-8 -*-

# Form layout please see a generated ui file 'MBTA_window_qtdesign.ui'
#
# WARNING! All changes made in this file might be lost if after running ui_to_py_converter_helper.py!
import logging
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

_logger = logging.getLogger(__name__)


class MBTAMainWindow(Qt.QWidget):

    def __init__(self, mbta):
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MBTA Schedule")
        self.mbta = mbta

    def setupUi(self, main_window_widget):
        main_window_widget.setObjectName("main_window_widget")
        main_window_widget.resize(480, 470)
        main_window_widget.setInputMethodHints(QtCore.Qt.ImhNone)
        main_window_widget.setAnimated(True)
        main_window_widget.setTabShape(QtWidgets.QTabWidget.Triangular)

        # Create the layout to hold the form components
        self.form_layout_widget = QtWidgets.QWidget(main_window_widget)
        self.form_layout_widget.setGeometry(QtCore.QRect(60, 140, 351, 291))
        self.form_layout_widget.setObjectName("form_layout_widget")
        self.route_selection = QtWidgets.QFormLayout(self.form_layout_widget)
        self.route_selection.setContentsMargins(0, 0, 0, 0)
        self.route_selection.setObjectName("route_selection")

        # Create route label and combo box
        self.route_label = QtWidgets.QLabel(self.form_layout_widget)
        self.route_label.setObjectName("line_label")
        self.route_selection.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.route_label)
        self.route_combo_box = QtWidgets.QComboBox(self.form_layout_widget)
        self.route_combo_box.setObjectName("line_combo_box")
        self.route_combo_box.currentIndexChanged.connect(self.handle_line_change)
        self.route_selection.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.route_combo_box)

        # Create stop label and combo box
        self.stop_label = QtWidgets.QLabel(self.form_layout_widget)
        self.stop_label.setObjectName("stop_label")
        self.route_selection.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.stop_label)
        self.stop_combo_box = QtWidgets.QComboBox(self.form_layout_widget)
        self.stop_combo_box.setObjectName("stop_combo_box")
        self.stop_combo_box.setMinimumSize(QtCore.QSize(141, 21))
        self.stop_combo_box.currentIndexChanged.connect(self.handle_stop_change)
        self.route_selection.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stop_combo_box)

        # Create direction label and combo box
        self.direction_label = QtWidgets.QLabel(self.form_layout_widget)
        self.direction_label.setObjectName("direction_label")
        self.route_selection.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.direction_label)
        self.direction_combo_box = QtWidgets.QComboBox(self.form_layout_widget)
        self.direction_combo_box.setObjectName("direction_combo_box")
        self.direction_combo_box.setMinimumSize(QtCore.QSize(141, 21))
        self.direction_combo_box.currentIndexChanged.connect(self.hand_direction_change)
        self.route_selection.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.direction_combo_box)

        # Create refresh button
        self.refresh_button = QtWidgets.QPushButton(self.form_layout_widget)
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.clicked.connect(self.display_prediction)
        self.route_selection.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.refresh_button)

        # Create prediction box
        self.predicted_label = QtWidgets.QLabel(self.form_layout_widget)
        self.predicted_label.setObjectName("predicted_label")
        self.route_selection.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.predicted_label)
        self.predicted_line_edit = QtWidgets.QPlainTextEdit(self.form_layout_widget)
        self.predicted_line_edit.setEnabled(False)
        self.predicted_line_edit.setMinimumSize(QtCore.QSize(100, 94))
        self.predicted_line_edit.setObjectName("predicted_line_edit")
        self.route_selection.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.predicted_line_edit)

        # Load MBTA logo
        self.set_application_logo(main_window_widget)

        # Create status bar
        self.create_status_bar(main_window_widget)

        # Create menu bar
        self.create_menu_bar(main_window_widget)

        self.retranslateUi(main_window_widget)
        QtCore.QMetaObject.connectSlotsByName(main_window_widget)

        self.populate_lines_combo_box()

    def set_application_logo(self, main_window_widget):
        self.logo_placeholder = QtWidgets.QLabel(main_window_widget)
        self.logo_placeholder.setGeometry(QtCore.QRect(180, 25, 111, 101))
        self.logo_placeholder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_placeholder.setText("")
        self.logo_placeholder.setPixmap(QtGui.QPixmap("resources/images/1000px-MBTA.png"))
        self.logo_placeholder.setScaledContents(True)
        self.logo_placeholder.setObjectName("logo_placeholder")

    def create_status_bar(self, main_window):
        # Create status bar
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName('statusBar')
        main_window.setStatusBar(self.status_bar)

    def create_menu_bar(self, main_window):
        # Create menu
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 799, 22))
        self.menu_bar.setObjectName('menuBar')
        self.menu_bar.setNativeMenuBar(False)

        # Add menu bar to main window
        main_window.setMenuBar(self.menu_bar)

        # Create 'File > Reset' menu item
        self.action_reset = QtWidgets.QAction(main_window)
        self.action_reset.setObjectName('actionExit')
        self.action_reset.setShortcut("Ctrl+R")
        self.action_reset.setStatusTip('Reset input')
        self.action_reset.triggered.connect(MBTAMainWindow.quitting)

        # Create 'File > Exit' menu item
        self.action_exit = QtWidgets.QAction(main_window)
        self.action_exit.setObjectName('action_exit')
        self.action_exit.setShortcut("Ctrl+X")
        self.action_exit.setStatusTip('Close application')
        self.action_exit.triggered.connect(MBTAMainWindow.quitting)

        # Set the menu bar
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName('menu_file')
        self.menu_file.addAction(self.action_reset)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_bar.addAction(self.menu_file.menuAction())

    def populate_lines_combo_box(self):
        self.route_combo_box.addItem('')
        for route in self.mbta.routes.values():
            self.route_combo_box.addItem(route.name)

    def populate_stops_combo_box(self, current_route_text):
        self.stop_combo_box.clear()
        if current_route_text:
            self.stop_combo_box.addItems(self.mbta.fetch_stops(current_route_text))

    def populate_direction_combo_box(self, current_route_text):
        self.direction_combo_box.clear()
        if current_route_text:
            self.direction_combo_box.addItem(self.mbta.routes[current_route_text].directions[0])
            self.direction_combo_box.addItem(self.mbta.routes[current_route_text].directions[1])

    def handle_line_change(self):
        current_route_text = self.route_combo_box.currentText()
        self.populate_stops_combo_box(current_route_text)
        self.populate_direction_combo_box(current_route_text)
        self.display_prediction()

    def handle_stop_change(self):
        self.display_prediction()

    def hand_direction_change(self):
        self.display_prediction()

    def display_prediction(self):
        prediction_string = ''
        current_route_text = self.route_combo_box.currentText()
        stop_name = self.stop_combo_box.currentText()
        direction_id = self.direction_combo_box.currentIndex()
        if current_route_text and stop_name:
            predicted_times = self.mbta.get_predictions(current_route_text, stop_name, direction_id)
            prediction_string = '\n'.join(predicted_times)

        self.predicted_line_edit.clear()
        self.predicted_line_edit.insertPlainText(prediction_string)

    def reset(self):
        self.route_combo_box.clear()
        self.stop_combo_box.clear()
        self.direction_combo_box.clear()

    """

    """

    @staticmethod
    def quitting():
        try:
            QtWidgets.qApp.quit()
        except:
            _logger.critical("Something went wrong while trying to stop the MBTA schedule application ... ")
            print("====== TRACED =====")
            traceback.print_exc()

    def retranslateUi(self, main_window_widget):
        _translate = QtCore.QCoreApplication.translate
        main_window_widget.setWindowTitle(_translate("main_window_widget", "MBTA Schedule"))
        self.route_label.setText(_translate("main_window_widget", "Line"))
        self.stop_label.setText(_translate("main_window_widget", "Stop"))
        self.direction_label.setText(_translate("main_window_widget", "Direction"))
        self.predicted_label.setText(_translate("main_window_widget", "Predicted"))
        self.refresh_button.setText(_translate("main_window_widget", "Refresh"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_reset.setText(_translate("MainWindow", "Reset"))
