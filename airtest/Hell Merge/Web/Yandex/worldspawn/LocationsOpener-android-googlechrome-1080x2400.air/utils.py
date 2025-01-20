from airtest.core.api import *

# Functions
def random_touch():
    sleep(2.0)
    touch([500, 1020])
    
def interstitial_check():
    sleep(3.0)
    if (exists(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    if exists(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))):
        touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))

def autowin_toggle():
    # Enable Auto-Win Cheat
    touch((76, 454))

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
    
    wait(Template(r"tpl1737374734015.png", record_pos=(0.005, -0.061), resolution=(1080, 2400)))
    touch(Template(r"tpl1737374741818.png", rgb=True, record_pos=(-0.097, -0.422), resolution=(1080, 2400)))
    sleep(1.0)
    touch((843, 1492)) # toggler
    sleep(1.0)
    touch(Template(r"tpl1737374755545.png", record_pos=(0.297, -0.419), resolution=(1080, 2400)))
    interstitial_check()
    touch(Template(r"tpl1737374829415.png", record_pos=(0.313, -0.454), resolution=(1080, 2400)))
    interstitial_check()
    
def complete_quest():
    assert_exists(Template(r"tpl1737378790269.png", record_pos=(0.0, 0.269), resolution=(1080, 2400)), "Complete Button.")
    touch(Template(r"tpl1737378790269.png", record_pos=(0.0, 0.269), resolution=(1080, 2400)))
    interstitial_check()

__all__ = ['random_touch', 'interstitial_check', 'autowin_toggle', 'complete_quest']
