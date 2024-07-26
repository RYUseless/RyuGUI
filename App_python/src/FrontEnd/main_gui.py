import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from src.BackEnd import screen_utils
import src.BackEnd.json_utils as Json_utils


class App_window:
    def __init__(self):
        # instance screen_utils
        _get_info_instance = screen_utils.get_info()  # instance screen_utils
        # instance json actions
        Json_utils_instance = Json_utils.actions()
        # percentil for window size
        _length_percentage, _high_percentage = Json_utils_instance.read_config("FrontEnd_config", "App_window")
        # screen id
        self.monitor_id = Json_utils_instance.read_config("FrontEnd_config", "App_def_screenId")
        # screen X/Y values
        self.screen_x, self.screen_y, self.window_width, self.window_height, self.min_x, self.min_y = \
            _get_info_instance.window_geometry(_length_percentage, _high_percentage)
        # background color
        self.background_hex = Json_utils_instance.read_config("FrontEnd_config", "Background_color_hex")

    def root(self):
        app = QApplication(sys.argv)

        # Create the main window
        main_window = QMainWindow()
        main_window.setGeometry(self.screen_x, self.screen_y, self.window_width, self.window_height)
        main_window.setMinimumSize(self.min_x, self.min_y)

        screens = QApplication.screens()

        if self.monitor_id < len(screens):
            screen_geometry = screens[self.monitor_id].geometry()
            screen_center = screen_geometry.center()

            # Center the window
            window_geometry = main_window.frameGeometry()
            window_geometry.moveCenter(screen_center)
            main_window.move(window_geometry.topLeft())
        else:
            print(f"Monitor ID {self.monitor_id} neexistuje.")
            return

        main_window.setWindowTitle("Ryu's Foo thing")
        main_window.setAttribute(Qt.WA_StyledBackground, True)
        main_window.setStyleSheet(f'background-color: {self.background_hex};')

        main_window.show()
        sys.exit(app.exec())


def run():
    window_instance = App_window()
    window_instance.root()
