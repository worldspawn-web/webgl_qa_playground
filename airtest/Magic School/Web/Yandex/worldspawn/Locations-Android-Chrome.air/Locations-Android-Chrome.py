# -*- encoding=utf8 -*-
# ! IMPORT SAVEDATA BEFORE RUNNING !
#
# SAVE NAME:
# MagicSchool-5cpiqJtaJykrCWLQchIkO2GCRazUFl4foA5smdAJ-qU=
#

from airtest.core.api import *
import logging
from utils import (
    special_touch,
    inter_check,
    close_window,
    yandex_pay,
    random_touch,
    dialog_skip,
    assert_and_touch,
    leafs_checker,
    reload_page,
    use_generators
)

auto_setup(__file__)


#                                       #
#   Special Startup for the Savefile    #
#                                       #

def startup():
    # Daily Reward Assertions
    # were checked in another test file
    # -> Authorized-Android-Chrome.air
    assert_exists(Template(r"tpl1738167965657.png", record_pos=(-0.077, 0.051), resolution=(2400, 1080)), "Daily Reward Appeared.")
    special_touch("side")
    inter_check()
    
    # Previous Event 'Chest Rush' Ending
    chest_rush_item = Template(r"tpl1738169131106.png", record_pos=(-0.216, 0.049), resolution=(2400, 1080))
    if not exists(chest_rush_item, "Previous Event Ending Window."):
        close_window()
        
    # Previous Event 
    assert_exists(chest_rush_item, "Main Event Item.")
    assert_exists(Template(r"tpl1738169328020.png", record_pos=(-0.029, 0.05), resolution=(2400, 1080)), "Free Items.")
    assert_exists(Template(r"tpl1738169341272.png", record_pos=(-0.027, 0.127), resolution=(2400, 1080)), "Golden Items (Locked).")
    
    golden_ticket = Template(r"tpl1738169354815.png", target_pos=8, record_pos=(-0.215, 0.129), resolution=(2400, 1080))
    golden_ticket_btn = Template(r"tpl1738170106361.png", record_pos=(-0.08, 0.178), resolution=(2400, 1080))
    assert_and_touch(golden_ticket, "Golden Ticket.")

    assert_exists(Template(r"tpl1738170096872.png", record_pos=(-0.074, 0.03), resolution=(2400, 1080)), "Golden Ticket Icon.")
    assert_exists(Template(r"tpl1738170102023.png", record_pos=(-0.074, 0.103), resolution=(2400, 1080)), "Incoming Gold Rewards.")
    
    assert_exists(golden_ticket_btn, "Buy Button.")
    yandex_pay(golden_ticket_btn)
    inter_check()
    touch(Template(r"tpl1738171088382.png", record_pos=(0.165, -0.026), resolution=(2400, 1080)))

    # New Event Start (dynamic)
    sleep(3.0)
    wait(golden_ticket)
    close_window()  
    
#                       #
#   Dragon UI Checks    #
#                       #

