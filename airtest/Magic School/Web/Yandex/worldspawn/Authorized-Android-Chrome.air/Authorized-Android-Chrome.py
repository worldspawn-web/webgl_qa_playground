# -*- encoding=utf8 -*-
# ! IMPORT SAVEDATA BEFORE RUNNING !
#
# SAVE NAME:
# MagicSchool-5cpiqJtaJykrCWLQchIkO2GCRazUFl4foA5smdAJ-qU=
#

from airtest.core.api import *
import logging
from utils import (
    random_touch, 
    assert_and_touch,
    close_window,
    yandex_pay
)

auto_setup(__file__)

#                               #
#   Minor Utility Functions     #
#                               #

def open_settings():
    settings_btn = Template(r"tpl1738077103247.png", record_pos=(0.237, -0.102), resolution=(2400, 1080))
    settings_window = Template(r"tpl1738077151793.png", record_pos=(-0.078, 0.042), resolution=(2400, 1080))
    touch(settings_btn)
    wait(settings_window)
    
def flying_reward_claim():
    flying_reward = Template(r"tpl1738147568753.png", record_pos=(-0.075, 0.019), resolution=(2400, 1080))

    if exists(flying_reward):
        touch(flying_reward)
        
        
def leafs_checker():
    templates = [
        Template(r"tpl1738150775316.png", record_pos=(0.162, 0.1), resolution=(2400, 1080)),
    ]
    for leaf in templates:
        if exists(leaf):
            touch(leaf)

    
#                                               #
#   Checks for a correct game & tests start     #
#                                               #

def startup():        
    startup_daily = Template(r"tpl1738070567065.png", record_pos=(-0.078, 0.056), resolution=(2400, 1080))
    if exists(startup_daily):
        random_touch()

    
    offer_noads = Template(r"tpl1738071251829.png", record_pos=(-0.086, 0.06), resolution=(2400, 1080))
    if exists(offer_noads):
        sleep(1.0)
        touch((0.75, 0.7))

    assert_exists(Template(r"tpl1738071315727.png", record_pos=(-0.076, 0.051), resolution=(2400, 1080)), "Game Loaded.")

#                   #
#   Checks CopyID   #
#                   #

def copyid():
    # Values
    id_field = Template(r"tpl1738077228917.png", target_pos=6, record_pos=(-0.049, 0.007), resolution=(2400, 1080))
    expected_id = "5cpiqJtaJykrCWLQchIkO2GCRazUFl4foA5smdAJ-qU="
    
    # Actions
    open_settings()
    assert_and_touch(id_field, "User ID Field.")
    copied_id = get_clipboard()
    assert_equal(copied_id, expected_id, "Copied correct ID.") # does this even work?
    close_window()

#                                                   #
#   Checks Settings Togglers (w/o volume checks)    #
#                                                   #

def togglers_checker():
    # Toggler Parameters
    togglers = [
        {
            "on": Template(r"tpl1738078173835.png", record_pos=(-0.122, 0.142), resolution=(2400, 1080)),
            "off": Template(r"tpl1738078209121.png", record_pos=(-0.122, 0.142), resolution=(2400, 1080)),
            "note": "VFX Toggle"
        },
        {
            "on": Template(r"tpl1738078222028.png", record_pos=(-0.077, 0.142), resolution=(2400, 1080)),
            "off": Template(r"tpl1738078233757.png", record_pos=(-0.078, 0.142), resolution=(2400, 1080)),
            "note": "Music toggle"
        },
        {
            "on": Template(r"tpl1738078247879.png", record_pos=(-0.031, 0.142), resolution=(2400, 1080)),
            "off": Template(r"tpl1738078260018.png", record_pos=(-0.032, 0.142), resolution=(2400, 1080)),
            "note": "Touch toggle"
        }
    ]

    # Actions
    open_settings()
    
    for toggle in togglers:
        assert_and_touch(toggle["on"], toggle["note"])
        sleep(1.0)
        assert_and_touch(toggle["off"], toggle["note"])
        sleep(1.0)

    close_window()
    
