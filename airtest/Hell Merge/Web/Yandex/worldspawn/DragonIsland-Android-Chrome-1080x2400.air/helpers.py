from airtest.core.api import *
import logging

# Logger Setup
logger = logging.getLogger("airtest")

# Functions
def random_touch():
    sleep(2.0)
    touch([500, 1020])
    

# Functions (will be moved to a separate file later)
def interstitial_check():
    inter_templates = [
        Template(r"tpl1736872848834.png", rgb=True, record_pos=(0.42, -0.967), resolution=(1080, 2400)),
        Template(r"tpl1736852577544.png", rgb=True, record_pos=(0.427, -0.967), resolution=(1080, 2400)),
        Template(r"tpl1737548555454.png", rgb=True, record_pos=(-0.001, 0.913), resolution=(1080, 2400))
    ]

    sleep(2.0)
    
    for inter in inter_templates:
        if exists(inter):
            touch(inter)
            break

def quit_window():
    logger.info("Looking for a window to close...")
    cross_templates = [
        Template(r"tpl1737375587281.png", record_pos=(0.31, -0.458), resolution=(1080, 2400)),
        Template(r"tpl1737381782191.png", record_pos=(0.306, -0.533), resolution=(1080, 2400)),
        Template(r"tpl1737382243343.png", record_pos=(0.304, -0.436), resolution=(1080, 2400)),
        Template(r"tpl1737389486120.png", record_pos=(0.322, -0.673), resolution=(1080, 2400))
    ]

    for _ in range(10):
        for cross in cross_templates:
            if exists(cross):
                touch(cross)
                interstitial_check()
                return

    raise Exception("Failed to find and close window")
               
def autowin_toggle():
    # Enable Auto-Win Cheat
    touch((76, 454))
    
    if not exists(Template(r"tpl1737543351937.png", record_pos=(-0.294, -0.45), resolution=(1080, 2400))):
        ## Cheat Opener Combination
        for i in range(3):
            swipe((318, 863), (318, 953))
            sleep(1.0)
        for i in range(2):
            swipe((358, 908), (276, 908))
            sleep(1.0)
        for i in range(2):
            swipe((276, 908), (358, 908))
            sleep(1.0)
    else:
        touch(Template(r"tpl1737543351937.png", record_pos=(-0.294, -0.45), resolution=(1080, 2400)))

    wait(Template(r"tpl1737374734015.png", record_pos=(0.005, -0.061), resolution=(1080, 2400)))
    touch(Template(r"tpl1737374741818.png", rgb=True, record_pos=(-0.097, -0.422), resolution=(1080, 2400)))
    sleep(1.0)
    touch((843, 1492)) # toggler
    sleep(1.0)
    for i in range(2):
        quit_window()
    
def quest_finder():
    touch(Template(r"tpl1737544532460.png", record_pos=(-0.418, 0.599), resolution=(1080, 2400)))
    sleep(1.0)
    if exists(Template(r"tpl1737544571181.png", record_pos=(0.169, -0.307), resolution=(1080, 2400))):
        touch(Template(r"tpl1737544571181.png", record_pos=(0.169, -0.307), resolution=(1080, 2400)))
        interstitial_check()
        return True
    return False

__all__ = ['random_touch', 'autowin_toggle', 'interstitial_check', 'quit_window', 'quest_finder']
