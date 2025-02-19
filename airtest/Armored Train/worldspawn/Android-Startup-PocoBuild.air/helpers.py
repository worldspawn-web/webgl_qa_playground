from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import json

# JSON Config Usage
with open('config.json') as config_file:
    config = json.load(config_file)
    
poco = UnityPoco()

# Available log tags
log_tags = {
    "error": "- [ERROR]: ",
    "assert": "- [ASSERTION]: ",
    "cheats": "- [CHEATS]: "
}

# Raises an Exception if some element is not on the screen
def poco_exception(obj):
    print("\n---------- ERROR ----------\n")
    raise Exception(f"{log_tags['error']}Requested Element has not been found!\nElement ID: {obj}")

# Prints current assertions to console
def poco_logger(note):
    print(f"{log_tags['assert']}{note}...OK!")

# Checks if an element exists
def poco_exists(img, note=""):
    if img.exists():
        poco_logger(note)
    else:
        poco_exception(note)
    sleep(0.5)

# Checks if an element exists & touches/clicks it
# if using with Poco -> pocoInstance=True
# if using with Airtest Templates -> posoInstance=False
def assert_and_touch(img, note="", pocoInstance=False, delay=1.0):
    if pocoInstance:
        if img.exists():
            img.click()
            poco_logger(note)
        else:
            poco_exception(note)
        return
    
    if assert_exists(img, note):
        touch(img)
        sleep(delay)
        poco_logger(note)
    else:
        poco_exception(note)

# Middle screen touch (It's random in terms of game design)
def random_touch(delay=1.0):
    touch((0.5, 0.5))
    sleep(delay)

# Checks if multiple elements exists on the current screen
# You need to create an object before using
# Object Example:
# object = {
#     "img1": [poco(text="test"), "Test Image 1"],
#     "img2": [poco(texture="S_Image"), "Test Image 2"]    
# }
def multiple_checker(obj):
    for key, (el, note) in obj.items():
        poco_exists(el, note)

# Checks for crossmarks and touches them
# NOTE: We can't simply use Poco here since all the crossmarks have the same name,
#       the same texture, and text.
#       Because of that, we are currently using good old Airtest snapshot method.
def close_ui():
    btns = [
        Template(r"snapshots/tpl1739790881049.png", rgb=True, record_pos=(0.107, -0.079), resolution=(2400, 1080)),
        Template(r"snapshots/tpl1739818435141.png", rgb=True, target_pos=6, record_pos=(0.363, -0.2), resolution=(2400, 1080)),
        Template(r"snapshots/tpl1739818808573.png", rgb=True, target_pos=6, record_pos=(0.037, -0.078), resolution=(2400, 1080))
    ]
    
    for btn in btns:
        if exists(btn):
            touch(btn)
            sleep(1.0)
            poco_logger("Close Button")
            return True
    
    raise Exception(f"{log_tags['error']}Sorry, Boss, I haven't found any crossmark to touch.\nCheck your code, idk.\nZzz...")

# Checks a snapshot (exists), but also logs poco result
def snapshot_check(snap, note):
    if exists(snap):
        sleep(1.0)
        poco_logger(note)
        return True
    else:
        raise Exception(f"{log_tags['error']}Snapshot has not been found!\nSnapshot Name: {note}")

# Checks if two values are not the same
# NOTE: Useful for checking before/after values
def value_diff(x, y, note=""):
    x, y = str(x), str(y)
    if x != y:
        poco_logger(note)
        sleep(0.5)
    else:
        poco_exception(note)

# Checks if the current screwnuts value suits Balancy config
# Balancy config is a "value" param that originally comes from config.json
# Example:
#   -   screw_check(config['rewards']['level_2'])
def screw_check(value):
    if poco("Text (TMP)").get_text() == str(value):
        poco_logger(f"Screwnuts updated to {value}")
    else:
        poco_exception("Something is wrong with rewards system!")
