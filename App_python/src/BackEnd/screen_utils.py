from screeninfo import get_monitors
from src.BackEnd import json_utils as Json_utils


class get_info:
    def __init__(self):
        self.screenID = 0  # placeholder for now
        self.screen_width = None
        self.screen_height = None
        self.Json_utils_instance = Json_utils.actions()

    def _window_resolution(self):
        self.screen_width = get_monitors()[self.screenID].width
        self.screen_height = get_monitors()[self.screenID].height

    def window_geometry(self):
        self._window_resolution()  # initialize screen res
        lengh_percantage, high_percantage = self.Json_utils_instance.read_config("FrontEnd_config", "App_window")

        division_x = lengh_percantage / 100
        division_y = high_percantage / 100

        # get X and Y res for application window
        window_x = int(self.screen_width * division_x)
        window_y = int(self.screen_height * division_y)

        # minimal possible window size
        min_x = int(self.screen_height * 0.20)
        min_y = int(self.screen_width * 0.20)

        # I am returning screen poss. for x and y as 0, because in frontend there is qt function that should center the
        # app better than my function (it was not counting with titlebar somehow)
        return 0, 0, window_x, window_y, min_y, min_x

    def rootWindow_info(self):
        background_color = self.Json_utils_instance.read_config("FrontEnd_config", "Background_color_hex")
        monitor_id = self.Json_utils_instance.read_config("FrontEnd_config", "App_def_screenId")
        return monitor_id, background_color

