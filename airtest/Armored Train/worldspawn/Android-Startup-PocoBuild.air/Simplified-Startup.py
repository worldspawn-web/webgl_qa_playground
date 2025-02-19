# -*- encoding=utf8 -*-
__author__ = "Michael 'Worldspawn' Lozickii"
__branch__ = "aqa/unity_poco"
__device__ = "Redmi Note 13"

#   NOTE:   Most likely that you will have to re-name this file in order to run in Airtest
#           Rename to: "Android-Startup-PocoBuild"

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

log_tags = {
    "error": "- [ERROR]: ",
    "assert": "- [ASSERTION]: ",
    "cheats": "- [CHEATS]: "
}

def poco_exception(obj):
    print("\n---------- ERROR ----------\n")
    raise Exception(f"{log_tags['error']}Requested Element has not been found!\nElement ID: {obj}")

def poco_logger(note):
    print(f"{log_tags['assert']}{note}...OK!")
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
        Template(r"tpl1739790881049.png", rgb=True, record_pos=(0.107, -0.079), resolution=(2400, 1080)),
        Template(r"tpl1739818435141.png", rgb=True, target_pos=6, record_pos=(0.363, -0.2), resolution=(2400, 1080)),
        Template(r"tpl1739818808573.png", rgb=True, target_pos=6, record_pos=(0.037, -0.078), resolution=(2400, 1080))
    ]
    
    for btn in btns:
        if exists(btn):
            touch(btn)
            sleep(1.0)
            poco_logger("Close Button")
            return True
        
    raise Exception(f"{log_tags['error']}Sorry, Boss, I haven't found any crossmark to touch.\nCheck your code, idk.\nZzz...")
    
def snapshot_check(snap, note):
    if exists(snap):
        sleep(1.0)
        poco_logger(note)
        return True
    else:
        raise Exception(f"{log_tags['error']}Snapshot has not been found!\nSnapshot Name: {note}")
        
def value_diff(x, y, note = ""):
    x = str(x)
    y = str(y)
    
    if x != y:
        poco_logger(note)
        sleep(0.5)
        return
    else:
        poco_exception(note)
        
def cheats_toggle(cheat):
    c_cross = Template(r"tpl1739816499641.png", record_pos=(0.467, -0.196), resolution=(2400, 1080))
    # Gold/Screw/Coal Future Value
    c_value = 14355341
    # Cheat Opener Speed (Experimental)
    c_swipe_speed = 0.8
    # Logger
    c_tag = log_tags['cheats']
    
    pause_btn = poco(name="PauseButton")
    pause_settings_btn = poco(text="Settings")
    
    def cheatmenu(toggle):
        if toggle:
            pause_btn.click()
            pause_settings_btn.click()
            swipes = [([0.3, 0.3], [0.3, 0.6], 3),
                      ([0.3, 0.3], [0.1, 0.3], 2),
                      ([0.3, 0.3], [0.5, 0.3], 2)]
            
            for start, end, i in swipes:
                for _ in range(i):
                    poco.swipe(start, end, duration=c_swipe_speed)
            poco(name="CheatWindow(Clone)").wait_for_appearance()
            poco_logger("Cheat Window Opened")
            return True

        else:
            if exists(c_cross):
                touch(c_cross)
                poco_logger("Cheat Window Closed")
                for _ in range(2):
                    close_ui()
                return True
            else:
                raise Exception(f"{log_tags['error']}Can't Close Cheat Window!")
            return True
                
    def set_value(value):
        poco("CheatWindow(Clone)").offspring("Give Resources").child("InputField (TMP)").focus().set_text(str(value))
        poco("CheatWindow(Clone)").offspring("Give Resources").child("Button").click()
        
    def kill_enemies():
        poco("CheatWindow(Clone)").offspring("KillAllEnemies").child("Button").click()
        
    def add_resource(resource, value):
        if (resource != "Gold"):
            poco("CheatWindow(Clone)").offspring("Give Resources").child("Dropdown").click()
            poco("CheatWindow(Clone)").offspring("Scroll View").child("Viewport").offspring("Give Resources").offspring(f"Item {resource}").click()
        set_value(value)
        
    def end_battle(result):
        if (result == "win"):
            poco(name="VictoryButton").click()
        else:
            poco(name="DefeatButton").click()
        
    def perform_cheat_action(action, *args):
        print(f"{c_tag}Performing {action.__name__}...")
        cheatmenu(True)
        action(*args)
        cheatmenu(False)
        
    cheat_actions = {
        "killall": lambda: perform_cheat_action(kill_enemies),
        "gold": lambda: perform_cheat_action(add_resource, "Gold", c_value),
        "screwnuts": lambda: perform_cheat_action(add_resource, "1: ScrewNuts", c_value),
        "coal": lambda: perform_cheat_action(add_resource, "2: Coal", c_value),
        "win": lambda: perform_cheat_action(end_battle, "win"),
        "lose": lambda: perform_cheat_action(end_battle, "lose")
    }
    
    if cheat in cheat_actions:
        cheat_actions[cheat]() # calls lambda now, don't touch them
        print(f"{c_tag}Cheat has been activated!")
    else:
        raise Exception(f"{log_tags['error']}Unknown cheat: '{cheat}'")
        
