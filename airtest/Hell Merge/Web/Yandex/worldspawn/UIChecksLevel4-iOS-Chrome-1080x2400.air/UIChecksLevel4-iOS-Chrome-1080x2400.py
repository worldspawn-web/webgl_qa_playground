# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Test starts on the first pop-up offer.
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7
# Device: iPhone XR

__author__ = "Michael 'Worldspawn' Lozickii"

from airtest.core.api import *
from utils import (
    interstitial_check,
    random_touch,
    quit_window
)

auto_setup(__file__)

def main():
    # Close Popup Offer
    if exists(Template(r"tpl1736958318809.png", record_pos=(-0.002, -0.025), resolution=(1080, 2400))):
        touch(Template(r"tpl1736958340836.png", record_pos=(0.436, -0.674), resolution=(1080, 2400)))
        sleep(1.0)

    # Sometimes a Shop could be opened on game start
    # quit_window()
    
    # UI Checks
    assert_exists(Template(r"tpl1736958356734.png", record_pos=(-0.002, -0.52), resolution=(1080, 2400)), "Current Location Panel.")
    sleep(1.0)
    assert_exists(Template(r"tpl1736958972213.png", record_pos=(-0.364, 0.442), resolution=(1080, 2400)), "New Location is Available to Open.")
    sleep(1.0)
    assert_exists(Template(r"tpl1736959001633.png", record_pos=(-0.429, -0.549), resolution=(1080, 2400)), "NoADS Offer Icon.")
    sleep(1.0)
    assert_exists(Template(r"tpl1736959017731.png", record_pos=(-0.092, -0.191), resolution=(1080, 2400)), "Completed Quest Icon.")
    sleep(1.0)
    assert_exists(Template(r"tpl1736959042212.png", record_pos=(-0.432, -0.686), resolution=(1080, 2400)), "Correct Level.")
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
        sleep(1.0)
        assert_exists(Template(r"tpl1736960039427.png", record_pos=(0.149, -0.188), resolution=(1080, 2400)), "Please fill in the test point.")
        touch(Template(r"tpl1736960052871.png", record_pos=(-0.143, -0.184), resolution=(1080, 2400)))
        sleep(1.0)
        touch(Template(r"tpl1736960057993.png", record_pos=(0.296, -0.35), resolution=(1080, 2400)))
        interstitial_check()
    else:
        assert_exists(Template(r"tpl1736959402954.png", record_pos=(0.239, -0.016), resolution=(1080, 2400)), "Russian Language Icon.")
        touch(Template(r"tpl1736959402954.png", record_pos=(0.238, -0.019), resolution=(1080, 2400)))
        sleep(1.0)
        assert_exists(Template(r"tpl1736960254062.png", record_pos=(-0.002, -0.051), resolution=(1080, 2400)), "Please fill in the test point.")
        assert_exists(Template(r"tpl1736960244233.png", record_pos=(0.151, -0.19), resolution=(1080, 2400)), "Please fill in the test point.")
        touch(Template(r"tpl1736960265512.png", record_pos=(-0.143, -0.184), resolution=(1080, 2400)))
        sleep(1.0)
        assert_exists(Template(r"tpl1736960274150.png", record_pos=(-0.143, -0.187), resolution=(1080, 2400)), "Please fill in the test point.")
        touch(Template(r"tpl1736960285216.png", record_pos=(0.148, -0.187), resolution=(1080, 2400)))
        sleep(1.0)
        touch(Template(r"tpl1736960057993.png", record_pos=(0.299, -0.349), resolution=(1080, 2400)))
        interstitial_check()

    touch(Template(r"tpl1736960580158.png", record_pos=(0.304, -0.356), resolution=(1080, 2400))) # quits settings menu *note for clearance*
    interstitial_check()

    # NoADs Offer
    assert_exists(Template(r"tpl1736959001633.png", record_pos=(-0.429, -0.549), resolution=(1080, 2400)), "NoAds Offer Icon.")
    touch(Template(r"tpl1736959001633.png", record_pos=(-0.425, -0.545), resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1736960781169.png", record_pos=(-0.002, -0.028), resolution=(1080, 2400)), "NoAds Offer.")
    assert_exists(Template(r"tpl1736960864932.png", record_pos=(0.0, 0.178), resolution=(1080, 2400)), "NoAds Icons.")
    assert_exists(Template(r"tpl1736960904008.png", record_pos=(0.002, 0.505), resolution=(1080, 2400)), "Purchase Button.")
    assert_exists(Template(r"tpl1736961036433.png", record_pos=(0.44, -0.673), resolution=(1080, 2400)), "Please fill in the test point.")
    touch(Template(r"tpl1736961036433.png", record_pos=(0.437, -0.678), resolution=(1080, 2400)))
    interstitial_check()
    
    # Shop Checker
    touch(Template(r"tpl1737035149615.png", record_pos=(-0.276, 0.591), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737035160514.png", record_pos=(-0.269, -0.547), resolution=(1080, 2400)), "Soft Value Icon.")
    assert_exists(Template(r"tpl1737035167584.png", record_pos=(0.15, -0.552), resolution=(1080, 2400)), "Hard Value Icon.")
    swipe((0.5, 0.5), (0.5, 0.1))
    sleep(5.0)
    assert_exists(Template(r"tpl1737035234160.png", record_pos=(-0.299, 0.347), resolution=(1080, 2400)), "'Day Specials' Decor (which means the container is rendered).")
    assert_exists(Template(r"tpl1737036156830.png", record_pos=(0.013, -0.267), resolution=(1080, 2400)), "Icons on 'Day Specials'")
    assert_exists(Template(r"tpl1737036166170.png", record_pos=(0.001, -0.13), resolution=(1080, 2400)), "'Day Specials' Prices.")
    assert_exists(Template(r"tpl1737036131630.png", record_pos=(0.006, 0.014), resolution=(1080, 2400)), "'On Sale' Container.")

    assert_exists(Template(r"tpl1737036185730.png", record_pos=(-0.241, 0.27), resolution=(1080, 2400)), "Random Sales Item Icon")
    swipe((0.5, 0.5), (0, -0.01))
    sleep(5.0)
    assert_exists(Template(r"tpl1737037116041.png", record_pos=(0.007, -0.294), resolution=(1080, 2400)), "Loot Boxes Header.")
    assert_exists(Template(r"tpl1737036298846.png", record_pos=(0.002, -0.166), resolution=(1080, 2400)), "Loot Boxes Icons.")
    assert_exists(Template(r"tpl1737036307669.png", record_pos=(0.004, 0.156), resolution=(1080, 2400)), "Boosters Header.")
    assert_exists(Template(r"tpl1737036314326.png", record_pos=(-0.231, 0.397), resolution=(1080, 2400)), "Summon Booster Icon.")
    assert_exists(Template(r"tpl1737036320289.png", record_pos=(-0.002, 0.394), resolution=(1080, 2400)), "Grow Booster Icon.")
    assert_exists(Template(r"tpl1737036325217.png", record_pos=(0.227, 0.385), resolution=(1080, 2400)), "Scissors Booster Icon.")
    swipe((0.5, 0.5), (0.5, 0.1))
    sleep(5.0)
    assert_exists(Template(r"tpl1737036561947.png", record_pos=(-0.001, -0.444), resolution=(1080, 2400)), "Crystals Header.")
    assert_exists(Template(r"tpl1737036574653.png", record_pos=(-0.001, -0.282), resolution=(1080, 2400)), "Crystals Hard Icons #1.")
    assert_exists(Template(r"tpl1737036581009.png", record_pos=(0.0, 0.08), resolution=(1080, 2400)), "Crystals Hard Icons #2.")
    assert_exists(Template(r"tpl1737036587307.png", record_pos=(0.006, 0.411), resolution=(1080, 2400)), "Soft Header.")
    swipe((0.5, 0.5), (0.5, 0.01))
    sleep(3.0)
    assert_exists(Template(r"tpl1737036670924.png", record_pos=(0.001, 0.065), resolution=(1080, 2400)), "Soft Icons #1")
    assert_exists(Template(r"tpl1737036678344.png", record_pos=(-0.003, 0.426), resolution=(1080, 2400)), "Soft Icons #2")
    sleep(1.0)
    assert_exists(Template(r"tpl1737036690530.png", record_pos=(0.427, -0.631), resolution=(1080, 2400)), "Quit Window Button.")
    touch(Template(r"tpl1737036690530.png", record_pos=(0.429, -0.634), resolution=(1080, 2400)))
    interstitial_check()
    assert_exists(Template(r"tpl1737036727773.png", record_pos=(-0.002, -0.02), resolution=(1080, 2400)), "Main Scene.")
    
    # Current Location Panel Action
    touch(Template(r"tpl1737039446656.png", record_pos=(0.007, -0.514), resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1737039458524.png", record_pos=(-0.003, -0.324), resolution=(1080, 2400)), "Current Location Extended Panel.")
    touch(Template(r"tpl1737039446656.png", record_pos=(0.007, -0.514), resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1736958356734.png", record_pos=(-0.002, -0.52), resolution=(1080, 2400)), "Minimized Location Panel.")
    
    # Player Info Window
    touch(Template(r"tpl1737039678341.png", record_pos=(-0.43, -0.687), resolution=(1080, 2400)))
    wait(Template(r"tpl1737039688050.png", record_pos=(-0.001, -0.092), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737039698690.png", record_pos=(-0.206, -0.269), resolution=(1080, 2400)), "Current Level Icon.")
    assert_exists(Template(r"tpl1737039704372.png", record_pos=(0.005, 0.269), resolution=(1080, 2400)), "Locked LevelUp Button.")
    assert_exists(Template(r"tpl1737039714601.png", record_pos=(0.004, 0.042), resolution=(1080, 2400)), "Awards for the Next Level.")
    touch(Template(r"tpl1737039720525.png", record_pos=(0.312, -0.457), resolution=(1080, 2400)))
    interstitial_check()

    
    # New Zone Unlock
    touch(Template(r"tpl1737039609327.png", record_pos=(-0.372, 0.451), resolution=(1080, 2400)))
    sleep(5.0)
    assert_exists(Template(r"tpl1737039646252.png", record_pos=(0.005, -0.028), resolution=(1080, 2400)), "New Quest Appeared.")


if __name__ == "__main__":
    main()
    
# Swipe Coordinate Helper:
# x - left/right
# y - up/down