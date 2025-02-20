from helpers import poco

# UI Elements
# This class contains all poco variable definitions
#
# To add new one:
#   - self.name = poco(...)
#
# To use in main code:
#   - from ui_elements import UIElements
#   - ui = UIElements()
#   - ui.name

class UIElements:
    def __init__(self):
        # Tutorial
        self.to_mission = poco(text="TO MISSION!")
        self.loader_play = poco(text="PLAY")
        self.start_mission = poco(text="START")
        self.tutor_finger_0 = poco(name="TutorHand_0")
        self.tutor_finger_2 = poco(name="TutorHand_2")
        
        # Mascot
        self.mascot_img = poco(name="Character Image")
        self.mascot_header = poco(text="GENERAL")
        
        # Battle HUD
        self.wave_notify = poco(name="WaveNotify(Clone)")
        self.rotation_input = poco(name="RotationInput")
        self.skip_waiting = poco("Text (TMP)")
        self.wagons_btn = poco(name="ProxyButton")
        self.exit_wagons = poco(name="ExitButton")
        self.buy_wagon = poco(text="Buy")
        self.city_name = poco(text="Defend the objective")
        self.goals_hud = poco(name="GoalHud")
        
        # Locomotive
        self.hp_bars = poco(name="TrainHp")
        self.hp_bar_loco = poco("LocoHp Variant(Clone)")
        
        # Main Goal
        self.main_goal = poco(text="Eliminate all waves enemies")
        self.main_goal_icon = poco("Battle HUD").offspring("Icon")
        self.main_goal_bar = poco("Battle HUD").offspring("ProgressBar")
        self.main_goal_progress = poco("Battle HUD").offspring("Progress")
        
        # Victory/Defeat
        self.reward_image = poco("RenderImage")
        self.victory_window = poco("VictoryWindow(Clone)").offspring("Background1")
        self.to_menu = poco(text="TO MAIN MENU")
        
        # Pause & Settings
        self.pause_btn = poco(name="PauseButton")
        self.pause_settings_btn = poco(text="Settings")
        self.close_btn = poco(name="Close Button")
        self.pause_settings_panel = poco(name="Settings Panel")
        self.settings_sound_h2 = poco(text="Sound")
        self.privacy_policy = poco(text="PRIVACY POLICY")
        
        # Icons
        self.icon_volume = poco(texture="S_icon_volume")
        self.icon_music = poco(texture="S_icon_music")
        self.icon_sounds = poco(texture="S_icon_sounds")
        self.icon_graphics = poco(texture="S_icon_graphics")
        self.icon_language = poco(texture="S_icon_language")
        
        # Main Scene
        self.pause_btn_menu = poco(name="Settings")
        self.screwnuts_img = poco(texture="Nuts(Clone)")
        self.active_stats_menu = poco(texture="S_tab_paper")
        self.active_stats_deco = poco(texture="S_paper_deco_01")
        self.active_stats_desc = poco(name="Desc")
        
        # Stats Icons
        self.stats_damage_icon = poco(texture="Damage(Clone)")
        self.stats_armor_icon = poco(texture="Hp(Clone)")
        self.stats_firerate_icon = poco(texture="GunReload(Clone)")
        self.stats_guns_x_icon = poco(texture="Modernization(Clone)")
        
        # Stat Checks
        self.stat_name = poco(text="Number of guns")
        self.stat_value = poco(name="Value")
        self.stat_bg_slider = poco(name="Background")
        self.stat_fill_slider = poco(name="Fill")
        self.stat_handle_slider = poco(name="Handle")
        
        # Main Scene Wagon Icons
        self.main_wagon_title = poco(name="WagonName")
        self.main_loco = poco(texture="Locomotive_Icon(Clone)")
        self.main_machinegun = poco(texture="Wagon_MachineGun_Icon(Clone)")
        self.main_wagon_tank = poco(texture="Wagon_TankTurret_Icon(Clone)")
        
        # Global Map Elements
        self.hud_top = poco(name="Top")
        self.hud_bot = poco(name="Bottom")
        self.hud_map = poco(texture="Global_Map 1")
        self.hud_currency_n = poco(name="Currency Counter")
        self.hud_missionview = poco(name="MapMissionView")
        self.hud_mission_flag = poco(texture="Flag_Red")
        self.hud_mission_medal = poco(texture="S_icon_Main_mission 1")
        self.hud_mission_icon = poco(texture="Stalingrad(Clone)")
        self.hud_mission_pointer = poco(texture="S_pointer")
        self.hud_mission_2 = poco("Stalingrad")
        self.hud_difficulty_text = poco("MapWindow Variant(Clone)").offspring("Bottom").child("Difficulty").child("Text (TMP)")
        self.hud_difficulty_easy = poco(texture="S_icon_difficulty_1_star_active")
        self.hud_difficulty_medium = poco(texture="S_icon_difficulty_2_star_closed")
        self.hud_difficulty_hard = poco(texture="S_icon_difficulty_3_star_closed")
        self.hud_back_btn = poco("Back")
        self.hud_preview = poco(name="MissionPreview")
        self.hud_preview_header = poco(text="STALINGRAD")
        self.hud_preview_bg = poco(texture="S_tab_paper")
        self.hud_preview_deco = poco(texture="S_paper_deco_01")
        self.hud_preview_h_deco = poco(texture="S_paper_deco_02")
        self.hud_preview_desc = poco(name="MissionDescription")
        self.hud_preview_tasks = poco(name="MissionInfo")
        self.hud_preview_enemies = poco(name="EnemiesInfo")
        self.hud_preview_reward = poco(name="Reward")
        
        # Victory / Defeat Window
        self.victory_bg = poco(texture="S_darken")
        self.victory_flags_back = poco(name="FlagsBack")
        self.victory_vfx = poco(name="Wreath")
        self.victory_flags_mid = poco(name="FlagsMiddle")
        self.victory_star = poco(name="Star")
        self.victory_txt = poco("VictoryWindow(Clone)").offspring("Text")
        self.victory_window_bg = poco(texture="S_tab_paper")
        self.victory_window_decor = poco(texture="S_paper_deco_01")