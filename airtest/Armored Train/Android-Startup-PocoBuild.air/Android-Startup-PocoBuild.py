# -*- encoding=utf8 -*-
__author__ = "Michael 'Worldspawn' Lozickii"
__branch__ = "aqa/unity_poco"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import logging

auto_setup(__file__)
poco = UnityPoco()

logging.getLogger("airtest").setLevel(logging.ERROR)
logging.getLogger("poco").setLevel(logging.ERROR)
logging.getLogger("adb").setLevel(logging.ERROR)

########################
#   HELPER FUNCTIONS   #
########################

def poco_exception(obj):
    print("---------- ERROR ----------")
    raise Exception(f"Requested Element has not been found!\nElement ID: {obj}")

def poco_logger(obj):
    print(f"- {obj}...OK!")
    return

def poco_exists(img, note = ""):
    if img.exists():
        poco_logger(note)
    else:
        poco_exception(note)
    sleep(0.5)
    return

def assert_and_touch(img, note = "", pocoInstance = False, delay = 1.0):
    if pocoInstance:
        if img.exists():
            img.click()
            poco_logger(note)
        else:
            poco_exception(note)
        return
    
    if assert_exists(img, note):
        touch(img)
        sleep(delay)
        poco_logger(note)
    else:
        poco_exception(note)
    return
    
def random_touch(delay = 1.0):
    touch((0.5, 0.5))
    sleep(delay)
    return

def multiple_checker(obj):
    for key, (el, note) in obj.items():
            poco_exists(el, note)
    return

# def switch_device(id):
#     try:
#         set_current(id)
#         print(f"Successfully connected to\n-{id}")
#         return True
#     except:
#         raise Exception(f"Error while connecting to device with serial number:\n-{id}")

###################
#   TESTS START   #
###################

