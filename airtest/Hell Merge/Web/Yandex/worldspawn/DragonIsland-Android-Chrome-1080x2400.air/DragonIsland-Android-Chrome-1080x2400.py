# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Test starts on Dragon Island Tutorial Start
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs (Turned Off):
# logger.setLevel(logging.ERROR)

# IMPORTS
import logging
from airtest.core.api import *
from helpers import random_touch, autowin_toggle, interstitial_check, quit_window

# Logger Setup
logger = logging.getLogger("airtest")

# Airtest Setup
auto_setup(__file__)
logger.info("Setting up Airtest Game Environment")

def tap_menu(menu):
    menu_height = 0.763
    menu_endpoints = {
        'quests': 0.2,
        'inventory': 0.34,
        'shop': 0.66,
        'switch': 0.8
    }
    
    if menu not in menu_endpoints:
        raise ValueError(f"Invalid menu option: {menu}")
    
    endpoint = menu_endpoints[menu]
    touch((endpoint, menu_height))
    sleep(1.0)


def main():
    dragon_complete_btn = Template(r"tpl1737556794407.png", record_pos=(0.171, 0.156), resolution=(1080, 2400))
    
    wait(Template(r"tpl1737554974809.png", threshold=0.6, record_pos=(-0.001, -0.028), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737554997331.png", record_pos=(0.382, -0.723), resolution=(1080, 2400)), "Skip Button.")
    random_touch()
    sleep(8.0)
    wait(Template(r"tpl1737555163307.png", record_pos=(-0.006, -0.548), resolution=(1080, 2400)))
    
    for i in range(2):
        random_touch()
    
    dragon_q_tutor = Template(r"tpl1737555225104.png", record_pos=(-0.414, 0.597), resolution=(1080, 2400))
    wait(dragon_q_tutor) # can be done with absolutes
    touch(dragon_q_tutor)
    wait(Template(r"tpl1737555346064.png", record_pos=(-0.002, -0.537), resolution=(1080, 2400)))
    random_touch()
    
    wait(Template(r"tpl1737555474787.png", record_pos=(0.001, -0.544), resolution=(1080, 2400)))
    
    dragon_q_tutor3 = (Template(r"tpl1737559751439.png", record_pos=(0.167, 0.156), resolution=(1080, 2400)))
    wait(dragon_q_tutor3)
    touch(dragon_q_tutor3)

    wait(Template(r"tpl1737560113313.png", record_pos=(-0.001, 0.047), resolution=(1080, 2400)))
    random_touch()
    sleep(1.0)
    tap_menu('quests')
    touch(dragon_complete_btn)
    random_touch()
    
    # Dragon Island Event Assertions
    assert_exists(Template(r"tpl1737555553031.png", record_pos=(-0.009, -0.56), resolution=(1080, 2400)), "Dragon Island Header.")
    assert_exists(Template(r"tpl1737555559554.png", record_pos=(-0.175, -0.409), resolution=(1080, 2400)), "Dragon Island Cover.")
    assert_exists(Template(r"tpl1737555565677.png", record_pos=(-0.103, -0.284), resolution=(1080, 2400)), "Dragon Island Progress.")
    assert_exists(Template(r"tpl1737555571559.png", rgb=True, record_pos=(0.156, -0.459), resolution=(1080, 2400)), "Dragon Island Timer.")
    assert_exists(Template(r"tpl1737555583843.png", record_pos=(-0.173, -0.154), resolution=(1080, 2400)), "Dragon Island Golden Ticket.")
    assert_exists(Template(r"tpl1737555588827.png", record_pos=(0.177, -0.148), resolution=(1080, 2400)), "Dragon Island Standart Ticket.")
    assert_exists(Template(r"tpl1737555594952.png", record_pos=(-0.19, 0.002), resolution=(1080, 2400)), "Dragon Island Locked Rewards.")
    assert_exists(Template(r"tpl1737555602084.png", record_pos=(-0.197, 0.379), resolution=(1080, 2400)), "Dragon Island Locked Rewards #2 & #3.")
    assert_exists(Template(r"tpl1737555607971.png", record_pos=(0.212, 0.498), resolution=(1080, 2400)), "Dragon Island Locked Standart Reward.")

    dragon_q_tutor4 = (Template(r"tpl1737555648771.png", rgb=True, target_pos=8, record_pos=(0.198, 0.049), resolution=(1080, 2400)))
    wait(dragon_q_tutor4)
    touch(dragon_q_tutor4)

    sleep(3.0)

    assert_not_equal(dragon_q_tutor4, Template(r"tpl1737555808709.png", record_pos=(0.201, 0.007), resolution=(1080, 2400)), "Dragon Award Claimed.")

    # Dragon Island Play
    dragon_play_btn = Template(r"tpl1737556010104.png", record_pos=(0.221, -0.289), resolution=(1080, 2400))
    exists(dragon_play_btn)
    touch(dragon_play_btn)
    sleep(1.0)
    touch(Template(r"tpl1737556062498.png", record_pos=(0.297, 0.602), resolution=(1080, 2400)))
    # interstitial_check() - uncom if inter appears
    wait(Template(r"tpl1737556091461.png", record_pos=(-0.002, -0.518), resolution=(1080, 2400)))
    
    for i in range(2):
        random_touch()
        
    dragon_park_tutor = Template(r"tpl1737556142912.png", record_pos=(-0.007, -0.035), resolution=(1080, 2400))
    wait(dragon_park_tutor)
    touch(dragon_park_tutor) # can fail the test idk why
    sleep(2.0)
    assert_exists(Template(r"tpl1737556186737.png", record_pos=(0.001, -0.035), resolution=(1080, 2400)), "Hover Effect.")
    assert_exists(Template(r"tpl1737556203136.png", record_pos=(0.006, -0.544), resolution=(1080, 2400)), "Mascot Dialog.")
    assert_exists(Template(r"tpl1737556222873.png", record_pos=(-0.004, 0.426), resolution=(1080, 2400)), "Decor Type Progress.")
    assert_exists(Template(r"tpl1737556242027.png", record_pos=(-0.278, 0.544), resolution=(1080, 2400)), "Remove Decoration Button.")
    
    dragon_park_tutor2 = Template(r"tpl1737556265101.png", record_pos=(-0.097, 0.548), resolution=(1080, 2400))
    wait(dragon_park_tutor2)
    touch(dragon_park_tutor2)
    assert_exists(Template(r"tpl1737556315445.png", record_pos=(0.008, -0.547), resolution=(1080, 2400)), "Updated Mascot Dialog.")
    assert_exists(Template(r"tpl1737556328922.png", record_pos=(0.003, -0.069), resolution=(1080, 2400)), "New Decor with Hover Effect.")
    
    dragon_park_tutor3 = Template(r"tpl1737556354829.png", record_pos=(0.225, 0.567), resolution=(1080, 2400))
    wait(dragon_park_tutor3)
    touch(dragon_park_tutor3)
    sleep(4.0)
    
    dragon_park_tutor4 = Template(r"tpl1737556417301.png", target_pos=8, record_pos=(-0.006, -0.515), resolution=(1080, 2400))
    wait(dragon_park_tutor4)
    touch(dragon_park_tutor4)
    wait(Template(r"tpl1737556509493.png", record_pos=(-0.005, -0.216), resolution=(1080, 2400)))
    random_touch()
    
    if exists(Template(r"tpl1737561761717.png", record_pos=(0.008, -0.136), resolution=(1080, 2400))):
        touch(Template(r"tpl1737561769602.png", record_pos=(0.0, 0.433), resolution=(1080, 2400)))
        sleep(3.0)
        touch(Template(r"tpl1737561782308.png", record_pos=(0.003, 0.584), resolution=(1080, 2400)))
        sleep(1.0)
        interstitial_check()
        touch(Template(r"tpl1737561813708.png", record_pos=(0.309, -0.706), resolution=(1080, 2400)))
        sleep(5.0)

    autowin_toggle()
    touch(Template(r"tpl1737556763278.png", record_pos=(-0.412, 0.591), resolution=(1080, 2400)))
    

    dragon_complete_toggle = True
    
    while dragon_complete_toggle:
        touch(dragon_complete_btn)
        sleep(2.0)

        if not exists(Template(r"tpl1737562066415.png", record_pos=(-0.004, -0.562), resolution=(1080, 2400))):
            dragon_complete_toggle = False
            break
    
    touch(Template(r"tpl1737557106045.png", target_pos=8, record_pos=(0.194, 0.097), resolution=(1080, 2400)))
    
    for i in range(2):
        quit_window()
    
    
    # Decor Installation
    # ...


if __name__ == "__main__":
    main()
