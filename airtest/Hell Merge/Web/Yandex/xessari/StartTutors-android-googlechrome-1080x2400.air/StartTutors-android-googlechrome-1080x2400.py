# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Start Test Window: Empty Google Page
# Mode: Incognito (No Yandex Profile)
# Version: 1.1.7

__author__ = "Andrew 'Xessaki' Ivanov"

# Removes Debug Logs
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
auto_setup(__file__)

# Functions
def random_touch():
    sleep(2.0)
    touch([500, 1020])

# Cache Reset Variations Class
class BrowserCacheVariation:
    def __init__(self, image, record_pos, resolution):
        self.image = image
        self.record_pos = record_pos
        self.resolution = resolution
        
# Cache Resets Variations Define
def init_browsers():
    browser1 = BrowserCacheVariation("tpl1736944115125.png", (0.297, -0.955), (1080, 2400)) # dark panel
    browser2 = BrowserCacheVariation("tpl1736945067386.png", (0.309, -0.954), (1080, 2400)) # white panel w/ no avatar
    browser3 = BrowserCacheVariation("tpl1736945298223.png", (0.18, -0.954), (1080, 2400)) # only settings (tab viewer)
    return [browser1, browser2, browser3]

def main():
    # Auto Cache Reset
    browsers = init_browsers()
    start_app("com.android.chrome")

    if not (exists(Template(r"tpl1736943901499.png", record_pos=(0.001, -0.693), resolution=(1080, 2400)))):
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
    sleep(3.0)
    touch(Template(r"tpl1736872552631.png", record_pos=(-0.167, -0.585), resolution=(1080, 2400)))
    text("https://yandex.ru/games/app/359515?lang=ru")
    keyevent("ENTER")

    sleep(3.0)
    if (exists(Template(r"tpl1736872631342.png", record_pos=(-0.004, 0.378), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872665536.png", record_pos=(0.001, 0.47), resolution=(1080, 2400)))

    # Close Entry Interstitial
    sleep(5.0)
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    else:
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))

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

    # Merge Tutorial Items
    sleep(3.0)
    swipe(Template(r"tpl1736866208284.png", record_pos=(-0.001, 0.047), resolution=(1080, 2400)), vector=[0.1515, 0.002])
    sleep(1.0)
    assert_exists(Template(r"tpl1736866406138.png", record_pos=(0.004, 0.05), resolution=(1080, 2400)), "Updated Merge Row.")
    swipe(Template(r"tpl1736874264407.png", record_pos=(-0.126, 0.043), resolution=(1080, 2400)), vector=[0.2452, 0.0052])

    sleep(1.0)
    assert_exists(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.043), resolution=(1080, 2400)), "Selected New Item.")
    swipe(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.045), resolution=(1080, 2400)), vector=[0.0041, 0.0593])
    assert_exists(Template(r"tpl1736866754994.png", record_pos=(0.116, 0.163), resolution=(1080, 2400)), "Tutorial Generator Appeared.")

    # Multiple Generator Taps
    for i in range(2):
        touch(Template(r"tpl1736866754994.png"))
        sleep(1.0)
    
    # Tutorial Volume Toggler
    assert_exists(Template(r"tpl1736869088108.png", record_pos=(0.202, -0.858), resolution=(1080, 2400)), "Volume toggler.")

    # Next Tutorials have random item drops, which makes autotests way too complex to handle
    # We can create multiple if/else or switch cases for handling randomness, but It will not test any new mechanic.

if __name__ == "__main__":
    main()