#               #
#   IAP Checks  #
#               #

def iap_checks():
    # Hard Offers
    hard_offers = Template(r"tpl1738079311050.png", target_pos=6, record_pos=(0.168, -0.105), resolution=(2400, 1080))
    assert_and_touch(hard_offers, "Hard Offers Counter")
    wait(Template(r"tpl1738079364339.png", record_pos=(-0.073, 0.064), resolution=(2400, 1080)))
    assert_exists(Template(r"tpl1738079409162.png", record_pos=(-0.077, -0.082), resolution=(2400, 1080)), "Any offer disabled adverts.")
    
    yandex_pay(Template(r"tpl1738079516951.png", record_pos=(-0.071, 0.206), resolution=(2400, 1080))) 

    assert_exists(Template(r"tpl1738079946681.png", record_pos=(0.016, 0.029), resolution=(2400, 1080)), "Ads Disabled for N hours.")
    close_window()
    
    values_before = Template(r"tpl1738079576771.png", record_pos=(0.123, -0.103), resolution=(2400, 1080))
    values_after = Template(r"tpl1738079984594.png", record_pos=(0.312, -0.103), resolution=(2400, 1080))
    assert_not_equal(values_after, values_before, "Values Changed after Payment.")
    sleep(1.0)
    close_window()
    
    # Soft Offers
    soft_offers = Template(r"tpl1738080454859.png", target_pos=6, record_pos=(0.269, -0.105), resolution=(2400, 1080))
    noads_token_btn = Template(r"tpl1738080563321.png", record_pos=(-0.157, 0.132), resolution=(2400, 1080))
    
    assert_and_touch(soft_offers, "Soft Value Counter.")
    assert_exists(Template(r"tpl1738080516913.png", record_pos=(0.018, 0.037), resolution=(2400, 1080)), "Shop Window Appeared.")
    assert_exists(Template(r"tpl1738080531332.png", record_pos=(0.02, -0.062), resolution=(2400, 1080)), "Top Panel.")
    assert_exists(Template(r"tpl1738080548297.png", record_pos=(-0.158, 0.069), resolution=(2400, 1080)), "Free Soft Value.")
    assert_and_touch(noads_token_btn, "Get Reward for Ads Tokens Button.")
    
    assert_exists(Template(r"tpl1738080762942.png", record_pos=(0.051, 0.069), resolution=(2400, 1080)), "Other Offers.")
    swipe((0.72, 0.6),(0.3, 0.6))
    sleep(2.0)
    assert_exists(Template(r"tpl1738080813941.png", record_pos=(0.123, 0.068), resolution=(2400, 1080)), "Other Offers #2 + Swiper Works.")
    
    touch(Template(r"tpl1738080861476.png", record_pos=(0.195, 0.13), resolution=(2400, 1080)))
    assert_exists(Template(r"tpl1738080873340.png", record_pos=(0.016, 0.055), resolution=(2400, 1080)), "Confirm Payment Modal.")
    touch(Template(r"tpl1738080889792.png", record_pos=(0.018, 0.136), resolution=(2400, 1080)))
    sleep(1.5)
    close_window()
    
#   ! DROPS DEVICE CONNECTION FOR AN UNKNOWN REASON !
#   TODO: THINK ABOUT ANOTHER WAY OR SOLVE THE ISSUE
#     values_after = Template(r"tpl1738079984594.png", record_pos=(0.312, -0.103), resolution=(2400, 1080))
#     assert_not_equal(Template(r"tpl1738080949543.png", record_pos=(0.313, -0.102), resolution=(2400, 1080)), values_after, "Values Changed after Purchase.")



#                   #
#   NoAds Checker   #
#                   #

