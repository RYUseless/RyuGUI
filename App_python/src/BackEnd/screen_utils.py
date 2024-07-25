from screeninfo import get_monitors


class get_info:
    def __init__(self):
        self.screenID = 0  # placeholder for now
        self.screen_width = None
        self.screen_height = None

    def _window_resolution(self):
        self.screen_width = get_monitors()[self.screenID].width
        self.screen_height = get_monitors()[self.screenID].height

    def window_geometry(self, lengh_percantage, high_percantage):
        self._window_resolution()  # initialize screen res

        division_x = lengh_percantage / 100
        division_y = high_percantage / 100

        # get X and Y res for application window
        window_x = int(self.screen_width * division_x)
        window_y = int(self.screen_height * division_y)

        # I am returning screen poss. for x and y as 0, because in frontend there is qt function that should center the
        # app better than my function (it was not counting with titlebar somehow)
        return 0, 0, window_x, window_y
