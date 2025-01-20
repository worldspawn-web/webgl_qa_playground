# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Test starts on the first loaded scene (w/o offers)
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs (Turned Off)
# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

from airtest.core.api import *
auto_setup(__file__)

from utils import interstitial_check, autowin_toggle

    
def main():
    # Location Unlock through Button
    assert_exists(Template(r"tpl1737372642596.png", record_pos=(-0.369, 0.455), resolution=(1080, 2400)), "New Location Available Button.")
    touch(Template(r"tpl1737372642596.png", record_pos=(-0.374, 0.452), resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1737372765056.png", record_pos=(0.002, -0.031), resolution=(1080, 2400)), "New Quest Appeared.")

    assert_exists(Template(r"tpl1737372797304.png", record_pos=(-0.407, 0.175), resolution=(1080, 2400)), "New Completed Quest is Visible.")
    touch(Template(r"tpl1737372797304.png", record_pos=(-0.416, 0.186), resolution=(1080, 2400)))
    wait(Template(r"tpl1737372859053.png", record_pos=(-0.003, -0.08), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737372876995.png", record_pos=(-0.002, -0.119), resolution=(1080, 2400)), "Requested Item.")
    assert_exists(Template(r"tpl1737372885253.png", record_pos=(0.012, 0.073), resolution=(1080, 2400)), "Rewards.")
    touch(Template(r"tpl1737372866943.png", record_pos=(0.004, 0.272), resolution=(1080, 2400)))
    wait(Template(r"tpl1737372921982.png", record_pos=(-0.216, 0.4), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737372937860.png", record_pos=(-0.066, 0.35), resolution=(1080, 2400)), "Boss Mascot Appears.")
    assert_exists(Template(r"tpl1737372957532.png", record_pos=(0.348, -0.719), resolution=(1080, 2400)), "Skip Button & Volume Toggler.")
    touch(Template(r"tpl1737372962523.png", record_pos=(0.351, -0.725), resolution=(1080, 2400)))
    sleep(1.0)


    # Enable Auto-Win Cheat
    autowin_toggle()

    # Auto-Win Checker
    assert_exists(Template(r"tpl1737375153201.png", record_pos=(0.195, -0.192), resolution=(1080, 2400)), "Uncompleted Quest is Completed Now.")
    touch(Template(r"tpl1737375153201.png", record_pos=(0.194, -0.192), resolution=(1080, 2400)))
    sleep(1.0)
    wait(Template(r"tpl1737375189142.png", record_pos=(0.003, -0.089), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737375196856.png", record_pos=(0.004, -0.118), resolution=(1080, 2400)), "Requested Items.")
    assert_exists(Template(r"tpl1737375203483.png", record_pos=(0.004, 0.099), resolution=(1080, 2400)), "Reward.")
    assert_exists(Template(r"tpl1737375222086.png", record_pos=(-0.005, 0.272), resolution=(1080, 2400)), "Complete Button.")
    touch(Template(r"tpl1737375222086.png", record_pos=(0.001, 0.27), resolution=(1080, 2400)))

    # Wait for Cutscene
    sleep(10)

    # New Level
    assert_exists(Template(r"tpl1737375340393.png", record_pos=(-0.426, -0.68), resolution=(1080, 2400)), "New Level Icon.")
    touch(Template(r"tpl1737375340393.png", record_pos=(-0.426, -0.68), resolution=(1080, 2400)))
    wait(Template(r"tpl1737375409268.png", record_pos=(-0.002, -0.095), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737375416695.png", record_pos=(-0.206, -0.244), resolution=(1080, 2400)), "Completed Level Icon.")
    assert_exists(Template(r"tpl1737375425024.png", record_pos=(0.005, 0.093), resolution=(1080, 2400)), "Incoming Rewards.")
    assert_exists(Template(r"tpl1737375429205.png", rgb=True, record_pos=(-0.002, 0.275), resolution=(1080, 2400)), "Available LVLUP Button.") # rgb parameter MUST be True
    touch(Template(r"tpl1737375429205.png", rgb=True, record_pos=(-0.002, 0.275), resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1737375524410.png", rgb=True, record_pos=(-0.206, -0.238), resolution=(1080, 2400)), "Updated Level.")
    assert_exists(Template(r"tpl1737375540195.png", rgb=True, record_pos=(-0.002, 0.272), resolution=(1080, 2400)), "Button is Locked Now.")
    touch(Template(r"tpl1737375587281.png", record_pos=(0.31, -0.458), resolution=(1080, 2400)))
    interstitial_check()

if __name__ == "__main__":
    main()
