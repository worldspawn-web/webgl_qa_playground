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
    dialog_skip
)

auto_setup(__file__)

#                       #
#   Helper Functions    #
#                       #

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
    assert_exists(Template(r"tpl1738171020272.png", record_pos=(0.019, 0.038), resolution=(2400, 1080)), "Successfull Payment.")
    close_window()
    touch(Template(r"tpl1738171088382.png", record_pos=(0.165, -0.026), resolution=(2400, 1080)))

    # New Event Start (dynamic)
    sleep(3.0)
    wait(golden_ticket)
    close_window()  
    
def dragon_ui():
    # Tests will be here...

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
    dragon_ui()
    
    
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
    
#                           #
#   Main Entry Function     #
#                           #
    
def main():
    startup()
    dragon_modal()
    
    
if __name__ == "__main__":
    main()