def main():
    
    #####################
    #   Poco Variables  #
    #####################
    # Tutorial
    to_mission = poco(text="TO MISSION!")
    loader_play = poco(text="PLAY")
    start_mission = poco(text="START")
    tutor_finger_0 = poco(name="TutorHand_0")
    tutor_finger_2 = poco(name="TutorHand_2")
    # Mascot
    mascot_img = poco(name="Character Image")
    mascot_header = poco(text="GENERAL")
    # Battle HUD
    wave_notify = poco(name="WaveNotify(Clone)")
    rotation_input = poco(name="RotationInput")
    skip_waiting = poco(name="SkipButton")
    wagons_btn = poco(name="ProxyButton")
    exit_wagons = poco(name="ExitButton")
    buy_wagon = poco(text="Buy")
    city_name = poco(text="Defend the objective")
    goals_hud = poco(name="GoalHud")
    # Locomotive
    hp_bars = poco(name="TrainHp")
    hp_bar_loco = poco("LocoHp Variant(Clone)")
    # Main Goal
    main_goal = poco(text="Eliminate all waves enemies")
    main_goal_icon = poco("Battle HUD").offspring("Icon")
    main_goal_bar = poco("Battle HUD").offspring("ProgressBar")
    main_goal_progress = poco("Battle HUD").offspring("Progress")
    # Victory/Defeat
    reward_image = poco("RenderImage")
    victory_window = poco("VictoryWindow(Clone)").offspring("Background1")
    to_menu = poco(text="TO MAIN MENU")
    # Pause & Settings
    pause_btn = poco(name="PauseButton")
    pause_settings_btn = poco(text="Settings")
    close_btn = poco(name="Close Button")
    pause_settings_panel = poco(name="Settings Panel")
    settings_sound_h2 = poco(text="Sound")
    # settings_gameplay_h2 = poco(text="Gameplay")
    privacy_policy = poco(text="PRIVACY POLICY")

    
    #############
    #   START   #
    #############
    
    # Scenes
    assert_exists(Template(r"tpl1739382112852.png", record_pos=(-0.003, -0.001), resolution=(2400, 1080)), "Post-Loader Screen")
    assert_and_touch(loader_play, "Post Loader Play Button", True)
    assert_exists(Template(r"tpl1739383777982.png", record_pos=(-0.0, -0.0), resolution=(2400, 1080)), "Tutorial Mascot Appeared")
    random_touch()
    assert_exists(Template(r"tpl1739383067899.png", record_pos=(-0.0, -0.001), resolution=(2400, 1080)), "Tutorial Finger")
    assert_and_touch(to_mission, "'To Mission' Button", True)
    assert_exists(Template(r"tpl1739458153564.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Global Map Appeared")
    
    # Skip Dialog
    for i in range(4):
        random_touch(3)
    
    # Tutorial Pointer (Finger) Existence
    poco_exists(tutor_finger_2, "Tutorial Finger 1")
    poco_exists(tutor_finger_0, "Tutorial Finger 2")
    
    assert_and_touch(start_mission, "Start Mission Button", True, 1)
    # <- TODO: add quick check for loader screen
    
    # Waiting for Mascot (General)
    mascot_header.wait_for_appearance()
    assert_exists(Template(r"tpl1739459007447.png", record_pos=(-0.001, 0.0), resolution=(2400, 1080)), "First Mission Tutorial")
    assert_and_touch(mascot_img, "Mascot", True, 3)
    assert_exists(Template(r"tpl1739459175444.png", record_pos=(-0.009, -0.172), resolution=(2400, 1080)), "City HP with Fade")

    for i in range(2):
        random_touch()
        
    money_start = poco(text="350") # Money on Mission Start

    mascot_img.wait_for_appearance()
    assert_and_touch(wave_notify, "Wave Notification", True, 6.0)
    rotation_input.wait_for_appearance()
    assert_and_touch(rotation_input, "Wagon Input Handler", True)
    
    # Handler Functionality
    # TODO: Add before/after checks with Poco attribute values
    poco.swipe([0.863, 0.625], [0.859, 0.883])
    poco.swipe([0.859, 0.833], [0.849, 0.769])
    poco_logger("Handler Swipes")

    mascot_img.wait_for_appearance()
    random_touch(2.5)
    
    money_end = poco(text="365")
    money_note = "Soft Money Change"
    
    if money_start != money_end:
        poco_logger(money_note)
    else:
        poco_exception(money_note)
    
    assert_and_touch(skip_waiting, "Skip Waiting", True)
    wave_notify.wait_for_appearance()
    poco_exists(wave_notify, "Wave Notification after Skip")
    
    mascot_img.wait_for_appearance()
    
    for i in range(3):
        random_touch(3)
        
    # Wagon Buy Tutorial
    assert_and_touch(wagons_btn, "Wagons Button", True, 3.5)
    tutorial_open_wagons = poco("Cutscene").offspring("ProxyButton")
    assert_and_touch(tutorial_open_wagons, "Open Available Wagons Button", True)
    
    tutorial_select_1st_wagon = poco("TrainManagerWindow(Clone)").offspring("Available Wagons View").offspring("Selection (1)")
    assert_and_touch(tutorial_select_1st_wagon, "Select First Wagon by Tutorial", True)
    
    assert_and_touch(buy_wagon, "Buy Wagon Button", True, 2.5)
    poco_exists(mascot_img, "Mascot Image")
    random_touch()
    
    # HUD (Wagons Menu) Checks
    loco_icon = poco("TrainManagerWindow(Clone)").offspring("Content").child("WagonScrollViewItem(Clone)")[0].child("Background")
    loco_hp_bar = poco("TrainManagerWindow(Clone)").offspring("Content").child("WagonScrollViewItem(Clone)")[0].child("Health")
    poco_exists(loco_icon, "Locomotive Icon")
    poco_exists(loco_hp_bar, "Locomotive HP Bar")
    exit_wagons.click()
    
    # HUD (Level) Checks
    poco_exists(hp_bars, "Train HP Widget")
    poco_exists(hp_bar_loco, "Loco HP Bar")
    poco_exists(city_name, "City Name (Defend)")
    

    assert_and_touch(goals_hud, "Goals HUD", True, 2)
    poco_exists(main_goal, "Main Goal Description")
    poco_exists(main_goal_icon, "Main Goal Icon")
    poco_exists(main_goal_bar, "Main Goal Progress Bar")
    poco_exists(main_goal_progress, "Main Goal Progress Score")
    
    # Pause Checks
    assert_and_touch(pause_btn, "Pause Button", True)
    # <- TODO: Check that previous elements are not clickable through attr
    pause_note = "Pause Menu"
    
    if exists(Template(r"tpl1739470762870.png", record_pos=(-0.001, -0.01), resolution=(2400, 1080))):
        poco_logger(pause_note)
    else:
        poco_exception(pause_note)

    # Pause Settings
    assert_and_touch(pause_settings_btn, "Pause Settings Button", True)
    pause_settings_panel.wait_for_appearance()
    poco_exists(pause_settings_panel, "Pause Setting Panel")
    poco_exists(settings_sound_h2, "Sounds Header")
    # poco_exists(settings_gameplay_h2, "Gameplay Header")
    
    settings_icons = {
        "volume": [poco(texture="S_icon_volume"), "Volume Icon"],
        "music": [poco(texture="S_icon_music"), "Music Icon"],
        "sounds": [poco(texture="S_icon_sounds"), "Sounds Icon"],
        "graphics": [poco(texture="S_icon_graphics"), "Graphics Icon"],
        "language": [poco(texture="S_icon_language"), "Language Icon"]
    }
    
    multiple_checker(settings_icons)
    
    assert_and_touch(close_btn, "Close Settings", True, 1.0)
    assert_and_touch(close_btn, "Close Settings", True)
    
    # Tutorial Level Ending
    reward_image.wait_for_appearance()
    assert_and_touch(reward_image, "Reward Received", True, 2)
    poco_exists(mascot_img, "Mascot")
    random_touch()
    
    victory_window.wait_for_appearance()
    poco_exists(victory_window, "Victory Window")
    assert_and_touch(to_menu, "Back to the Menu Button", True)
    
if __name__ == "__main__":
    print("---------- RUNNING TESTS ----------")
    print("Current device: Redmi Note 13")
    main()
    print("---------- EVERYTHING IS COOL ----------")
