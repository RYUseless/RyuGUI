import json
import os
import sys

__json_config_name = "config.json"


class actions:
    def __init__(self):
        self.json_config_name = "config.json"
        self.assets_location = None

    @staticmethod
    def find_json_folder():
        working_dir = os.getcwd()
        current_dir_name = os.path.basename(os.path.abspath(working_dir))

        # finding directory one bellow assets folder.
        print(f"OS namae {sys.platform}")
        while current_dir_name != "App_python" and working_dir != "/":
            working_dir = os.path.abspath(os.path.join(working_dir, "../"))
            current_dir_name = os.path.basename(os.path.abspath(working_dir))

        location_assets = os.path.join(working_dir, "assets")
        loc_ass_boolean = os.path.exists(location_assets)

        if loc_ass_boolean is False:
            print("There is no valid path, for now exiting")
            # TODO: try to create assets folder once again, if path itself is corrupted, idk, delete whole OS.
            exit(1)
        else:
            return location_assets

    def find_json_config(self):
        if self.assets_location is None:
            self.assets_location = self.find_json_folder()
        else:
            pass

        full_path = os.path.join(self.assets_location, self.json_config_name)
        path_verify = os.path.exists(full_path)
        if path_verify is False:
            print("No config file was found, generating default config now...")
            self.write_default_json(self.assets_location)
            return full_path
        else:
            return full_path

    def read_config(self, key, value):
        path = self.find_json_config()  # maybe optimize this?  potential power inefficiency
        with open(path, "r") as file:
            jsonData = json.load(file)
        return jsonData[key][value]

    def write_default_json(self, path):
        # percentage out of whole screen for app dimensions:
        # first is percentage for X_axis, then for Y_axis
        window_percentage = [80, 60]
        dictionary = {
            'database_config': {
                "Port": 6969,
                "url": "tvojeMamka.com"
            },
            'FrontEnd_config': {
                "App_window": window_percentage.copy(),
                "App_def_screenId": 0,
                "Background_color_hex": "#9f9f9f",

            },

        }
        json_object = json.dumps(dictionary, indent=4)
        with open(os.path.join(path, self.json_config_name), "w+", encoding='utf-8') as outfile:
            outfile.write(json_object)
