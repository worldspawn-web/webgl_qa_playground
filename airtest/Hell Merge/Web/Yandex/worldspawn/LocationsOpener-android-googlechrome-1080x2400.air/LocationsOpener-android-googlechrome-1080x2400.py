# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Import savedata.json before running the test.
# Test starts on the first loaded scene (w/o offers)
# Source Config Name: HellMerge-plj90Vhd0wJ-BvlXhUhXW5RMy5aLFu6R0uUrYE2ctGw=
# Mode: Authorized
# Version: 1.1.7

__author__ = "Michael 'Worldspawn' Lozickii"

# Removes Debug Logs (Turned Off)
# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

from airtest.core.api import *
auto_setup(__file__)

from utils import interstitial_check, autowin_toggle, complete_quest, random_touch

    
def main():

    # Location Unlock through Button
    assert_exists(Template(r"tpl1737372642596.png", record_pos=(-0.369, 0.455), resolution=(1080, 2400)), "New Location Available Button.")
    touch(Template(r"tpl1737372642596.png", record_pos=(-0.374, 0.452), resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1737372765056.png", record_pos=(0.002, -0.031), resolution=(1080, 2400)), "New Quest Appeared.")

    assert_exists(Template(r"tpl1737372797304.png", record_pos=(-0.407, 0.175), resolution=(1080, 2400)), "New Completed Quest is Visible.")
    sleep(2.0)
    touch(Template(r"tpl1737372797304.png", record_pos=(-0.416, 0.186), resolution=(1080, 2400)))
    wait(Template(r"tpl1737372859053.png", record_pos=(-0.003, -0.08), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737372876995.png", record_pos=(-0.002, -0.119), resolution=(1080, 2400)), "Requested Item.")
    assert_exists(Template(r"tpl1737372885253.png", record_pos=(0.012, 0.073), resolution=(1080, 2400)), "Rewards.")
    touch(Template(r"tpl1737372866943.png", record_pos=(0.004, 0.272), resolution=(1080, 2400)))
    wait(Template(r"tpl1737372921982.png", record_pos=(-0.216, 0.4), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737372937860.png", record_pos=(-0.066, 0.35), resolution=(1080, 2400)), "Boss Mascot Appears.")
    assert_exists(Template(r"tpl1737372957532.png", record_pos=(0.348, -0.719), resolution=(1080, 2400)), "Skip Button & Volume Toggler.")
    touch(Template(r"tpl1737372962523.png", record_pos=(0.351, -0.725), resolution=(1080, 2400)))
    sleep(1.0)


    # Enable Auto-Win Cheat
    autowin_toggle()


    # Auto-Win Checker
    assert_exists(Template(r"tpl1737375153201.png", record_pos=(0.195, -0.192), resolution=(1080, 2400)), "Uncompleted Quest is Completed Now.")
    touch(Template(r"tpl1737375153201.png", record_pos=(0.194, -0.192), resolution=(1080, 2400)))
    sleep(1.0)
    wait(Template(r"tpl1737375189142.png", record_pos=(0.003, -0.089), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737375196856.png", record_pos=(0.004, -0.118), resolution=(1080, 2400)), "Requested Items.")
    assert_exists(Template(r"tpl1737375203483.png", record_pos=(0.004, 0.099), resolution=(1080, 2400)), "Reward.")
    assert_exists(Template(r"tpl1737375222086.png", record_pos=(-0.005, 0.272), resolution=(1080, 2400)), "Complete Button.")
    touch(Template(r"tpl1737375222086.png", record_pos=(0.001, 0.27), resolution=(1080, 2400)))
    
    # Wait for Cutscene
    sleep(10)
    touch(Template(r"tpl1737372962523.png", record_pos=(0.351, -0.725), resolution=(1080, 2400)))
    sleep(1.0)

    # New Level
    assert_exists(Template(r"tpl1737375340393.png", record_pos=(-0.426, -0.68), resolution=(1080, 2400)), "New Level Icon.")
    touch(Template(r"tpl1737375340393.png", record_pos=(-0.426, -0.68), resolution=(1080, 2400)))
    wait(Template(r"tpl1737375409268.png", record_pos=(-0.002, -0.095), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737375416695.png", record_pos=(-0.206, -0.244), resolution=(1080, 2400)), "Completed Level Icon.")
    assert_exists(Template(r"tpl1737375425024.png", record_pos=(0.005, 0.093), resolution=(1080, 2400)), "Incoming Rewards.")
    assert_exists(Template(r"tpl1737375429205.png", rgb=True, record_pos=(-0.002, 0.275), resolution=(1080, 2400)), "Available LVLUP Button.") # rgb parameter MUST be True
    touch(Template(r"tpl1737375429205.png", rgb=True, record_pos=(-0.002, 0.275), resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1737375524410.png", rgb=True, record_pos=(-0.206, -0.238), resolution=(1080, 2400)), "Updated Level.")
    assert_exists(Template(r"tpl1737375540195.png", rgb=True, record_pos=(-0.002, 0.272), resolution=(1080, 2400)), "Button is Locked Now.")
    touch(Template(r"tpl1737375587281.png", record_pos=(0.31, -0.458), resolution=(1080, 2400)))
    interstitial_check()
    
    # Disable Auto-Win to prevent event blocker
    autowin_toggle()
    touch(Template(r"tpl1737378737571.png", record_pos=(0.0, -0.026), resolution=(1080, 2400)))
    complete_quest()
    
    # Cutscene
    sleep(10.0)
    random_touch()
    wait(Template(r"tpl1737380371756.png", record_pos=(0.187, -0.206), resolution=(1080, 2400)))
    touch(Template(r"tpl1737380371756.png", record_pos=(0.187, -0.206), resolution=(1080, 2400)))
    
    # Chuck Event Tutorial
    wait(Template(r"tpl1737379501423.png", record_pos=(-0.003, -0.069), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737379488201.png", record_pos=(0.007, -0.121), resolution=(1080, 2400)), "Event Required Item.")
    random_touch()
    wait(Template(r"tpl1737379533310.png", record_pos=(-0.006, 0.274), resolution=(1080, 2400)))
    touch(Template(r"tpl1737379533310.png", record_pos=(-0.006, 0.274), resolution=(1080, 2400)))
    sleep(1.0)
    wait(Template(r"tpl1737379565742.png", record_pos=(-0.006, -0.013), resolution=(1080, 2400)))
    
    for i in range(2):
           random_touch()
    
    wait(Template(r"tpl1737379615903.png", record_pos=(-0.005, -0.104), resolution=(1080, 2400)))
    touch(Template(r"tpl1737379615903.png", record_pos=(-0.005, -0.104), resolution=(1080, 2400)))
    sleep(3.0)
    wait(Template(r"tpl1737379647393.png", record_pos=(-0.006, -0.048), resolution=(1080, 2400)))
    touch(Template(r"tpl1737379665339.png", record_pos=(-0.002, 0.149), resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1737379686093.png", record_pos=(0.005, 0.247), resolution=(1080, 2400)), "Event Tutorial Mascot.")
    assert_exists(Template(r"tpl1737379696993.png", record_pos=(0.162, -0.585), resolution=(1080, 2400)), "Event Tutorial Fades.")
    random_touch()
    wait(Template(r"tpl1737379784131.png", record_pos=(0.001, -0.057), resolution=(1080, 2400)))
    touch(Template(r"tpl1737379784131.png", record_pos=(0.001, -0.057), resolution=(1080, 2400)))
    
    sleep(1.0)
    touch(Template(r"tpl1737379837314.png", record_pos=(0.3, 0.602), resolution=(1080, 2400))) # leaving event early
    wait(Template(r"tpl1737380546760.png", record_pos=(-0.003, -0.029), resolution=(1080, 2400)))
    
    # Enable Autowin again and complete Chuck Event
    autowin_toggle()
    assert_exists(Template(r"tpl1737381016441.png", record_pos=(0.198, -0.184), resolution=(1080, 2400)), "Clown Event Completed")
    touch(Template(r"tpl1737381016441.png", record_pos=(0.198, -0.184), resolution=(1080, 2400)))
    wait(Template(r"tpl1737381066570.png", record_pos=(0.0, -0.08), resolution=(1080, 2400)))
    complete_quest()
    sleep(3.0)
    wait(Template(r"tpl1737381090320.png", record_pos=(-0.002, -0.083), resolution=(1080, 2400)))
    touch(Template(r"tpl1737381103225.png", record_pos=(0.001, 0.209), resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1737381152820.png", record_pos=(0.006, -0.521), resolution=(1080, 2400)), "Location has 3 stars.")
    
    # Auto Complete Quests
    assert_exists(Template(r"tpl1737381242255.png", record_pos=(-0.168, -0.186), resolution=(1080, 2400)), "Left Quest.")
    touch(Template(r"tpl1737381242255.png", record_pos=(-0.168, -0.186), resolution=(1080, 2400)))
    complete_quest()
    
    assert_exists(Template(r"tpl1737381320547.png", record_pos=(0.369, -0.003), resolution=(1080, 2400)), "Quest.")
    touch(Template(r"tpl1737381320547.png", record_pos=(0.369, -0.003), resolution=(1080, 2400)))
    complete_quest()
    
    # Special Month Event
    wait(Template(r"tpl1737381385141.png", record_pos=(-0.003, -0.022), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737381397113.png", record_pos=(-0.003, -0.456), resolution=(1080, 2400)), "Special Month Event Header.")
    assert_exists(Template(r"tpl1737381406536.png", record_pos=(-0.001, -0.096), resolution=(1080, 2400)), "Special Month Event Image.")
    assert_exists(Template(r"tpl1737381434775.png", record_pos=(-0.002, 0.431), resolution=(1080, 2400)), "Special Month Participate Button.")
    assert_exists(Template(r"tpl1737381450015.png", record_pos=(-0.009, 0.189), resolution=(1080, 2400)), "Timeleft.") # could be broken
    touch(Template(r"tpl1737381434775.png", record_pos=(-0.002, 0.431), resolution=(1080, 2400)))    
    
    sleep(10.0)
    wait(Template(r"tpl1737381523088.png", record_pos=(-0.003, -0.032), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737381530609.png", record_pos=(0.001, -0.03), resolution=(1080, 2400)), "Mascot Dialog.")
    assert_exists(Template(r"tpl1737381554298.png", record_pos=(-0.003, 0.452), resolution=(1080, 2400)), "Completed Event Quest.")
    
    random_touch()
    wait(Template(r"tpl1737381608014.png", record_pos=(-0.13, -0.431), resolution=(1080, 2400)))
    touch(Template(r"tpl1737381608014.png", record_pos=(-0.13, -0.431), resolution=(1080, 2400)))
    interstitial_check() # weird, but inter appeared
    
    wait(Template(r"tpl1737381679751.png", record_pos=(-0.006, 0.004), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737381689778.png", record_pos=(0.004, -0.212), resolution=(1080, 2400)), "Golden Ticket Image.")
    assert_exists(Template(r"tpl1737381699452.png", record_pos=(0.001, 0.506), resolution=(1080, 2400)), "Golden Ticket Buy Button.")
    assert_exists(Template(r"tpl1737381706209.png", record_pos=(0.004, -0.529), resolution=(1080, 2400)), "Golden Ticket Header.")
    touch(Template(r"tpl1737381782191.png", record_pos=(0.306, -0.533), resolution=(1080, 2400)))
    
    sleep(1.0)
    wait(Template(r"tpl1737381813761.png", record_pos=(-0.002, -0.025), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737381827827.png", record_pos=(-0.186, -0.439), resolution=(1080, 2400)), "Golden Ticket Button.")
    assert_exists(Template(r"tpl1737381832352.png", record_pos=(0.176, -0.439), resolution=(1080, 2400)), "Standart Ticket.")
    assert_exists(Template(r"tpl1737381840354.png", record_pos=(-0.003, -0.283), resolution=(1080, 2400)), "Locked Awards #1.")
    assert_exists(Template(r"tpl1737381848239.png", record_pos=(-0.006, -0.044), resolution=(1080, 2400)), "Locked Awards #2.")
    assert_exists(Template(r"tpl1737381854297.png", record_pos=(-0.002, 0.203), resolution=(1080, 2400)), "Locked Awards #3.")
    
    # Swipes till the end of the battlepass
    for i in range(8):
        swipe((321, 1523), (321, 790))
        
    assert_exists(Template(r"tpl1737382124506.png", record_pos=(0.003, 0.178), resolution=(1080, 2400)), "Locked Awards #30.")
    assert_exists(Template(r"tpl1737382130186.png", record_pos=(0.004, -0.055), resolution=(1080, 2400)), "Locked Awards #29.")
    assert_exists(Template(r"tpl1737382133892.png", record_pos=(0.001, -0.299), resolution=(1080, 2400)), "Locked Awards #28.")
    
    touch(Template(r"tpl1737382169345.png", record_pos=(0.194, 0.188), resolution=(1080, 2400)))
    wait(Template(r"tpl1737382177174.png", record_pos=(0.005, -0.038), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737382186526.png", record_pos=(-0.005, -0.191), resolution=(1080, 2400)), "Big Capsule Image.")
    assert_exists(Template(r"tpl1737382190946.png", record_pos=(0.01, 0.01), resolution=(1080, 2400)), "Tropheys Counter.")
    assert_exists(Template(r"tpl1737382196493.png", record_pos=(-0.005, 0.261), resolution=(1080, 2400)), "Drop Chances.")
    assert_exists(Template(r"tpl1737382203374.png", record_pos=(-0.003, -0.433), resolution=(1080, 2400)), "Window Header.")
    touch(Template(r"tpl1737382243343.png", record_pos=(0.304, -0.436), resolution=(1080, 2400)))
    interstitial_check()
    
    # Battlepass Buy
    touch(Template(r"tpl1737382330625.png", target_pos=6, record_pos=(-0.194, -0.438), resolution=(1080, 2400)))
    wait(Template(r"tpl1737382488475.png", record_pos=(-0.005, -0.003), resolution=(1080, 2400)))
    touch(Template(r"tpl1737382482118.png", record_pos=(-0.003, 0.541), resolution=(1080, 2400)))
    wait(Template(r"tpl1737382546543.png", record_pos=(-0.02, -0.444), resolution=(1080, 2400))) # simple wait for Yandex value logo appear; no checks for the price

    if exists(Template(r"tpl1737382525010.png", record_pos=(-0.269, 0.882), resolution=(1080, 2400))):
        touch(Template(r"tpl1737382509499.png", record_pos=(0.004, 0.335), resolution=(1080, 2400)))
    else:
        touch(Template(r"tpl1737382525010.png", record_pos=(-0.269, 0.882), resolution=(1080, 2400)))
        touch(Template(r"tpl1737382509499.png", record_pos=(0.004, 0.335), resolution=(1080, 2400)))
    
    wait(Template(r"tpl1737382620542.png", record_pos=(0.0, 0.098), resolution=(1080, 2400)))
    touch(Template(r"tpl1737382627723.png", record_pos=(0.002, 0.358), resolution=(1080, 2400)))
    sleep(1.0)
    wait(Template(r"tpl1737382642179.png", record_pos=(-0.003, -0.001), resolution=(1080, 2400)))
    touch(Template(r"tpl1737382647884.png", record_pos=(0.002, 0.134), resolution=(1080, 2400)))
    sleep(1.0)
    interstitial_check() # weird, but inter appeared
    wait(Template(r"tpl1737382738926.png", record_pos=(0.006, -0.214), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737382752344.png", record_pos=(0.005, -0.458), resolution=(1080, 2400)), "Award Header.")
    assert_exists(Template(r"tpl1737382758663.png", record_pos=(0.002, -0.073), resolution=(1080, 2400)), "Award Icon + Count.") # could be broken
    random_touch()
    sleep(4.0)
    
    # Getting Rewards from Battlepass
    assert_exists(Template(r"tpl1737382851643.png", record_pos=(0.007, -0.274), resolution=(1080, 2400)), "Unlocked Rewards #1.")
    assert_exists(Template(r"tpl1737382859023.png", record_pos=(0.006, -0.044), resolution=(1080, 2400)), "Locked Rewards #2.")
    touch(Template(r"tpl1737389103890.png", rgb=True, target_pos=8, record_pos=(-0.191, -0.282), resolution=(1080, 2400))) # rgb is essential
    assert_exists(Template(r"tpl1737389147725.png", record_pos=(0.0, -0.221), resolution=(1080, 2400)), "Pre-Unboxing Chosen Crate.")
    random_touch()
    sleep(3.0)
    assert_exists(Template(r"tpl1737389189832.png", record_pos=(-0.003, -0.499), resolution=(1080, 2400)), "Caller Progress Bar.")
    wait(Template(r"tpl1737389203946.png", record_pos=(0.0, -0.044), resolution=(1080, 2400)))
    
    ## Skip all the loot preview from Crate
    for i in range(7)
        random_touch()
        
    assert_exists(Template(r"tpl1737389255339.png", record_pos=(0.003, 0.573), resolution=(1080, 2400)), "Whole Loot Window.") # we can't directly check the images due to randomness
    touch(Template(r"tpl1737389314663.png", record_pos=(0.169, 0.572), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1737389486120.png", record_pos=(0.322, -0.673), resolution=(1080, 2400)))
    interstitial_check()
    touch(Template(r"tpl1737379837314.png", record_pos=(0.3, 0.602), resolution=(1080, 2400)))
    
    # Collections Tutorial
    wait(Template(r"tpl1737389711969.png", record_pos=(0.007, -0.032), resolution=(1080, 2400)))
    wait(Template(r"tpl1737389719704.png", record_pos=(-0.143, 0.599), resolution=(1080, 2400)))
    touch(Template(r"tpl1737389719704.png", record_pos=(-0.143, 0.599), resolution=(1080, 2400)))
    wait(Template(r"tpl1737389752015.png", record_pos=(0.001, 0.544), resolution=(1080, 2400)))
    wait(Template(r"tpl1737389777771.png", record_pos=(0.24, 0.102), resolution=(1080, 2400)))
    touch(Template(r"tpl1737389777771.png", record_pos=(0.24, 0.102), resolution=(1080, 2400)))
    wait(Template(r"tpl1737389803397.png", record_pos=(0.008, -0.515), resolution=(1080, 2400)))
    random_touch()
    wait(Template(r"tpl1737389823582.png", record_pos=(-0.007, -0.145), resolution=(1080, 2400)))
    touch(Template(r"tpl1737389823582.png", record_pos=(-0.007, -0.145), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737389842924.png", record_pos=(-0.35, -0.656), resolution=(1080, 2400)), "Soft Counter.")
    assert_exists(Template(r"tpl1737389858770.png", record_pos=(-0.229, 0.315), resolution=(1080, 2400)), "Boosted Generator Icon.")
    assert_exists(Template(r"tpl1737389862189.png", record_pos=(-0.006, 0.231), resolution=(1080, 2400)), "Progress Bar.")
    assert_exists(Template(r"tpl1737389867750.png", record_pos=(0.01, 0.558), resolution=(1080, 2400)), "Upgrade Button.")
    wait(Template(r"tpl1737389912770.png", record_pos=(0.0, 0.555), resolution=(1080, 2400)))
    touch(Template(r"tpl1737389912770.png", record_pos=(0.0, 0.555), resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1737389950633.png", rgb=True, record_pos=(-0.003, 0.556), resolution=(1080, 2400)), "Button is Disabled.")
    touch(Template(r"tpl1737389971418.png", record_pos=(0.423, -0.667), resolution=(1080, 2400)))
    interstitial_check()
    
    # Buy Collection Cards for Hard Value
    assert_exists(Template(r"tpl1737390037135.png", record_pos=(0.013, -0.541), resolution=(1080, 2400)), "Helper Window.")
    assert_exists(Template(r"tpl1737390021210.png", record_pos=(-0.126, 0.569), resolution=(1080, 2400)), "Buy 11 Cards for 20 Hard Value.")
    assert_exists(Template(r"tpl1737390027443.png", record_pos=(0.006, 0.469), resolution=(1080, 2400)), "Collection Level Progress.")
    touch(Template(r"tpl1737390076711.png", rgb=True, target_pos=8, record_pos=(-0.124, 0.564), resolution=(1080, 2400)))
    sleep(4.0) # delay is increased due to unusual lags
    
    while not exists(Template(r"tpl1737390456873.png", record_pos=(-0.122, 0.597), resolution=(1080, 2400))):
        touch([500, 1020])

    touch(Template(r"tpl1737390480469.png", record_pos=(0.447, -0.655), resolution=(1080, 2400)))
    interstitial_check()
    wait(Template(r"tpl1737390527875.png", record_pos=(-0.005, -0.054), resolution=(1080, 2400)))
    random_touch()
    
    # Cake Fever Event
    wait(Template(r"tpl1737391633404.png", record_pos=(0.0, -0.038), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737391640581.png", record_pos=(0.001, -0.465), resolution=(1080, 2400)), "Cake Fever Header")
    assert_exists(Template(r"tpl1737391647610.png", record_pos=(0.001, -0.122), resolution=(1080, 2400)), "Cake Fever Image.")
    assert_exists(Template(r"tpl1737391652961.png", record_pos=(0.001, 0.426), resolution=(1080, 2400)), "Cake Fever Button.")
    assert_not_exists(Template(r"tpl1737390480469.png", record_pos=(0.001, 0.426), resolution=(1080, 2400)), "There is no 'x' to escape the tutorial.")
    touch(Template(r"tpl1737391652961.png", record_pos=(0.001, 0.426), resolution=(1080, 2400)))
    
    sleep(8.0)
    wait(Template(r"tpl1737391785118.png", record_pos=(-0.002, -0.15), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737391793755.png", record_pos=(-0.193, -0.436), resolution=(1080, 2400)), "Cake Fever Gold Ticket.")
    assert_exists(Template(r"tpl1737391798615.png", record_pos=(0.175, -0.435), resolution=(1080, 2400)), "Cake Fever Standart Ticket.")
    assert_exists(Template(r"tpl1737391805329.png", record_pos=(-0.002, 0.331), resolution=(1080, 2400)), "Locked Awards #18.")
    assert_exists(Template(r"tpl1737391809567.png", record_pos=(-0.006, 0.093), resolution=(1080, 2400)), "Locked Awards #19.")
    assert_exists(Template(r"tpl1737391814063.png", record_pos=(-0.008, -0.148), resolution=(1080, 2400)), "Locked Awards #20.")
    wait(Template(r"tpl1737391826025.png", record_pos=(-0.007, 0.585), resolution=(1080, 2400))) 
    touch(Template(r"tpl1737391826025.png", record_pos=(-0.007, 0.585), resolution=(1080, 2400)))
    
    assert_exists(Template(r"tpl1737391907284.png", record_pos=(-0.006, 0.627), resolution=(1080, 2400)), "Cake Fever Owen Temperature.")
    assert_exists(Template(r"tpl1737391913245.png", record_pos=(0.01, -0.606), resolution=(1080, 2400)), "Cake Fever Level Progress.")
    assert_exists(Template(r"tpl1737391920419.png", record_pos=(0.002, 0.421), resolution=(1080, 2400)), "Basic Cakes.")
    swipe(Template(r"tpl1737391992558.png", record_pos=(-0.219, 0.423), resolution=(1080, 2400)), vector=[0.1575, -0.186]) # dangerous
    swipe(Template(r"tpl1737392017509.png", record_pos=(0.001, 0.426), resolution=(1080, 2400)), vector=[-0.0567, -0.2472]) # dangerous x2
    assert_exists(Template(r"tpl1737392053259.png", record_pos=(-0.063, -0.194), resolution=(1080, 2400)), "Cakes Combined.") # could be randomized, unchecked - dangerous x3
    swipe((784, 1656), (750, 1195))
    assert_exists(Template(r"tpl1737392192830.png", record_pos=(-0.183, 0.608), resolution=(1080, 2400)), "Higher Owen Temperature.")
    
    # We simply cannot check here:
    # - which cakes are coming next
    # - how cakes are combined
    # - how cakes are acting when the field is full
    
    touch(Template(r"tpl1737392282750.png", record_pos=(0.313, -0.706), resolution=(1080, 2400)))
    sleep(5.0)
    interstitial_check()
    assert_exists(Template(r"tpl1737392310384.png", record_pos=(0.426, -0.396), resolution=(1080, 2400)), "Cake Fever Icon on the Main Scene.")
    touch(Template(r"tpl1737392310384.png", record_pos=(0.426, -0.396), resolution=(1080, 2400)))
    wait(Template(r"tpl1737391785118.png", record_pos=(-0.002, -0.15), resolution=(1080, 2400)))
    touch(Template(r"tpl1737391793755.png", record_pos=(-0.193, -0.436), resolution=(1080, 2400)))
    wait(Template(r"tpl1737393404651.png", record_pos=(0.0, -0.006), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1737393413306.png", record_pos=(0.006, -0.226), resolution=(1080, 2400)), "Cake Fever Golden Ticket Image.")
    touch(Template(r"tpl1737393431436.png", record_pos=(-0.002, 0.534), resolution=(1080, 2400)))
    wait(Template(r"tpl1737382546543.png", record_pos=(-0.02, -0.444), resolution=(1080, 2400))) # simple wait for Yandex value logo appear; no checks for the price

    if exists(Template(r"tpl1737382525010.png", record_pos=(-0.269, 0.882), resolution=(1080, 2400))):
        touch(Template(r"tpl1737382509499.png", record_pos=(0.004, 0.335), resolution=(1080, 2400)))
    else:
        touch(Template(r"tpl1737382525010.png", record_pos=(-0.269, 0.882), resolution=(1080, 2400)))
        touch(Template(r"tpl1737382509499.png", record_pos=(0.004, 0.335), resolution=(1080, 2400)))
    
    wait(Template(r"tpl1737382620542.png", record_pos=(0.0, 0.098), resolution=(1080, 2400)))
    touch(Template(r"tpl1737382627723.png", record_pos=(0.002, 0.358), resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1737393519130.png", record_pos=(-0.181, -0.434), resolution=(1080, 2400)), "Battlepass Purchased.")
    touch(Template(r"tpl1737393544503.png", record_pos=(0.304, -0.671), resolution=(1080, 2400)))

if __name__ == "__main__":
    main()
