# -*- encoding=utf8 -*-
__author__ = "Michael 'Worldspawn' Lozickii"
__branch__ = "aqa/unity_poco"
__device__ = "Redmi Note 13"

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

def poco_logger(note):
    print(f"- {note}...OK!")
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

def close_ui():
    btns = [
        Template(r"tpl1739790881049.png", record_pos=(0.107, -0.079), resolution=(2400, 1080)),
    ]
    
    for btn in btns:
        if exists(btn):
            touch(wait(btn))
            sleep(1.4)
            poco_logger("Close Button")
            return
        raise Exception("Sorry, Boss, I haven't found any crossmark to touch.\nCheck your code, idk.\nZzz...")
        return
    
def snapshot_check(snap, note):
    if exists(snap):
        sleep(1.0)
        poco_logger(note)
        return True
    else:
        raise Exception(f"Snapshot has not been found T_T\nSnapshot Name: {note}")
        
def value_matcher(x, y, note = ""):
    if x = y:
        poco_logger(note)
        sleep(0.5)
        return
    else:
        poco_exception(note)
        

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
    
    # Main Scene
    pause_btn_menu = poco(name="Settings")
    screwnuts_img = poco(texture="Nuts(Clone)")
    active_stats_menu = poco(texture="S_tab_paper")
    active_stats_deco = poco(texture="S_paper_deco_01")
    active_stats_desc = poco(name="Desc")
    # Stats Icons
    stats_damage_icon = poco(texture="Damage(Clone)")
    stats_armor_icon = poco(texture="Hp(Clone)")
    stats_firerate_icon = poco(texture="GunReload(Clone)")
    stats_guns_x_icon = poco(texture="Modernization(Clone)")
    # Stat Checks
    stat_name = poco(text="Number of guns")
    stat_value = poco(name="Value")
    stat_bg_slider = poco(name="Background")
    stat_fill_slider = poco(name="Fill")
    stat_handle_slider = poco(name="Handle")
    # Main Scene Wagons
    main_wagon_title = poco(name="WagonName")
    main_loco = poco(texture="Locomotive_Icon(Clone)")
    main_machinegun = poco(texture="Wagon_MachineGun_Icon(Clone)")
    # Main Scene 3D Environment
    main3d_depot = poco(name="SM_Depot")
    main3d_mechanism = poco(name="SM_Mechanism")
    main3d_loco = poco(name="SM_ArmoredTrain_01")
    main3d_light = poco(name="SM_DepotLight")
    main3d_door_l = poco(name="SM_Door_left")
    main3d_door_r = poco(name="SM_Door_right")
    
    #############
    #   START   #
    #############
    
    print("---------- #1 — GAME STARTUP & FIRST LEVEL ----------")
    
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
        
    money_start = poco("Text (TMP)").get_text() # Money on Mission Start
    
    mascot_img.wait_for_appearance()
    sleep(3.0)
    assert_and_touch(wave_notify, "Wave Notification", True)
    rotation_input.wait_for_appearance()
    assert_and_touch(rotation_input, "Wagon Input Handler", True)
    
    # Handler Functionality
    # TODO: Add before/after checks with Poco attribute values
    poco.swipe([0.863, 0.625], [0.859, 0.883])
    poco.swipe([0.859, 0.833], [0.849, 0.769])
    poco_logger("Handler Swipes")

    mascot_img.wait_for_appearance()
    random_touch(2.5)
    money_end = poco("Text (TMP)").get_text()
    money_note = "Soft Money Change"
