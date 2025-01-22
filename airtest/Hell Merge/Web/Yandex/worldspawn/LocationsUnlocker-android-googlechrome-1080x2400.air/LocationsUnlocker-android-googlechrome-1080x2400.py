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

# Variables
inter_templates = [
    Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)),
    Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)),
    Template(r"tpl1737548555454.png", record_pos=(-0.001, 0.913), resolution=(1080, 2400))
]

# Functions (will be moved to a separate file later)
def interstitial_check():
    sleep(2.0)
    
    for inter in inter_templates:
        if exists(inter):
            touch(inter)
            break

def complete_quest():
    complete_btn = Template(r"tpl1737378790269.png", record_pos=(0.0, 0.269), resolution=(1080, 2400))
    touch(complete_btn)
    sleep(1.0)

def autoquest():
    checkmarks = [
        Template(r"tpl1737544148891.png", rgb=True),
        Template(r"tpl1737553283307.png", rgb=True, record_pos=(0.0, -0.026)),
        Template(r"tpl1737548274741.png", threshold=0.7, rgb=True, record_pos=(0.001, -0.038))
    ]

    quests_completed = False
    
    while True:
        found_checkmark = None
        for checkmark in checkmarks:
            if exists(checkmark): # sometimes clicks on ad banner
                found_checkmark = checkmark
                break
        if not found_checkmark:
            break
    
        wait(found_checkmark)
        touch(found_checkmark)
        sleep(1.0)
        complete_quest()
        interstitial_check()
        quests_completed = True

    return quests_completed

def quest_finder():
    touch(Template(r"tpl1737544532460.png", record_pos=(-0.418, 0.599), resolution=(1080, 2400)))
    sleep(1.0)
    if exists(Template(r"tpl1737544571181.png", record_pos=(0.169, -0.307), resolution=(1080, 2400))):
        touch(Template(r"tpl1737544571181.png", record_pos=(0.169, -0.307), resolution=(1080, 2400)))
        interstitial_check()
        return True
    return False

def main():
    # Locations Opener
#     swipe((878, 1242), (219, 1344))
    while True:
        if autoquest():
            logger.info("Quests Completed successfully.")
        else:
            logger.info("Looking for new quests...")
            if quest_finder():
                logger.info("Found new quests! Returning to auto quest complete...")
            else:
                logger.info("No new quests found. Zzz...")
                break

    if not autoquest():
        try:
            quest_finder()
        except Exception as e:
            logger.error(f"No quests found.")
            

if __name__ == "__main__":
    main()


