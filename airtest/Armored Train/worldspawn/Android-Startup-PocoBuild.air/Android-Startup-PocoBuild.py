# -*- encoding=utf8 -*-

# NOTE: IF YOU NEED A SIMPLE VERSION, USE:
#       -   "Simplified-Startup.py" (could possibly be outdated)

from airtest.core.api import *

from poco.drivers.unity3d import UnityPoco
from cheats import cheats_toggle
from ui_elements import UIElements
from assets import Assets3D
from helpers import (
    config, poco, poco_exception, poco_logger, poco_exists,
    assert_and_touch, random_touch, multiple_checker, close_ui,
    snapshot_check, value_diff, screw_check, head_log, poco_swipe
)
import logging

auto_setup(__file__)
poco = UnityPoco()

# Global Variables Definition (modify in main())
ui = None
assets = None

# Logger Settings. Currently sets everything to "error/warning-only"
for logger, level in config['log_levels'].items():
    logging.getLogger(logger).setLevel(getattr(logging, level))

def game_startup():
    head_log("GAME STARTUP & FIRST LEVEL")
    
    # Scenes
    snapshot_check(Template(r"snapshots/tpl1739382112852.png", record_pos=(-0.003, -0.001), resolution=(2400, 1080)), "Post-Loader Screen")
    assert_and_touch(ui.loader_play, "Post Loader Play Button", True)
    snapshot_check(Template(r"snapshots/tpl1739383777982.png", record_pos=(-0.0, -0.0), resolution=(2400, 1080)), "Tutorial Mascot Appeared")
    random_touch()
    snapshot_check(Template(r"snapshots/tpl1739383067899.png", record_pos=(-0.0, -0.001), resolution=(2400, 1080)), "Tutorial Finger")
    assert_and_touch(ui.to_mission, "'To Mission' Button", True)
    snapshot_check(Template(r"snapshots/tpl1739458153564.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Global Map Appeared")
    
    # Skip Dialog
    for _ in range(4):
        random_touch(3)
    
    # Tutorial Pointer (Finger) Existence
    poco_exists(ui.tutor_finger_2, "Tutorial Finger 1")
    poco_exists(ui.tutor_finger_0, "Tutorial Finger 2")
    
    assert_and_touch(ui.start_mission, "Start Mission Button", True, 1)
    
    # Waiting for Mascot (General)
    ui.mascot_header.wait_for_appearance()
    snapshot_check(Template(r"snapshots/tpl1739459007447.png", record_pos=(-0.001, 0.0), resolution=(2400, 1080)), "First Mission Tutorial")
    assert_and_touch(ui.mascot_img, "Mascot", True, 3)
    snapshot_check(Template(r"snapshots/tpl1739459175444.png", record_pos=(-0.009, -0.172), resolution=(2400, 1080)), "City HP with Fade")

    for _ in range(2):
        random_touch()
        
    money_start = poco("Text (TMP)").get_text() # Money on Mission Start
    
    ui.mascot_img.wait_for_appearance()
    sleep(3.0)
    assert_and_touch(ui.wave_notify, "Wave Notification", True)
    ui.rotation_input.wait_for_appearance()
    assert_and_touch(ui.rotation_input, "Wagon Input Handler", True)
    
    # Handler Functionality
    handler_up_pos = [0.863, 0.625]
    handler_down_pos = [0.859, 0.883]
    handler_mid_pos = [0.849, 0.769]
    poco_swipe(handler_up_pos, handler_down_pos)
    poco_swipe(handler_down_pos, handler_mid_pos)
    poco_logger("Handler Swipes")
    
    snapshot_check(Template(r"tpl1740053667938.png", record_pos=(-0.065, -0.154), resolution=(2400, 1080)), "Tutorial Stop-pos Glow.")

    ui.mascot_img.wait_for_appearance()
    random_touch(2.0)
    money_end = poco("Text (TMP)").get_text()
    value_diff(money_start, money_end, "Soft Money Change")
    
    assert_and_touch(ui.skip_waiting, "Skip Waiting", True)
    ui.wave_notify.wait_for_appearance()
    poco_exists(ui.wave_notify, "Wave Notification after Skip")
    
    sleep(3.0)
    cheats_toggle("killall")
    
    ui.mascot_img.wait_for_appearance()
    
    for _ in range(4):
        random_touch(3)
        
    # Wagon Buy Tutorial
    ui.wagons_btn.wait_for_appearance()
    assert_and_touch(ui.wagons_btn, "Wagons Button", True, 3.5)
    tutorial_open_wagons = poco("Cutscene").offspring("ProxyButton")
    assert_and_touch(tutorial_open_wagons, "Open Available Wagons Button", True)
    
    tutorial_select_1st_wagon = poco("TrainManagerWindow(Clone)").offspring("Available Wagons View").offspring("Selection (1)")
    assert_and_touch(tutorial_select_1st_wagon, "Select First Wagon by Tutorial", True)
    
    assert_and_touch(ui.buy_wagon, "Buy Wagon Button", True, 2.5)
    poco_exists(ui.mascot_img, "Mascot Image")
    random_touch()
    
    # HUD (Wagons Menu) Checks
    loco_icon = poco("TrainManagerWindow(Clone)").offspring("Content").child("WagonScrollViewItem(Clone)")[0].child("Background")
    loco_hp_bar = poco("TrainManagerWindow(Clone)").offspring("Content").child("WagonScrollViewItem(Clone)")[0].child("Health")
    poco_exists(loco_icon, "Locomotive Icon")
    poco_exists(loco_hp_bar, "Locomotive HP Bar")
    ui.exit_wagons.click()
    
    # HUD (Level) Checks
    poco_exists(ui.hp_bars, "Train HP Widget")
    poco_exists(ui.hp_bar_loco, "Loco HP Bar")
    poco_exists(ui.city_name, "City Name (Defend)")
    
    assert_and_touch(ui.goals_hud, "Goals HUD", True, 2)
    poco_exists(ui.main_goal, "Main Goal Description")
    poco_exists(ui.main_goal_icon, "Main Goal Icon")
    poco_exists(ui.main_goal_bar, "Main Goal Progress Bar")
    poco_exists(ui.main_goal_progress, "Main Goal Progress Score")
    
    # Pause Checks
    assert_and_touch(ui.pause_btn, "Pause Button", True)
    pause_note = "Pause Menu"
    
    if exists(Template(r"snapshots/tpl1739470762870.png", record_pos=(-0.001, -0.01), resolution=(2400, 1080))):
        poco_logger(pause_note)
    else:
        poco_exception(pause_note)

    # Pause Settings
    assert_and_touch(ui.pause_settings_btn, "Pause Settings Button", True)
    ui.pause_settings_panel.wait_for_appearance()
    poco_exists(ui.pause_settings_panel, "Pause Setting Panel")
    poco_exists(ui.settings_sound_h2, "Sounds Header")
    
    settings_icons = {
        "volume": [ui.icon_volume, "Volume Icon"],
        "music": [ui.icon_music, "Music Icon"],
        "sounds": [ui.icon_sounds, "Sounds Icon"],
        "graphics": [ui.icon_graphics, "Graphics Icon"],
        "language": [ui.icon_language, "Language Icon"]
    }
    
    multiple_checker(settings_icons)
    
    for _ in range(2):
        close_ui()
    
    # Tutorial Level Ending
    sleep(10.0)
    cheats_toggle("killall")
    ui.reward_image.wait_for_appearance()
    assert_and_touch(ui.reward_image, "Reward Received", True, 2)
    poco_exists(ui.mascot_img, "Mascot")
    random_touch()
    
    ui.victory_window.wait_for_appearance()
    poco_exists(ui.victory_window, "Victory Window")
    poco_exists(poco(texture="Nuts(Clone)"), "Screwnuts Reward")
    victory_reward_lvl1 = poco("VictoryWindow(Clone)").offspring("Amount")
    
    if victory_reward_lvl1.get_text() == str(config['rewards']['level_1']):
        poco_logger("Correct Reward Amount")
    else:
        poco_exception("Incorrect Reward Amount! Ask GD if balance has been changed.")
    
    # Victory Window UI Checks
    victory_window_els = {
        "bg": [ui.victory_bg, "Dark Background"],
        "flags_back": [ui.victory_flags_back, "Victory Flags (Back)"],
        "victory_vfx": [ui.victory_vfx, "Victory Wreath (VFX)"],
        "flags_mid": [ui.victory_flags_mid, "Victory Flags (Middle)"],
        "star": [ui.victory_star, "Victory Star"],
        "victory_txt": [ui.victory_txt, "Victory Text"],
        "window_bg": [ui.victory_window_bg, "Window Texture"],
        "window_decor": [ui.victory_window_decor, "Window Decorations"],
    }
    multiple_checker(victory_window_els)
    
    if (ui.victory_txt.get_text() == "VICTORY"):
        poco_logger("Correct Victory Header")
    else:
        poco_exception("Victory Header")
    
    assert_and_touch(ui.to_menu, "Back to the Menu Button", True, 3.0)
    
def main_checks():
    head_log("MAIN SCENE CHECKS")
    
    main_checks = {
        "screwnuts_icon": [ui.screwnuts_img, "Screwnuts Icon"],
        "settings_btn_menu": [ui.pause_btn_menu, "Settings Button (Main Scene)"],
        "active_stats_panel": [ui.active_stats_menu, "Active Stats Panel"],
        "active_stats_deco": [ui.active_stats_deco, "Active Stats Decoration"],
        "active_stats_desc": [ui.active_stats_desc, "Active Stats Description"],
        "stats_damage_icon": [ui.stats_damage_icon, "Stats Damage Icon"],
        "stats_armor_icon": [ui.stats_armor_icon, "Stats Armor Icon"],
        "stats_firerate_icon": [ui.stats_firerate_icon, "Stats Firerate Icon"],
        "stats_guns_x_icon": [ui.stats_guns_x_icon, "Stats Number of Guns Icon"],
        "stat_name": [ui.stat_name, "Stat Naming"],
        "stat_value": [ui.stat_value, "Stat Value"],
        "stat_bg_slider": [ui.stat_bg_slider, "Stat Background Slider"],
        "stat_fill_slider": [ui.stat_fill_slider, "Stat Fill Slider (Active)"],
        "stat_handle_slider": [ui.stat_handle_slider, "Stat Handle Slider (Separation)"],
        "active_wagon_text": [ui.main_wagon_title, "Active Wagon Title"],
        "loco": [ui.main_loco, "Main Scene Loco Icon"],
        "wagon_mg": [ui.main_machinegun, "Main Scene MachineGun Wagon Icon"],
        "depot": [assets.depot, "Main Scene Depot"],
        "rotate_mech": [assets.mechanism, "Depot Mechanism"],
        "depot_loco": [assets.loco, "Depot Loco"],
        "depot_light": [assets.depot_light, "Depot Light"],
        "depot_door_l": [assets.depot_door_l, "Depot Door (Left)"],
        "depot_door_r": [assets.depot_door_r, "Depot Door (Right)"],   
    }
    
    multiple_checker(main_checks)

    # Verification Snapshot
    stats_note = "General Stats Appearance (Snapshot)"
    stats_snap = Template(r"snapshots/tpl1739793021032.png", record_pos=(-0.375, -0.025), resolution=(2400, 1080))
    snapshot_check(stats_snap, stats_note)
    
def map_checks():
    head_log("MAP CHECKS")

    ui.to_mission.click()
    ui.mascot_img.wait_for_appearance()
    
    # Skip Dialog
    for _ in range(9):
        random_touch(3.35)
    
    global_map_tutor = Template(r"snapshots/tpl1739890579440.png", record_pos=(0.001, -0.001), resolution=(2400, 1080))
    snapshot_check(global_map_tutor, "Global Map Appearance")
        
    # Global Map UI Checks
    global_map_checks = {
        "screwnuts": [ui.screwnuts_img, "Global Map - Screwnuts"],
        "hud_top": [ui.hud_top, "Global Map - Top HUD"],
        "hud_bot": [ui.hud_bot, "Global Map - Bot HUD"],
        "hud_map": [ui.hud_map, "Global Map - Map Texture"],
        "hud_currency": [ui.hud_currency_n, "Global Map - Currency HUD"],
        "hud_missionview": [ui.hud_missionview, "Global Map - Mission View"],
        "hud_mission_flag": [ui.hud_mission_flag, "Global Map - Mission Flag"],
        "hud_mission_medal": [ui.hud_mission_medal, "Global Map - Mission Medal"],
        "hud_mission_icon": [ui.hud_mission_icon, "Global Map - Mission Icon"],
        "hud_mission_pointer": [ui.hud_mission_pointer, "Global Map - Mission Pointer"],
        "hud_mission_2": [ui.hud_mission_2, "Global Map - 'Stalingrad' Mission"],
        "hud_difficulty_text": [ui.hud_difficulty_text, "Global Map - Difficulty Text"],
        "hud_difficulty_easy": [ui.hud_difficulty_easy, "Global Map - Easy Difficulty (Unlocked)"],
        "hud_difficulty_mid": [ui.hud_difficulty_medium, "Global Map - Medium Difficulty (Locked)"],
        "hud_difficulty_hard": [ui.hud_difficulty_hard, "Global Map - Hard Difficulty (Locked)"],
        "hud_back_btn": [ui.hud_back_btn, "Global Map - Back Button"],
        "hud_preview": [ui.hud_preview, "Global Map - Mission Preview Panel"],
        "hud_preview_h": [ui.hud_preview_header, "Global Map - Mission Preview Header"],
        "hud_preview_bg": [ui.hud_preview_bg, "Global Map - Mission Preview Background"],
        "hud_preview_deco": [ui.hud_preview_deco, "Global Map - Mission Preview Decoration"],
        "hud_preview_h_deco": [ui.hud_preview_h_deco, "Global Map - Mission Header Deco"],
        "hud_preview_desc": [ui.hud_preview_desc, "Global Map - Mission Preview Description"],
        "hud_preview_tasks": [ui.hud_preview_tasks, "Global Map - Mission Preview Tasks"],
        "hud_preview_enemies": [ui.hud_preview_enemies, "Global Map - Mission Preview Enemies"],
        "hud_preview_reward": [ui.hud_preview_reward, "Global Map - Mission Preview Reward"],
        "tutorial_finger_1": [ui.tutor_finger_0, "Global Map - Tutorial Pointer 1"],
        "tutorial_finger_2": [ui.tutor_finger_2, "Global Map - Tutorial Pointer 2"]
    }
    multiple_checker(global_map_checks)
    
def mission_2():
    head_log("MISSION 2 - STALINGRAD")
    
    ui.start_mission.click()
    ui.mascot_img.wait_for_appearance()
    
    sleep(2.0)
    
    for _ in range(3):
        random_touch(3)
        
    # Checks if InputBlocker Works
    input_blocker = poco(name="InputBlocker")
    if input_blocker.attr("visible"):
        poco_logger("Input Blocker")
    else:
        poco_exception("Input Blocker")
            
    # Follows Tutorial Fades & Pointer
    for _ in range(3):
        click_pos = poco("Cutscene").offspring("ProxyButton")
        click_pos.click()
        sleep(3.0)
    
    random_touch(2)
    
    # Win through Cheats
    cheats_toggle("win")
    poco_exists(ui.reward_image, "Mission Reward")
    
    # Skips 2 Rewards
    for _ in range(2):
        random_touch(1.5)
        
    ui.victory_window.wait_for_appearance()
    
    # Checks for correct rewards (snap)
    rewards_mission2 = Template(r"snapshots/tpl1739894861328.png", record_pos=(-0.0, 0.05), resolution=(2400, 1080))
    rewards_mission2_note = "Correct Rewards - Mission 2"
    snapshot_check(rewards_mission2, rewards_mission2_note)
    
    ui.to_menu.click()
    assets.depot.wait_for_appearance() # making sure main scene loaded
    poco_exists(ui.main_wagon_tank, "Tank Wagon Unlocked")
    ui.main_wagon_tank.click()
    sleep(1.0)
    poco_exists(assets.wagon_tank, "Tank Wagon (3D)")

    screw_check(config['rewards']['level_2'])

def main():
    global ui, assets
    ui = UIElements()
    assets = Assets3D()
    
    game_startup()
    main_checks()
    map_checks()
    mission_2()

if __name__ == "__main__":
    head_log("RUNNING TESTS")
    print(f"Active device: {config['device']}")
    main()
    head_log("EVERYTHING IS COOL")

