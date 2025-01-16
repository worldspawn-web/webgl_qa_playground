# This file contains general utilities, whose could be used anywhere in Yandex projects.
#   Platform    =   Yandex

# Removes Debug Logs
# Note: In-line code run will ignore this rule.
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# Random Middle Touch (1080x2040)
# Usage: Use whenever "any" touch is required
def random_touch():
    sleep(2.0)
    touch([500, 1020])


# Checks for Interstitial
# Note: Insert your own images or copy from "worldspawn/PastTutorsChecker-android-googlechrome-1080x2400.air/...""
# Usage: Use right after every window close
def interstitial_check():
    sleep(1.0)
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    if exists(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))):
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))


# Cache Reset on Test Startup
# Note: Insert your own images or copy from "worldspawn/StartTutors-android-googlechrome-1080x2400.air/...""
# Usage: Use at the start of your empty profile tests.
class BrowserCacheVariation: ## First, create a class for different browser UI
    def __init__(self, image, record_pos, resolution):
        self.image = image
        self.record_pos = record_pos
        self.resolution = resolution
        
def init_browsers(): ## Define all your UI variations in this function
    browser1 = BrowserCacheVariation("tpl1736944115125.png", (0.297, -0.955), (1080, 2400)) # dark panel
    browser2 = BrowserCacheVariation("tpl1736945067386.png", (0.309, -0.954), (1080, 2400)) # white panel w/ no avatar
    browser3 = BrowserCacheVariation("tpl1736945298223.png", (0.18, -0.954), (1080, 2400)) # only settings (tab viewer)
    return [browser1, browser2, browser3]

browsers = init_browsers() ## Initialize the function inside the test

if not (exists(Template(r"tpl1736943901499.png", record_pos=(0.001, -0.693), resolution=(1080, 2400)))): ## Insert this as a part of the test
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