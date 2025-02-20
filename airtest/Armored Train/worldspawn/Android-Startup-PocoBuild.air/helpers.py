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
    "cheats": "- [CHEATS]: ",
    "touch": "- [TOUCH]: ",
    "swipe": "- [SWIPE]: ",
    "snapshot": "- [SNAPSHOT]: ",
    "warn": "- [WARNING]: "
}

def head_log(msg):
    strings = "----------"
    sleep(3.0)
    print(f"\n{strings} {msg.upper()} {strings}\n")

# Raises an Exception if some element is not on the screen
def poco_exception(obj):
    head_log("ERROR")
    raise Exception(f"{log_tags['error']}Requested Element has not been found!\nElement ID: {obj}")

# Prints current assertions to console
def poco_logger(note, type = "assert"):
    print(f"{log_tags[type]}{note}...OK!")

# Checks if an element exists
def poco_exists(img, note=""):
    if img.exists():
        poco_logger(note)
        return True
    else:
        poco_exception(note)
    
def poco_swipe(pos1, pos2, duration=0.8):
    poco.swipe(pos1, pos2)
    poco_logger(f"pos_1: {pos1}, pos_2: {pos2}, Duration: {duration}", "swipe")

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
    x, y = 0.5, 0.5
    touch((x, y))
    poco_logger(f"XY: ({x}, {y})", "touch")
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
        poco_logger(note, "snapshot")
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

def touch_proxy(n=1, delay=3.0):
    for _ in range(n):
        click_pos = poco("Cutscene").offspring("ProxyButton") # we need to define it again each time to work (unity tree updates)
        click_pos.click()
        sleep(delay)
    return True

def isRZD_Banner():
    rzd_banner = poco("Banner Image")
    rzd_banner_cross = rzd_banner.child("Close Button")
    rzd_warn = "RZD Banner status - Active!"
    rzd_note = "Waiting for RZD timer..."
    rzd_success = "Successfully closed RZD Banner"
    
    if rzd_banner.exists():
        poco_logger(rzd_warn, "warn")
        poco_logger(rzd_note)
        sleep(15.0)
        rzd_banner_cross.click()
        sleep(1.5)
        
        if not rzd_banner.exists():
            poco_logger(rzd_success)
            return True
        else:
            poco_exception("Can't Close RZD Banner!")
    else:
        return False