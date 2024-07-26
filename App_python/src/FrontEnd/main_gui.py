import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import Qt
from src.BackEnd import screen_utils
import src.BackEnd.json_utils as Json_utils


class Window:
    def __init__(self):
        _get_info_instance = screen_utils.get_info()
        Json_utils_instance = Json_utils.actions()
        _lengh_percentage, _high_percentage = Json_utils_instance.read_config("FrontEnd_config", "App_window")
        self.monitor_id = Json_utils_instance.read_config("FrontEnd_config", "App_def_screenId")
        self.screen_x, self.screen_y, self.window_width, self.window_height = \
            _get_info_instance.window_geometry(_lengh_percentage, _high_percentage)

    def root(self):
        app = QApplication(sys.argv)

        mainwindow = QMainWindow()
        mainwindow.setGeometry(self.screen_x, self.screen_y, self.window_width, self.window_height)

        screens = QApplication.screens()

        if self.monitor_id < len(screens):
            screen_geometry = screens[self.monitor_id].geometry()
            screen_center = screen_geometry.center()

            # window settings
            window_geometry = mainwindow.frameGeometry()
            window_geometry.moveCenter(screen_center)
            mainwindow.move(window_geometry.topLeft())
        else:
            print(f"Monitor ID {self.monitor_id} neexistuje.")
            return

        mainwindow.setWindowTitle("Ryu's Foo thing")
        mainwindow.show()

        sys.exit(app.exec())


def run():
    window_instance = Window()
    window_instance.root()
