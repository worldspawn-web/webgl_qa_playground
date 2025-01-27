from airtest.core.api import *

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