def dragon_ui():
    ## Different Energy
    assert_exists(Template(r"tpl1738235818507.png", record_pos=(-0.32, -0.103), resolution=(2400, 1080)), "Event Energy.")
    # <- assert_not_exists "Main Energy"
    
    event_info_btn = Template(r"tpl1738235991451.png", record_pos=(-0.311, 0.186), resolution=(2400, 1080))
    assert_exists(event_info_btn, "Event Info Button.")
    event_bp_btn = Template(r"tpl1738235996873.png", record_pos=(-0.365, 0.188), resolution=(2400, 1080))
    assert_exists(event_bp_btn, "Current Event Level Button.")
    assert_exists(Template(r"tpl1738236006564.png", record_pos=(-0.365, -0.086), resolution=(2400, 1080)), "User Avatar (Dragon).") # special for this savedata
    assert_exists(Template(r"tpl1738236052011.png", threshold=0.5, record_pos=(-0.365, 0.058), resolution=(2400, 1080)), "Quests List.")
    
    touch(event_info_btn)
    sleep(1.0)
    assert_exists(Template(r"tpl1738236157651.png", record_pos=(-0.117, 0.087), resolution=(2400, 1080)), "Mascot Image.")
    assert_exists(Template(r"tpl1738236163691.png", record_pos=(0.082, 0.011), resolution=(2400, 1080)), "Resources Required for Trade.")
    assert_exists(Template(r"tpl1738236168001.png", record_pos=(0.085, 0.128), resolution=(2400, 1080)), "Trade Items.")
    assert_exists(Template(r"tpl1738236173031.png", rgb=True, record_pos=(0.084, 0.198), resolution=(2400, 1080)), "Locked Button.")
    
    hint_btn = Template(r"tpl1738236190117.png", record_pos=(-0.134, -0.052), resolution=(2400, 1080))
    assert_and_touch(hint_btn, "Hint Button.")
    sleep(0.5)
    assert_exists(Template(r"tpl1738236226161.png", record_pos=(-0.012, 0.075), resolution=(2400, 1080)), "Hint Image.")
    special_touch("side", True)
    
    close_window()
    
    # Pinch (zoom) doens't work :(
    # pinch('out', center=(540, 1080))

    touch(Template(r"tpl1738236849503.png", target_pos=6, record_pos=(-0.26, -0.202), resolution=(2400, 1080)))
    sleep(1.0)
    assert_exists(Template(r"tpl1738236864759.png", record_pos=(-0.036, -0.028), resolution=(2400, 1080)), "Event Energy Sets.")
    assert_exists(Template(r"tpl1738236868701.png", record_pos=(-0.043, 0.031), resolution=(2400, 1080)), "Event Energy Image.")
    assert_exists(Template(r"tpl1738236911021.png", record_pos=(-0.035, 0.117), resolution=(2400, 1080)), "Energy for Soft.")
    assert_exists(Template(r"tpl1738236934091.png", record_pos=(0.131, 0.115), resolution=(2400, 1080)), "Energy for Ads.")

    close_window()

#                           #
#   Dragon Event Tutorial   #
#                           #

def dragon_tutorial():
    dragon_mascot = Template(r"tpl1738171311517.png", record_pos=(-0.171, -0.008), resolution=(2400, 1080))
    
    wait(dragon_mascot)
    dialog_skip(2) # could be broken or too fast
    assert_exists(Template(r"tpl1738171511008.png", record_pos=(-0.01, 0.077), resolution=(2400, 1080)), "Basic Tutorial Image.")
    assert_exists(dragon_mascot, "Dragon Island Mascot.")
    random_touch()
    assert_exists(Template(r"tpl1738171593487.png", record_pos=(-0.003, 0.073), resolution=(2400, 1080)), "Basic Tutorial Image #2.")
    random_touch()
    sleep(2.0)
    
    # Page Reload -> Save Check
    reload_page()
    wait(Template(r"tpl1738235523154.png", record_pos=(-0.105, 0.022), resolution=(2400, 1080)))
    special_touch("side", True)

    if not exists(Template(r"tpl1738235613473.png", record_pos=(0.082, 0.055), resolution=(2400, 1080))):
        try:
            close_window()
        except:
            logging.error("Something is wrong!")

    # Go to UI Checks
    dragon_ui()

#                           #
#   Checks for Dragon Modal #
#                           #

def dragon_modal():
    dragon_modal = Template(r"tpl1738171189807.png", target_pos=6, record_pos=(0.013, -0.025), resolution=(2400, 1080))

    if exists(dragon_modal):
        assert_exists(Template(r"tpl1738171210130.png", record_pos=(-0.122, 0.055), resolution=(2400, 1080)), "Event Rewards.")
        assert_exists(Template(r"tpl1738171214383.png", record_pos=(-0.12, 0.134), resolution=(2400, 1080)), "Dragon Golden Ticket.")
        assert_exists(Template(r"tpl1738171225903.png", record_pos=(0.037, 0.055), resolution=(2400, 1080)), "Possible Rewards.")
        touch(dragon_modal)
        sleep(3.0)
        dragon_tutorial()
    else:
        return

#                                           #
#   Complex Tutorial Checks with Swipes     #
#                                           #

