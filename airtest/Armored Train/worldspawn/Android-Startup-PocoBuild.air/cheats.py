from airtest.core.api import *
from helpers import poco, config, log_tags, poco_logger, close_ui

# This function toggles any desired cheat
def cheats_toggle(cheat):
    c_cross = Template(r"snapshots/tpl1739816499641.png", record_pos=(0.467, -0.196), resolution=(2400, 1080))
    c_value = config['cheat_values']['resources']
    c_swipe_speed = config['cheat_values']['swipe_speed']
    c_tag = log_tags['cheats']
    
    pause_btn = poco(name="PauseButton")
    pause_settings_btn = poco(text="Settings")
    
    # Opens cheat menu with swipes, if toggle = True
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
                    poco_logger(f"pos_1: {start}, pos_2: {end}, Duration: {c_swipe_speed}", "swipe")
            poco(name="CheatWindow(Clone)").wait_for_appearance()
            poco_logger("Cheat Window Opened", "cheats")
            return True
        # Closes cheat menu through crossmarks, if toggle = False
        else:
            if exists(c_cross):
                touch(c_cross)
                poco_logger("Cheat Window Closed", "cheats")
                for _ in range(2):
                    close_ui()
                return True
            else:
                raise Exception(f"{log_tags['error']}Can't Close Cheat Window!")
    
    # Sets desired value for gold/coal/screwnuts input field
    # Usually uses pre-defined variable c_value
    def set_value(value):
        poco("CheatWindow(Clone)").offspring("Give Resources").child("InputField (TMP)").focus().set_text(str(value))
        poco("CheatWindow(Clone)").offspring("Give Resources").child("Button").click()
        poco_logger(f"Setted Value: {value}", "cheats")
    
    # Simply, kills all enemies
    def kill_enemies():
        poco("CheatWindow(Clone)").offspring("KillAllEnemies").child("Button").click()
        poco_logger(f"Kill all enemy units", "cheats")
    
    # Sets desired resource type, then goes to set_value()
    def add_resource(resource, value):
        if resource != "Gold":
            poco("CheatWindow(Clone)").offspring("Give Resources").child("Dropdown").click()
            poco("CheatWindow(Clone)").offspring("Scroll View").child("Viewport").offspring("Give Resources").offspring(f"Item {resource}").click()
        set_value(value)
        poco_logger(f"Added resource {resource}: +{value}", "cheats")
    
    # Quick Win/Defeat
    def end_battle(result):
        if result == "win":
            poco(name="VictoryButton").click()
        else:
            poco(name="DefeatButton").click()
        poco_logger(f"Ended battle with result: {result}", "cheats")
        return
    
    # Toggles cheat menu before & after selected cheat activation
    def perform_cheat_action(action, *args):
        print(f"{c_tag}Performing {action.__name__}...")
        cheatmenu(True)
        action(*args)
        if (action != end_battle):
            cheatmenu(False)
    
    # List of all cheat actions
    # NOTE: lambda's essential, or every cheat will be executed
    cheat_actions = {
        "killall": lambda: perform_cheat_action(kill_enemies),
        "gold": lambda: perform_cheat_action(add_resource, "Gold", c_value),
        "screwnuts": lambda: perform_cheat_action(add_resource, "1: ScrewNuts", c_value),
        "coal": lambda: perform_cheat_action(add_resource, "2: Coal", c_value),
        "win": lambda: perform_cheat_action(end_battle, "win"),
        "lose": lambda: perform_cheat_action(end_battle, "lose")
    }
    
    # Checks if selected cheat exists, then executes
    if cheat in cheat_actions:
        cheat_actions[cheat]()
        print(f"{c_tag}Cheat has been activated!")
    else:
        raise Exception(f"{log_tags['error']}Unknown cheat: '{cheat}'")
