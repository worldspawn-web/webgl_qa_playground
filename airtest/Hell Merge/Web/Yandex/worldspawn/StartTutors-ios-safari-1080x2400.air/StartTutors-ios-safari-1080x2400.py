# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Start Test Window: Empty Chrome
# Mode: Incognito (No Yandex Profile)
# Version: 1.1.7
# Device: iPhone XR (17.6.1)

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
from utils import (
    random_touch,
    init_browsers
)

auto_setup(__file__)

def fullscreen_window_check():
    window = Template(r"tpl1737976810731.png", target_pos=3, record_pos=(-0.005, -0.684), resolution=(828, 1792))
    if exists(window):
        touch(window)
        
def inter_check():
    templates = [
        Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)),
        Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))
    ]
    
    sleep(3.0)
    
    for inter in templates:
        if exists(inter):
            touch(inter)
            break

def main():
    # Auto Cache Reset
    browsers = init_browsers()

    if not (exists(Template(r"tpl1737975235780.png", record_pos=(-0.006, -0.634), resolution=(828, 1792)))):
        for browser in browsers:
            if exists(Template(r"" + browser.image, record_pos=browser.record_pos, resolution=browser.resolution)):
                touch(Template(r"" + browser.image, record_pos=browser.record_pos, resolution=browser.resolution, target_pos=6))
                break

        touch(Template(r"tpl1736945440708.png", record_pos=(0.119, -0.432), resolution=(1080, 2400)))
        sleep(1.0)
        wait(Template(r"tpl1736945481294.png", record_pos=(0.28, 0.566), resolution=(1080, 2400)))
        touch(Template(r"tpl1736945481294.png", record_pos=(0.28, 0.566), resolution=(1080, 2400)))
        sleep(3.0)
        touch(Template(r"tpl1736945586374.png", record_pos=(-0.187, -0.956), resolution=(1080, 2400), target_pos=4))

    # Hell Merge - Yandex (RU)
    touch(Template(r"tpl1737975235780.png", record_pos=(-0.006, -0.634), resolution=(828, 1792)))
    sleep(2.0)
    text("https://yandex.ru/games/app/359515?lang=ru")

    sleep(3.0)
    if (exists(Template(r"tpl1736872631342.png", record_pos=(-0.004, 0.378), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872665536.png", record_pos=(0.001, 0.47), resolution=(1080, 2400)))

    # Close Entry Interstitial
    sleep(3.0)
    inter_check()

    # Loading Screen Banner
    sleep(2.0)
    wait(Template(r"tpl1736852660900.png", record_pos=(0.032, -0.508), resolution=(1080, 2400)))

    # First Tutorial Window
    sleep(14.0)
    wait(Template(r"tpl1736852766557.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1736852766557.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)), "First Tutorial Window.")

    # Skip Dialogs
    for i in range(2):
        touch(Template(r"tpl1736858679598.png", record_pos=(0.324, -0.858), resolution=(1080, 2400)))
        sleep(8.0)

    # Touch before Tutorial Pointer
    wait(Template(r"tpl1736858768883.png", record_pos=(-0.005, -0.041), resolution=(1080, 2400)))
    sleep(2.0)
    random_touch()

    # Tutorial Pointer
    sleep(4.0)
    assert_exists(Template(r"tpl1736858804654.png", record_pos=(0.369, 0.688), resolution=(1080, 2400)), "Tutorial Finger")
    touch(Template(r"tpl1736858804654.png", record_pos=(0.369, 0.688), resolution=(1080, 2400)))

    # Merge Field Exists
    sleep(5.0)
    assert_exists(Template(r"tpl1736858868805.png", record_pos=(0.001, 0.051), resolution=(1080, 2400)), "Merge Field")
    assert_exists(Template(r"tpl1737308873014.png", record_pos=(-0.308, -0.656), resolution=(1080, 2400)), "Succubus Avatar.")
    
    # Merge Tutorial Items
    sleep(3.0)
    wait(Template(r"tpl1737975679506.png", record_pos=(0.005, -0.537), resolution=(828, 1792)))
    
    swipe_mid_h = 0.505
    swipe((0.498, swipe_mid_h),(0.6, swipe_mid_h))
    sleep(2.0)
    swipe((0.413, swipe_mid_h),(0.6, swipe_mid_h))
    sleep(2.0)
    
    assert_exists(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.043), resolution=(1080, 2400)), "Selected New Item.")
    swipe(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.045), resolution=(1080, 2400)), vector=[0.0041, 0.0593])

    # Multiple Generator Taps
    for i in range(3):
        touch((0.595, 0.551))
        sleep(2.0)

    # Checks for a Yandex Fullscreen Suggestion
    fullscreen_window_check()
    
    # Tutorial Volume Toggler
    assert_exists(Template(r"tpl1736869088108.png", record_pos=(0.202, -0.858), resolution=(1080, 2400)), "Volume toggler.")

    # Next Tutorials have random item drops, which makes autotests way too complex to handle
    # We can create multiple if/else or switch cases for handling randomness, but It will not test any new mechanic.

if __name__ == "__main__":
    main()
