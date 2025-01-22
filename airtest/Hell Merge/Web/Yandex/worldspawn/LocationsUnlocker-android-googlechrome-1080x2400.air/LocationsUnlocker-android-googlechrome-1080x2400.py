# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Test starts right after Events-android-googlechrome-1080x2400.air (no offers must be opened)
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs (Turned Off):
#
# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

# IMPORTS
import logging
from airtest.core.api import *

# Logger Setup
logger = logging.getLogger("airtest")

# Airtest Setup
auto_setup(__file__)
logger.info("Setting up Airtest Game Environment")

# Functions (will be moved to a separate file later)
def interstitial_check():
    sleep(3.0)
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    if exists(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))):
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))

def complete_quest():
    complete_btn = Template(r"tpl1737378790269.png", record_pos=(0.0, 0.269), resolution=(1080, 2400))
    assert_exists(complete_btn, "Complete Button.")
    touch(complete_btn)
    sleep(1.0)

def autoquest():
    checkmark = Template(r"tpl1737544148891.png", record_pos=(-0.143, -0.045))
    
    while exists(checkmark):
        touch(checkmark)
        assert_exists(Template(r"tpl1737378790269.png", record_pos=(0.0, 0.269), resolution=(1080, 2400)), "Complete Button.")
        complete_quest()
        interstitial_check()

    return False

def quest_finder():
    touch(Template(r"tpl1737544532460.png", record_pos=(-0.418, 0.599), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1737544571181.png", record_pos=(0.169, -0.307), resolution=(1080, 2400)))
    sleep(4.0)

def main():
    # Locations Opener
    swipe((878, 1242), (219, 1344))
    if not autoquest():
        try:
            quest_finder()
        except Exception as e:
            logger.error(f"No quests found.")
            
    
    
if __name__ == "__main__":
    main()


