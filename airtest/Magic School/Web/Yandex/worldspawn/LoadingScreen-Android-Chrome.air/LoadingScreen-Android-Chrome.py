# -*- encoding=utf8 -*-
# ! CLEAR CACHE & DEAUTHORIZE FROM YANDEX BEFORE RUNNING !
#

# Device: Redmi Note 13 (1080x2400)
# System Lang: English
# Browser: Chrome - Light Version - Russian Language
# System: MIUI - Light Version - Russian Language

from airtest.core.api import *
import logging

auto_setup(__file__)

def assert_and_touch(img, note):
    assert_exists(img, note)
    touch(img)
    sleep(1.0)

def clear_cache():
    remove_data_btn = Template(r"tpl1738162915831.png", rgb=True, record_pos=(0.206, 0.592), resolution=(1080, 2400))
    
    settings_list = [
        Template(r"tpl1738163624598.png", target_pos=6, record_pos=(0.353, -0.155), resolution=(2400, 1080)), # horizontal
        Template(r"tpl1738162770322.png", rgb=True, record_pos=(0.442, -0.955), resolution=(1080, 2400)) # vertical
    ]
    
    for settings in settings_list:
        if exists(settings):
            touch(settings)
            break
            
    assert_and_touch(Template(r"tpl1738162876914.png", record_pos=(0.156, -0.434), resolution=(1080, 2400)), "Clear Cache Button.")
    wait(remove_data_btn)
    assert_and_touch(remove_data_btn, "Remove Data Button.")
    assert_and_touch(Template(r"tpl1738163807907.png", record_pos=(-0.428, -0.156), resolution=(2400, 1080)), "New Window Button.")



def game_launch(field, url):
    assert_and_touch(field, "Browser Search Field.")
    text(url)
    
def inter_check(start = False):
    templates = [
        Template(r"tpl1738163148883.png", record_pos=(0.467, -0.201), resolution=(2400, 1080))
    ]
    
    if (start == True):
        wait(Template(r"tpl1738163148883.png", record_pos=(0.467, -0.201), resolution=(2400, 1080)))
    
    for inter in templates:
        if exists(inter):
            touch(inter)
            break
            
def loading_checks():
    banner_logo = Template(r"tpl1738163369569.png", record_pos=(0.024, -0.038), resolution=(2400, 1080))
    assert_exists(Template(r"tpl1738163391631.png", threshold=0.5, rgb=True, record_pos=(0.013, 0.178), resolution=(2400, 1080)), "Loading Progress Bar.")
    
    wait(banner_logo)
    assert_exists(banner_logo, "Loading Image.")
    assert_exists(Template(r"tpl1738163449339.png", threshold=0.6, rgb=True, record_pos=(0.209, 0.211), resolution=(2400, 1080)), "Loading Version.")


#                   #
#   Main Function   #
#                   #

def main():
    # Global Variables
    game_url = "https://yandex.ru/games/app/359422?lang=ru"
    search_field = Template(r"tpl1738162984061.png", record_pos=(0.0, -0.589), resolution=(1080, 2400))

    # Actions
    clear_cache()
    game_launch(search_field, game_url)
    inter_check(True)
    loading_checks()

    
if __name__ == "__main__":
    main()