def screw_check(value):
    if (poco("Text (TMP)".get_text() == str(value))):
        poco_logger(f"Screwnuts updated to {value}")
    else:
        poco_exception("Something is wrong with rewards system!")
        
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
    skip_waiting = poco("Skip waiting")
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
    main_wagon_tank = poco(texture="Wagon_TankTurret_Icon(Clone)")
    # Main Scene 3D Environment
    main3d_depot = poco(name="SM_Depot")
    main3d_mechanism = poco(name="SM_Mechanism")
    main3d_loco = poco(name="SM_ArmoredTrain_01")
    main3d_light = poco(name="SM_DepotLight")
    main3d_door_l = poco(name="SM_Door_left")
    main3d_door_r = poco(name="SM_Door_right")
    main3d_wagon_tank = poco(name="SM_Wagon_TankGun_01")
    # Global Map Elements
    hud_top = poco(name="Top")
    hud_bot = poco(name="Bottom")
    hud_map = poco(texture="Global_Map 1")
    hud_currency_n = poco(name="Currency Counter")
    hud_missionview = poco(name="MapMissionView")
    hud_mission_flag = poco(texture="Flag_Red")
    hud_mission_medal = poco(texture="S_icon_Main_mission 1")
    hud_mission_icon = poco(texture="Stalingrad(Clone)")
    hud_mission_pointer = poco(texture="S_pointer")
    hud_mission_2 = poco("Stalingrad")
    hud_difficulty_text = poco("Difficulty:")
    hud_difficulty_easy = poco(texture="S_icon_difficulty_1_star_active")
    hud_difficulty_medium = poco(texture="S_icon_difficulty_2_star_closed")
    hud_difficulty_hard = poco(texture="S_icon_difficulty_3_star_closed")
    hud_back_btn = poco("Back")
    hud_preview = poco(name="MissionPreview")
    hud_preview_header = poco(text="STALINGRAD")
    hud_preview_bg = poco(texture="S_tab_paper")
    hud_preview_deco = poco(texture="S_paper_deco_01")
    hud_preview_h_deco = poco(texture="S_paper_deco_02")
    hud_preview_desc = poco(name="MissionDescription")
    hud_preview_tasks = poco(name="MissionInfo")
    hud_preview_enemies = poco(name="EnemiesInfo")
    hud_preview_reward = poco(name="Reward")
    
    
    #############
    #   START   #
    #############
    
    print("\n---------- #1 — GAME STARTUP & FIRST LEVEL ----------\n")
    
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
    value_diff(money_start, money_end, money_note)
    
    assert_and_touch(skip_waiting, "Skip Waiting", True)
    wave_notify.wait_for_appearance()
    poco_exists(wave_notify, "Wave Notification after Skip")
    
    cheats_toggle("killall")
    
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
    sleep(10.0)
    cheats_toggle("killall")
    reward_image.wait_for_appearance()
    assert_and_touch(reward_image, "Reward Received", True, 2)
    poco_exists(mascot_img, "Mascot")
    random_touch()
    
    victory_window.wait_for_appearance()
    poco_exists(victory_window, "Victory Window")
    poco_exists(poco(texture="Nuts(Clone)"), "Screwnuts Reward")
    victory_reward_lvl1 = poco("VictoryWindow(Clone)").offspring("Amount")
    
    if (victory_reward_lvl1.get_text() == str(30)):
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
    
    print("\n---------- #2 — MAIN SCENE CHECKS ----------\n")
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

    print("\n---------- #3 — MAP CHECKS ----------\n")
    to_mission.click()
    mascot_img.wait_for_appearance()
    
    # Skip Dialog
    for i in range(7):
        random_touch(3.35)
    
    global_map_tutor = Template(r"tpl1739890579440.png", record_pos=(0.001, -0.001), resolution=(2400, 1080))
    snapshot_check(global_map_tutor, "Global Map Appearance")
    
    global_map_checks = {
        "screwnuts": [screwnuts_img, "Global Map - Screwnuts"],
        "hud_top": [hud_top, "Global Map - Top HUD"],
        "hud_bot": [hud_bot, "Global Map - Bot HUD"],
        "hud_map": [hud_map, "Global Map - Map Texture"],
        "hud_currency": [hud_currency_n, "Global Map - Currency HUD"],
        "hud_missionview": [hud_missionview, "Global Map - Mission View"],
        "hud_mission_flag": [hud_mission_flag, "Global Map - Mission Flag"],
        "hud_mission_medal": [hud_mission_medal, "Global Map - Mission Medal"],
        "hud_mission_icon": [hud_mission_icon, "Global Map - Mission Icon"],
        "hud_mission_pointer": [hud_mission_pointer, "Global Map - Mission Pointer"],
        "hud_mission_2": [hud_mission_2, "Global Map - 'Stalingrad' Mission"],
        "hud_difficulty_text": [hud_difficulty_text, "Global Map - Difficulty Text"],
        "hud_difficulty_easy": [hud_difficulty_easy, "Global Map - Easy Difficulty (Unlocked)"],
        "hud_difficulty_mid": [hud_difficulty_medium, "Global Map - Medium Difficulty (Locked)"],
        "hud_difficulty_hard": [hud_difficulty_hard, "Global Map - Hard Difficulty (Locked)"],
        "hud_back_btn": [hud_back_btn, "Global Map - Back Button"],
        "hud_preview": [hud_preview, "Global Map - Mission Preview Panel"],
        "hud_preview_h": [hud_preview_header, "Global Map - Mission Preview Header"],
        "hud_preview_bg": [hud_preview_bg, "Global Map - Mission Preview Background"],
        "hud_preview_deco": [hud_preview_deco, "Global Map - Mission Preview Decoration"],
        "hud_preview_h_deco": [hud_preview_h_deco, "Global Map - Mission Header Deco"],
        "hud_preview_desc": [hud_preview_desc, "Global Map - Mission Preview Description"],
        "hud_preview_tasks": [hud_preview_tasks, "Global Map - Mission Preview Tasks"],
        "hud_preview_enemies": [hud_preview_enemies, "Global Map - Mission Preview Enemies"],
        "hud_preview_reward": [hud_preview_reward, "Global Map - Mission Preview Reward"],
        "tutorial_finger_1": [tutor_finger_0, "Global Map - Tutorial Pointer 1"],
        "tutorial_finger_2": [tutor_finger_2, "Global Map - Tutorial Pointer 2"]
    }

    multiple_checker(global_map_checks)
    # Mission Checks (Stalingrad)
    start_mission.click()
    mascot_img.wait_for_appearance()
    
    for i in range(3): # 3 - ???
        random_touch(3)
        
    # Checks if InputBlocker Works
    input_blocker = poco(name="InputBlocker")
    if (input_blocker.attr("visible")):
        poco_logger("Input Blocker")
    else:
        poco_exception("Input Blocker")
        
    # Follows Tutorial Fades & Pointer
    # in ATT, every tutorial step is "ProxyButton"
    # Since it's a dynamic element, we can't separate it
    # and we have to use it like that...
    for i in range(2):
        poco("Cutscene").offspring("ProxyButton").click()
    
    mascot_img.wait_for_appearance()
    random_touch()
    
    sleep(5.0)
    cheats_toggle("killall")
    
    skip_waiting.click()
    wave_notify.wait_for_appearance()
    
    sleep(10.0)
    # Win through Cheats
    cheats_toggle("win")
    poco_exists(reward_image, "Mission Reward")
    
    # Skips 2 Rewards
    for i in range(2):
        random_touch(1.5)
        
    victory_window.wait_for_appearance()
    
    # Checks for correct rewards (snap)
    rewards_mission2 = Template(r"tpl1739894861328.png", record_pos=(-0.0, 0.05), resolution=(2400, 1080))
    rewards_mission2_note = "Correct Rewards - Mission 2"
    snapshot_check(rewards_mission2, rewards_mission2_note)
    
    to_menu.click()
    main3d_depot.wait_for_appearance() # making sure main scene loaded
    poco_exists(main_wagon_tank, "Tank Wagon Unlocked")
    main_wagon_tank.click()
    sleep(1.0)
    poco_exists(main_wagon_tank, "Tank Wagon (3D)")

    # TODO: separate hardcoded values to json
    screw_check(65)

    
if __name__ == "__main__":
    print("\n---------- RUNNING TESTS ----------\n")
    print(f"Active device: {__device__}")
    main()
    print("\n---------- EVERYTHING IS COOL ----------\n")