from airtest.core.api import *

# Functions
def random_touch():
    sleep(2.0)
    touch([500, 1020])
    
# Checks for Interstitial
# Call after every window close on the main scene!
def interstitial_check():
    sleep(3.0)
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    if exists(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))):
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))