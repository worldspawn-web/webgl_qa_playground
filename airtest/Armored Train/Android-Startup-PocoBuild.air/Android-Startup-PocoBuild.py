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

###################
#   TESTS START   #
###################

def main():
    
    #####################
    #   Poco Variables  #
    #####################
    
    to_mission = poco(text="TO MISSION!")
    loader_play = poco(text="PLAY")
    start_mission = poco(text="START")
    tutor_finger_0 = poco(name="TutorHand_0")
    tutor_finger_2 = poco(name="TutorHand_2")
    mascot_img = poco(name="Character Image")
    mascot_header = poco(text="GENERAL")
    wave_notify = poco(name="WaveNotify(Clone)")
    rotation_input = poco(name="RotationInput")
    skip_waiting = poco(name="SkipButton")
    wagons_btn = poco(name="ProxyButton")
    buy_wagon = poco(text="Buy")
    city_name = poco(text="Defend the objective")
    goals_hud = poco(name="GoalHud")
    reward_image = poco("RenderImage")
    victory_window = poco("VictoryWindow(Clone)").offspring("Background1")
    to_menu = poco(text="TO MAIN MENU")
    exit_wagons = poco(name="ExitButton")
    
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

    for i in range(3):
        random_touch()

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
    poco_exists(city_name, "City Name (Defend)")
    poco_exists(goals_hud, "Goals Hud")
    exit_wagons.click()
    
    # HUD (Level) Checks
    # TODO...
    
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
    main()
    print("---------- EVERYTHING IS COOL ----------")