def noAds_checks():
    assert_exists(Template(r"tpl1738146840165.png", record_pos=(0.046, -0.2), resolution=(2400, 1080)), "NoAds Counter.")
    assert_and_touch(Template(r"tpl1738146899530.png", record_pos=(0.46, -0.073), resolution=(2400, 1080)), "NoAds Offer.")
    assert_exists(Template(r"tpl1738146960296.png", record_pos=(0.036, -0.008), resolution=(2400, 1080)), "NoAds Offer Extended.")
    assert_exists(Template(r"tpl1738147101545.png", record_pos=(0.199, -0.013), resolution=(2400, 1080)), "NoAds Offer Tokens.")
    noads_buybtn = Template(r"tpl1738147107505.png", record_pos=(0.049, 0.144), resolution=(2400, 1080))
    assert_exists(noads_buybtn, "Price Button.")
    yandex_pay(noads_buybtn)
    assert_exists(Template(r"tpl1738147269316.png", record_pos=(0.04, -0.02), resolution=(2400, 1080)), "Payment Success.")
    close_window()
    # inter_check() <- uncom if inter still appears after payment
    
#                   #
#   Island Purchase #
#                   #

def iap_island():
    # Variables
    island_balloon = Template(r"tpl1738148005369.png", record_pos=(-0.25, 0.172), resolution=(2400, 1080))
    buy_btn = Template(r"tpl1738148059726.png", record_pos=(0.058, 0.161), resolution=(2400, 1080))
    info_btn = Template(r"tpl1738148197539.png", record_pos=(0.191, -0.073), resolution=(2400, 1080))

    
    
    if not exists(island_balloon):
        logging.error("Ballon not exists!")
        return
        
    # Assertions
    assert_and_touch(island_balloon, "Island Balloon Offer.")
    assert_exists(Template(r"tpl1738148037942.png", record_pos=(-0.265, 0.019), resolution=(2400, 1080)), "Left Gnome.")
    assert_exists(Template(r"tpl1738148044412.png", record_pos=(0.315, 0.055), resolution=(2400, 1080)), "Right Gnome.")
    assert_exists(Template(r"tpl1738148054664.png", record_pos=(0.058, -0.006), resolution=(2400, 1080)), "Offer Modal.")
    assert_exists(Template(r"tpl1738148066789.png", record_pos=(0.053, 0.017), resolution=(2400, 1080)), "Offer Modal Image.")
    
    assert_and_touch(info_btn, "Island Info Button.")
    sleep(1.5)
    assert_exists(Template(r"tpl1738148304182.png", record_pos=(0.046, 0.0), resolution=(2400, 1080)), "Island Info Modal.")
    assert_exists(Template(r"tpl1738148320876.png", record_pos=(0.049, 0.039), resolution=(2400, 1080)), "Island Rewards.")
    assert_exists(Template(r"tpl1738148331769.png", record_pos=(0.066, -0.09), resolution=(2400, 1080)), "Island Rewards #2.")
    close_window()
    
    if not exists(buy_btn):
        logging.error("Buy Button is Missing!")
        return
    
    yandex_pay(buy_btn)
    assert_exists(Template(r"tpl1738148411813.png", record_pos=(0.04, -0.019), resolution=(2400, 1080)), "Adverts are Turned off for 48 hours.")
    touch((0.8, 0.5))
    swipe((0.37, 0.94),(0.543, 0.543))
    assert_exists(Template(r"tpl1738148516310.png", record_pos=(-0.12, 0.183), resolution=(2400, 1080)), "Island Unlocked.")

    