#     value_matcher(money_start, money_end, money_note) # uncom later
    
    assert_and_touch(skip_waiting, "Skip Waiting", True)
    wave_notify.wait_for_appearance()
    poco_exists(wave_notify, "Wave Notification after Skip")
    
    mascot_img.wait_for_appearance()
    
    for i in range(4):
        random_touch(3)
        
    # Wagon Buy Tutorial
    wagons_btn.wait_for_appearance()
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
    
    for i in range(2):
        close_ui()
    
    # Tutorial Level Ending
    reward_image.wait_for_appearance()
    assert_and_touch(reward_image, "Reward Received", True, 2)
    poco_exists(mascot_img, "Mascot")
    random_touch()
    
    victory_window.wait_for_appearance()
    poco_exists(victory_window, "Victory Window")
    poco_exists(poco(texture="Nuts(Clone)"), "Screwnuts Reward")
    victory_reward_lvl1 = poco(name="Amount")
    
    if (victory_reward_lvl1.get_text()) == 30:
        poco_logger("Correct Reward Amount")
    else:
        poco_exception("Incorrect Reward Amount! Ask GD if balance has been changed.")
    
    victory_window_els = {
        "bg": [poco(texture="S_darken"), "Dark Background"],
        "flags_back": [poco(name="FlagsBack"), "Victory Flags (Back)"],
        "victory_vfx": [poco(name="Wreath"), "Victory Wreath (VFX)"],
        "flags_mid": [poco(name="FlagsMiddle"), "Victory Flags (Middle)"],
        "star": [poco(name="Star"), "Victory Star"],
        "victory_txt": [poco(text="VICTORY"), "Victory Text"],
        "window_bg": [poco(texture="S_tab_paper"), "Window Texture"],
        "window_decor": [poco(texture="S_paper_deco_01"), "Window Decorations"],
    }
    
    multiple_checker(victory_window_els)
    
    assert_and_touch(to_menu, "Back to the Menu Button", True, 3.0)
    
    print("---------- #2 — MAIN SCENE CHECKS ----------")
    screwnuts_start = poco(text="30")
    
    main_ui_checks = {
        "screwnuts_icon": [screwnuts_img, "Screwnuts Icon"],
        "settings_btn_menu": [pause_btn_menu, "Settings Button (Main Scene)"],
        # Active Stats Panel Visual
        "active_stats_panel": [active_stats_menu, "Active Stats Panel"],
        "active_stats_deco": [active_stats_deco, "Active Stats Decoration"],
        "active_stats_desc": [active_stats_desc, "Active Stats Description"],
        # Stat Icons
        "stats_damage_icon": [stats_damage_icon, "Stats Damage Icon"],
        "stats_armor_icon": [stats_armor_icon, "Stats Armor Icon"],
        "stats_firerate_icon": [stats_firerate_icon, "Stats Firerate Icon"],
        "stats_guns_x_icon": [stats_guns_x_icon, "Stats Number of Guns Icon"],
        # Stat Checks
        "stat_name": [stat_name, "Stat Naming"],
        "stat_value": [stat_value, "Stat Value"],
        "stat_bg_slider": [stat_bg_slider, "Stat Background Slider"],
        "stat_fill_slider": [stat_fill_slider, "Stat Fill Slider (Active)"],
        "stat_handle_slider": [stat_handle_slider, "Stat Handle Slider (Separation)"],
        # Available Wagons & Loco
        "active_wagon_text": [main_wagon_title, "Active Wagon Title"],
        "loco": [main_loco, "Main Scene Loco Icon"],
        "wagon_mg": [main_machinegun, "Main Scene MachineGun Wagon Icon"],
        # 3D Environment
        "depot": [main3d_depot, "Main Scene Depot"],
        "rotate_mech": [main3d_mechanism, "Depot Mechanism"],
        "depot_loco": [main3d_loco, "Depot Loco"],
        "depot_light": [main3d_light, "Depot Light"],
        "depot_door_l": [main3d_door_l, "Depot Door (Left)"],
        "depot_door_r": [main3d_door_r, "Depot Door (Right)"],   
    }
    
    multiple_checker(main_ui_checks)

    # Verification Snapshot
    stats_note = "General Stats Appearance (Snapshot)"
    stats_snap = Template(r"tpl1739793021032.png", record_pos=(-0.375, -0.025), resolution=(2400, 1080))
    snapshot_check(stats_snap, stats_note)

    
if __name__ == "__main__":
    print("---------- RUNNING TESTS ----------")
    print(f"Active device: {__device__}")
    main()
    print("---------- EVERYTHING IS COOL ----------")
