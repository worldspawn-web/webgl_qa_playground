# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
auto_setup(__file__)

# Functions
def random_touch():
    sleep(2.0)
    touch([300, 300])
    
# Checks for Interstitial
# Call after every window close on the main scene!
def interstitial_check():
    sleep(3.0)
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    else:
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))


# Close Popup Offer
wait(Template(r"tpl1736958318809.png", record_pos=(-0.002, -0.025), resolution=(1080, 2400)))
touch(Template(r"tpl1736958340836.png", record_pos=(0.436, -0.674), resolution=(1080, 2400)))
sleep(1.0)

# UI Checks
assert_exists(Template(r"tpl1736958356734.png", record_pos=(-0.002, -0.52), resolution=(1080, 2400)), "Current Location Panel.")
sleep(1.0)
assert_exists(Template(r"tpl1736958972213.png", record_pos=(-0.364, 0.442), resolution=(1080, 2400)), "New Location is Available to Open.")
sleep(1.0)
assert_exists(Template(r"tpl1736959001633.png", record_pos=(-0.429, -0.549), resolution=(1080, 2400)), "NoADS Offer Icon.")
sleep(1.0)
assert_exists(Template(r"tpl1736959017731.png", record_pos=(-0.092, -0.191), resolution=(1080, 2400)), "Completed Quest Icon.")
sleep(1.0)
assert_exists(Template(r"tpl1736959042212.png", record_pos=(-0.432, -0.686), resolution=(1080, 2400)), "Currect Level.")
sleep(1.0)
assert_exists(Template(r"tpl1736959065913.png", record_pos=(0.44, -0.684), resolution=(1080, 2400)), "Settings Button.")
sleep(1.0)
assert_exists(Template(r"tpl1736959082317.png", record_pos=(0.389, 0.581), resolution=(1080, 2400)), "Play (Merge) Button.")
sleep(1.0)
assert_exists(Template(r"tpl1736959110938.png", record_pos=(-0.409, 0.598), resolution=(1080, 2400)), "Available Quests Button.")
sleep(1.0)
assert_exists(Template(r"tpl1736959150143.png", record_pos=(-0.272, 0.588), resolution=(1080, 2400)), "Shop Icon.")
sleep(1.0)

# Settings Window
touch(Template(r"tpl1736959343843.png", record_pos=(0.439, -0.683), resolution=(1080, 2400)))
wait(Template(r"tpl1736959353467.png", record_pos=(0.002, -0.048), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736959386934.png", record_pos=(-0.26, -0.123), resolution=(1080, 2400)), "Settings Icons.")

if not exists(Template(r"tpl1736959402954.png", record_pos=(0.239, -0.016), resolution=(1080, 2400))):
    assert_exists(Template(r"tpl1736959516722.png", record_pos=(0.236, -0.022), resolution=(1080, 2400)), "English Language Icon.")
    touch(Template(r"tpl1736959516722.png", record_pos=(0.234, -0.016), resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1736959944935.png", record_pos=(-0.002, -0.056), resolution=(1080, 2400)), "Please fill in the test point.")
    assert_exists(Template(r"tpl1736960023923.png", record_pos=(-0.145, -0.187), resolution=(1080, 2400)), "Please fill in the test point.")
    touch(Template(r"tpl1736959956034.png", record_pos=(0.146, -0.184), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1736960039427.png", record_pos=(0.149, -0.188), resolution=(1080, 2400)), "Please fill in the test point.")
    touch(Template(r"tpl1736960052871.png", record_pos=(-0.143, -0.184), resolution=(1080, 2400)))
    touch(Template(r"tpl1736960057993.png", record_pos=(0.296, -0.35), resolution=(1080, 2400)))
else:
    assert_exists(Template(r"tpl1736959402954.png", record_pos=(0.239, -0.016), resolution=(1080, 2400)), "Russian Language Icon.")
    touch(Template(r"tpl1736959402954.png", record_pos=(0.238, -0.019), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1736960254062.png", record_pos=(-0.002, -0.051), resolution=(1080, 2400)), "Please fill in the test point.")
    assert_exists(Template(r"tpl1736960244233.png", record_pos=(0.151, -0.19), resolution=(1080, 2400)), "Please fill in the test point.")
    touch(Template(r"tpl1736960265512.png", record_pos=(-0.143, -0.184), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1736960274150.png", record_pos=(-0.143, -0.187), resolution=(1080, 2400)), "Please fill in the test point.")
    touch(Template(r"tpl1736960285216.png", record_pos=(0.148, -0.187), resolution=(1080, 2400)))
    touch(Template(r"tpl1736960057993.png", record_pos=(0.299, -0.349), resolution=(1080, 2400)))

touch(Template(r"tpl1736960580158.png", record_pos=(0.304, -0.356), resolution=(1080, 2400))) # quits settings menu *note for clearance*
interstitial_check()

# NoADs Offer
assert_exists(Template(r"tpl1736959001633.png", record_pos=(-0.429, -0.549), resolution=(1080, 2400)), "NoAds Offer Icon.")
sleep(1.0)
touch(Template(r"tpl1736959001633.png", record_pos=(-0.425, -0.545), resolution=(1080, 2400)))
sleep(3.0)
assert_exists(Template(r"tpl1736960781169.png", record_pos=(-0.002, -0.028), resolution=(1080, 2400)), "NoAds Offer.")
assert_exists(Template(r"tpl1736960864932.png", record_pos=(0.0, 0.178), resolution=(1080, 2400)), "NoAds Icons.")
assert_exists(Template(r"tpl1736960904008.png", record_pos=(0.002, 0.505), resolution=(1080, 2400)), "Purchase Button.")
assert_exists(Template(r"tpl1736961036433.png", record_pos=(0.44, -0.673), resolution=(1080, 2400)), "Please fill in the test point.")
touch(Template(r"tpl1736961036433.png", record_pos=(0.437, -0.678), resolution=(1080, 2400)))

