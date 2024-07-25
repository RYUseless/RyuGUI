# import json
import os


def _go_to_assets():
    working_dir = os.getcwd()
    wrk_one_up = os.path.abspath(os.path.join(working_dir, "../"))
    location_assets = os.path.join(wrk_one_up, "assets")
    loc_ass_boolean = os.path.exists(location_assets)

    if loc_ass_boolean:
        return True, location_assets
    else:
        return False, None


def find_json_folder():
    print("todo")