def shop_checks():
    # Variables
    shop_btn = Template(r"tpl1738148685832.png", record_pos=(0.307, 0.182), resolution=(2400, 1080))
    buy_icon = Template(r"tpl1738149075249.png", record_pos=(-0.197, 0.104), resolution=(2400, 1080))
    out_of_stock = Template(r"tpl1738149134706.png", record_pos=(-0.178, 0.018), resolution=(2400, 1080))
    refresh_full_stock = Template(r"tpl1738149291216.png", target_pos=6, record_pos=(0.039, 0.156), resolution=(2400, 1080))
    noads_refresh = Template(r"tpl1738149162913.png", rgb=True, record_pos=(-0.181, 0.101), resolution=(2400, 1080))
    
    # Helper Function
    def triple_buy():
        if exists(buy_icon):
            for i in range(3)
                touch(buy_icon)
                
            assert_exists(out_of_stock, "Selected Ingredient is Out of Stock.")

    
    # Assertions
    assert_and_touch(shop_btn, "Shop Button.")
    assert_exists(Template(r"tpl1738148727645.png", record_pos=(0.04, 0.005), resolution=(2400, 1080)), "Shop Window.")
    assert_exists(Template(r"tpl1738148741038.png", record_pos=(0.048, -0.143), resolution=(2400, 1080)), "Ingredients Tab is Active.")
    assert_exists(refresh_full_stock, "Refresh Ingredients Button.")
    assert_exists(Template(r"tpl1738148780093.png", record_pos=(-0.132, -0.068), resolution=(2400, 1080)), "Info Button of the Ingredient.")
    triple_buy()
    assert_and_touch(noads_refresh, "Refresh Ingredient Stock for NoAds Tokens.")
    assert_not_exists(out_of_stock, "Ingredient Stock Refreshed.")

    triple_buy()
    assert_and_touch(refresh_full_stock, "Update Full Stock for Hard Value."
    assert_exists(Template(r"tpl1738149455467.png", record_pos=(0.04, -0.002), resolution=(2400, 1080)), "Confirmation Window.")
    assert_and_touch(Template(r"tpl1738149489808.png", rgb=True, record_pos=(-0.057, 0.064), resolution=(2400, 1080)), "Confirmation - Cancel.")
    assert_and_touch(refresh_full_stock, "Update Full Stock for Hard Value."
    assert_exists(Template(r"tpl1738149455467.png", record_pos=(0.04, -0.002), resolution=(2400, 1080)), "Confirmation Window.")
    assert_and_touch(Template(r"tpl1738149507635.png", rgb=True, record_pos=(0.147, 0.064), resolution=(2400, 1080)), "Confirmation - Confirm.")
    
    if exists(out_of_stock):
        logging.error("Something is Wrong!")
        return
    
    assert_exists(Template(r"tpl1738150005488.png", threshold=0.5, record_pos=(-0.26, -0.135), resolution=(2400, 1080)), "Bought Ingredients in a Fly Reward.")
    
    # Building Purchase
    touch(Template(r"tpl1738150236432.png", target_pos=6, record_pos=(0.038, -0.148), resolution=(2400, 1080)))
    sleep(0.5)
    assert_exists(buy_icon)
    assert_exists(refresh_full_stock)
    triple_buy()
    
    assert_and_touch(noads_refresh, "Buildings out of Stock.")
    assert_exists(Template(r"tpl1738150387072.png", threshold=0.5, record_pos=(-0.263, -0.131), resolution=(2400, 1080)), "Purchased Buildings.")

    # Special (Free Crate)
    free_crate = Template(r"tpl1738150624450.png", rgb=True, target_pos=8, record_pos=(0.095, 0.014), resolution=(2400, 1080))
    touch(Template(r"tpl1738150598111.png", record_pos=(0.25, -0.145), resolution=(2400, 1080)))
    sleep(1.0)
    
    if exists(free_crate):
        touch(free_crate)
        sleep(0.5)
        assert_exists(out_of_stock)
    
    close_window()
    leafs_checker()

#                           #
#   Main Entry Function     #
#                           #
    
def main():
    startup()
    copyid()
    togglers_checker()
    iap_checks()
    flying_reward_claim()
    iap_island()
    noAds_checks()
    

    
    
if __name__ == "__main__":
    main()
