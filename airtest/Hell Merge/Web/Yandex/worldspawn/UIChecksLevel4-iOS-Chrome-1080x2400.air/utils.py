# -*- encoding=utf8 -*-
from airtest.core.api import *
import logging

# Logger Setup
logger = logging.getLogger("airtest")

auto_setup(__file__, logdir=None, devices=["ios:///http://127.0.0.1:8100",])

# Functions
def random_touch():
    sleep(2.0)
    touch([500, 1020])
    
# Checks for Interstitial
# Call after every window close on the main scene!
def interstitial_check():
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    if exists(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))):
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))
# TODO: think about the way to capture this rare inter ad with white button
#     if exists(Template(r"tpl1737988644552.png", rgb=True, record_pos=(-0.004, 0.82), resolution=(828, 1792))):
#         touch(Template(r"tpl1737988644552.png", rgb=True, record_pos=(-0.004, 0.82), resolution=(828, 1792)))
        
def quit_window():
    logger.info("Looking for a window to close...")
    cross_templates = [
        Template(r"tpl1737375587281.png", record_pos=(0.31, -0.458), resolution=(1080, 2400)),
        Template(r"tpl1737381782191.png", record_pos=(0.306, -0.533), resolution=(1080, 2400)),
        Template(r"tpl1737382243343.png", record_pos=(0.304, -0.436), resolution=(1080, 2400)),
        Template(r"tpl1737389486120.png", record_pos=(0.322, -0.673), resolution=(1080, 2400)),
        Template(r"tpl1737988266220.png", record_pos=(0.44, -0.65), resolution=(828, 1792))
    ]

    for _ in range(2):
        cross_found = False
        for cross in cross_templates:
            if exists(cross):
                touch(cross)
                interstitial_check()
                return True
        if not cross_found:
            sleep(0.5)
            
    logger.warning("No window to close was found after 10 attempts.")
    return False

__all__ = ['random_touch', 'interstitial_check', 'quit_window']
