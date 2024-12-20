from screeninfo import get_monitors
from src.BackEnd import json_utils as Json_utils


class get_info:
    def __init__(self):
        __Json_utils_local_instance = Json_utils.Actions()  # init local instance for json utils
        self.Json_utils_instance = __Json_utils_local_instance  # global json utils instance
        self.__screenID = __Json_utils_local_instance.read_config("FrontEnd_config", "App_def_screenId")
        self.__screen_width = None
        self.__screen_height = None

    def _window_resolution(self):
        self.__screen_width = get_monitors()[self.__screenID].width
        self.__screen_height = get_monitors()[self.__screenID].height

    def window_geometry(self):
        self._window_resolution()  # initialize screen res
        lengh_percantage, high_percantage = self.Json_utils_instance.read_config("FrontEnd_config", "App_window")

        division_x = lengh_percantage / 100
        division_y = high_percantage / 100

        # get X and Y res for application window
        window_x = int(self.__screen_width * division_x)
        window_y = int(self.__screen_height * division_y)

        # minimal possible window size
        min_x = int(self.__screen_height * 0.20)
        min_y = int(self.__screen_width * 0.20)

        x = (self.__screen_width - window_x) // 2
        y = (self.__screen_height - window_y) // 2
        # I am returning screen poss. for x and y as 0, because in frontend there is qt function that should center the
        # app better than my function (it was not counting with titlebar somehow)
        return x, y, window_x, window_y, min_y, min_x

    def rootWindow_info(self):
        background_color = self.Json_utils_instance.read_config("FrontEnd_config", "Background_color_hex")
        monitor_id = self.Json_utils_instance.read_config("FrontEnd_config", "App_def_screenId")
        return monitor_id, background_color

