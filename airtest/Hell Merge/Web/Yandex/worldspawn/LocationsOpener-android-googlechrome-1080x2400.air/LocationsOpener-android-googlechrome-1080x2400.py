# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Test starts on the first pop-up offer.
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs (Turned Off)
# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

from airtest.core.api import *
from utils import (
    interstitial_check,
    random_touch,
    autowin_toggle
)

auto_setup(__file__)

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


# Enable Auto-Win Cheat
autowin_toggle()