def swipes_for_tutor():
    # hardcoded
    for i in range (2):  
        swipe((0.485, 0.579), (0.516, 0.606))
    
    # <--- congratulations window (missed)
    random_touch()
    assert_exists(Template(r"tpl1738238234186.png", record_pos=(0.058, -0.003), resolution=(2400, 1080)), "Energy Reward for BP LevelUp.")
    random_touch()
    
    wait(Template(r"tpl1738238265427.png", record_pos=(-0.104, -0.102), resolution=(2400, 1080)))
    assert_and_touch(Template(r"tpl1738238278624.png", target_pos=2, record_pos=(-0.023, 0.002), resolution=(2400, 1080)), "Unlocked Reward.")
    assert_and_touch(Template(r"tpl1738238317196.png", record_pos=(0.051, -0.01), resolution=(2400, 1080)), "Reward Receive.")

    swipe((0.485, 0.579), (0.516, 0.606))
    sleep(1.0)
    
    wait(Template(r"tpl1738238392421.png", record_pos=(-0.212, -0.031), resolution=(2400, 1080)))
    dialog_skip(2)
    
    sleep(3.0)
    assert_and_touch(Template(r"tpl1738238477036.png", target_pos=2, record_pos=(0.053, 0.01), resolution=(2400, 1080)), "Tutorial Pointer.")
    sleep(2.0)
    assert_and_touch(Template(r"tpl1738238547769.png", target_pos=8, record_pos=(0.131, 0.161), resolution=(2400, 1080)), "Tutorial Trade.")
    wait(Template(r"tpl1738238605984.png", record_pos=(0.047, -0.03), resolution=(2400, 1080)))
    random_touch()
    
    ## Moving to another zone
    swipe((0.5, 0.03), (0.5, 0.3)) # swiping to the req. area
    use_generators("dark_blue")
    
    # Re-launch auto generators usage, since we got a popup window
    use_generators("dark_blue")

    # Swipes on full board
    for i in range(3):
        swipe((0.497, 0.567), (0.545, 0.62))
        sleep(0.5)
    
    # Trade Checks
    for i in range(4):
        assert_and_touch(Template(r"tpl1738239554747.png", record_pos=(-0.281, 0.177), resolution=(2400, 1080)), "Quest Completed Button")
        assert_and_touch(Template(r"tpl1738239576077.png", rgb=True, record_pos=(0.129, 0.188), resolution=(2400, 1080)), "Trade Button.")
        assert_exists(Template(r"tpl1738239601353.png", record_pos=(-0.044, 0.01), resolution=(2400, 1080)), "Traded Items Appeared.")
        assert_exists(Template(r"tpl1738239605868.png", record_pos=(0.004, -0.01), resolution=(2400, 1080)), "Traded Items Appeared #2.")

        
    # Foster Rewards
    assert_and_touch(Template(r"tpl1738241124244.png", record_pos=(-0.351, 0.093), resolution=(2400, 1080)), "Foster Rewards Button.")
    assert_exists(Template(r"tpl1738241147738.png", record_pos=(0.051, -0.008), resolution=(2400, 1080)), "Foster Rewards Modal.")
    assert_exists(Template(r"tpl1738241154251.png", record_pos=(0.163, 0.032), resolution=(2400, 1080)), "Premium Rewards.")
    assert_exists(Template(r"tpl1738241158146.png", record_pos=(-0.032, 0.036), resolution=(2400, 1080)), "Basic Rewards.")
    foster_buy_btn = Template(r"tpl1738241659077.png", record_pos=(0.159, 0.152), resolution=(2400, 1080))
    assert_exists(foster_buy_btn, "Buy Button.")
    yandex_pay(foster_buy_btn)

    
    # Golden Ticket
    assert_and_touch(Template(r"tpl1738242499752.png", record_pos=(-0.352, 0.174), resolution=(2400, 1080)), "Battlepass Icon.")
    assert_and_touch(Template(r"tpl1738242507420.png", target_pos=8, record_pos=(-0.133, 0.105), resolution=(2400, 1080)), "Golden Ticket.")
    yandex_pay(Template(r"tpl1738242700943.png", record_pos=(0.047, 0.164), resolution=(2400, 1080))
    assert_exists(Template(r"tpl1738242747525.png", record_pos=(0.025, 0.101), resolution=(2400, 1080)), "Golden Rewards Exist.")
    touch(Template(r"tpl1738242770261.png", target_pos=2, record_pos=(-0.022, 0.102), resolution=(2400, 1080)))
    assert_and_touch(Template(r"tpl1738242783202.png", record_pos=(0.039, -0.005), resolution=(2400, 1080)), "Golden Reward.")

    
#                           #
#   Main Entry Function     #
#                           #
    
def main():
    startup()
    dragon_modal()
    use_generators("blue")
    swipes_for_tutor()
    
    
if __name__ == "__main__":
    main()
