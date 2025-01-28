# -*- encoding=utf8 -*-
# ! IMPORT SAVEDATA BEFORE RUNNING !
#
# SAVE NAME:
# MagicSchool-5cpiqJtaJykrCWLQchIkO2GCRazUFl4foA5smdAJ-qU=
#

from airtest.core.api import *
import logging
from utils import (
    random_touch, 
    assert_and_touch,
    close_window,
    yandex_pay
)

auto_setup(__file__)

ST.SNAPSHOT_DIR = "./snapshots

#
# Minor Utility Functions
#

def open_settings():
    settings_btn = Template(r"tpl1738077103247.png", record_pos=(0.237, -0.102), resolution=(2400, 1080))
    settings_window = Template(r"tpl1738077151793.png", record_pos=(-0.078, 0.042), resolution=(2400, 1080))
    touch(settings_btn)
    wait(settings_window)
    
#
# Checks for a correct game & tests start
#

def startup():        
    startup_daily = Template(r"tpl1738070567065.png", record_pos=(-0.078, 0.056), resolution=(2400, 1080))
    if exists(startup_daily):
        random_touch()

    
    offer_noads = Template(r"tpl1738071251829.png", record_pos=(-0.086, 0.06), resolution=(2400, 1080))
    if exists(offer_noads):
        touch((0.7, 0.7))

    assert_exists(Template(r"tpl1738071315727.png", record_pos=(-0.076, 0.051), resolution=(2400, 1080)), "Game Loaded.")

#
# Checks CopyID
#

def copyid():
    # Values
    id_field = Template(r"tpl1738077228917.png", target_pos=6, record_pos=(-0.049, 0.007), resolution=(2400, 1080))
    name_field = Template(r"tpl1738077311428.png", record_pos=(-0.08, -0.02), resolution=(2400, 1080))
    
    # Actions
    open_settings()
    assert_and_touch(id_field, "User ID Field.")
    assert_and_touch(name_field, "Name Field.")
    paste()
    sleep(0.5)
    assert_exists(Template(r"tpl1738077610637.png", rgb=True, record_pos=(-0.052, -0.022), resolution=(2400, 1080)), "Value Pasted.")
    close_window()

#
# Checks Settings Togglers (w/o volume checks)
#

def togglers_checker():
    # Toggler Parameters
    togglers = [
        {
            "on": Template(r"tpl1738078173835.png", record_pos=(-0.122, 0.142), resolution=(2400, 1080)),
            "off": Template(r"tpl1738078209121.png", record_pos=(-0.122, 0.142), resolution=(2400, 1080)),
            "note": "VFX Toggle"
        },
        {
            "on": Template(r"tpl1738078222028.png", record_pos=(-0.077, 0.142), resolution=(2400, 1080)),
            "off": Template(r"tpl1738078233757.png", record_pos=(-0.078, 0.142), resolution=(2400, 1080)),
            "note": "Music toggle"
        },
        {
            "on": Template(r"tpl1738078247879.png", record_pos=(-0.031, 0.142), resolution=(2400, 1080)),
            "off": Template(r"tpl1738078260018.png", record_pos=(-0.032, 0.142), resolution=(2400, 1080)),
            "note": "Touch toggle"
        }
    ]

    # Actions
    open_settings()
    
    for toggle in togglers:
        assert_and_touch(toggle["on"], toggle["note"])
        sleep(1.0)
        assert_and_touch(toggle["off"], toggle["note"])
        sleep(1.0)

    close_window()
    
#
# IAP Checks
#
def iap_checks():
    # Hard Offers
    hard_offers = Template(r"tpl1738079311050.png", target_pos=6, record_pos=(0.168, -0.105), resolution=(2400, 1080))
    assert_and_touch(hard_offers, "Hard Offers Counter")
    wait(Template(r"tpl1738079364339.png", record_pos=(-0.073, 0.064), resolution=(2400, 1080)))
    assert_exists(Template(r"tpl1738079409162.png", record_pos=(-0.077, -0.082), resolution=(2400, 1080)), "Any offer disabled adverts.")
    
    yandex_pay(Template(r"tpl1738079516951.png", record_pos=(-0.071, 0.206), resolution=(2400, 1080))) 

    assert_exists(Template(r"tpl1738079946681.png", record_pos=(0.016, 0.029), resolution=(2400, 1080)), "Ads Disabled for N hours.")
    close_window()
    
    values_before = Template(r"tpl1738079576771.png", record_pos=(0.123, -0.103), resolution=(2400, 1080))
    values_after = Template(r"tpl1738079984594.png", record_pos=(0.312, -0.103), resolution=(2400, 1080))
    assert_not_equal(values_after, values_before, "Values Changed after Payment.")
    sleep(1.0)
    close_window()
    
    # Soft Offers
    soft_offers = Template(r"tpl1738080454859.png", target_pos=6, record_pos=(0.269, -0.105), resolution=(2400, 1080))
    noads_token_btn = Template(r"tpl1738080563321.png", record_pos=(-0.157, 0.132), resolution=(2400, 1080))
    
    assert_and_touch(soft_offers, "Soft Value Counter.")
    assert_exists(Template(r"tpl1738080516913.png", record_pos=(0.018, 0.037), resolution=(2400, 1080)), "Shop Window Appeared.")
    assert_exists(Template(r"tpl1738080531332.png", record_pos=(0.02, -0.062), resolution=(2400, 1080)), "Top Panel.")
    assert_exists(Template(r"tpl1738080548297.png", record_pos=(-0.158, 0.069), resolution=(2400, 1080)), "Free Soft Value.")
    assert_and_touch(noads_token_btn, "Get Reward for Ads Tokens Button.")
    
    assert_exists(Template(r"tpl1738080762942.png", record_pos=(0.051, 0.069), resolution=(2400, 1080)), "Other Offers.")
    swipe((0.72, 0.6),(0.3, 0.6))
    sleep(2.0)
    assert_exists(Template(r"tpl1738080813941.png", record_pos=(0.123, 0.068), resolution=(2400, 1080)), "Other Offers #2 + Swiper Works.")
    
    touch(Template(r"tpl1738080861476.png", record_pos=(0.195, 0.13), resolution=(2400, 1080)))
    assert_exists(Template(r"tpl1738080873340.png", record_pos=(0.016, 0.055), resolution=(2400, 1080)), "Confirm Payment Modal.")
    touch(Template(r"tpl1738080889792.png", record_pos=(0.018, 0.136), resolution=(2400, 1080)))
    close_window()
    assert_not_equal(Template(r"tpl1738080949543.png", record_pos=(0.313, -0.102), resolution=(2400, 1080)), values_after, "Values Changed after Purchase.")


#
# Main Entry Function
#
    
def main():
    startup()
    copyid()
    togglers_checker()
    iap_checks()
    
    
if __name__ == "__main__":
    main()
