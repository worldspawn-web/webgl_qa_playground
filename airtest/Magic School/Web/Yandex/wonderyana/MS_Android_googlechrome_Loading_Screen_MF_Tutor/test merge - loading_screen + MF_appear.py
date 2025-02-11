# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Home screen
# Use json file "MagicFosrestAppear" from the folder
# Version: 1.6.14

__author__ = "syndi"

import logging
from airtest.core.api import *
from utils import *

game_url = "https://yandex.ru/games/app/359422?lang=ru"

def main():
    auto_setup(__file__)
    start_app("com.android.chrome")

    img_name_light = Template(r"tpl1738163458836.png", record_pos=(0.005, -0.579), resolution=(1080, 2340))
    img_name_dark = Template(r"tpl1738163566332.png", record_pos=(-0.011, -0.581), resolution=(1080, 2340))

    if exists_and_touch(img_name_light, 2, "Светлая тема"):
        text(game_url)
    else:
        exists_and_touch(img_name_dark, 2, "Темная тема")
        text(game_url)

    inter_check(True)

    ya_play_btn = Template(r"tpl1737106168601.png", record_pos=(0.003, 0.74), resolution=(1080, 2340))
    if exists(ya_play_btn):
        touch(ya_play_btn)

    sleep(2)    
    
    # Проверка экрана загрузки
    assert_exists(Template(r"tpl1738148391338.png", record_pos=(0.039, -0.002), resolution=(2340, 1080)), "Проверка наличия экрана загрузки.")
    assert_exists(Template(r"tpl1738071922510.png", record_pos=(0.03, -0.03), resolution=(2340, 1080)), "Проверка наличия лого рус.")
    assert_exists(Template(r"tpl1738160756396.png", threshold=0.6, rgb=True, record_pos=(0.012, 0.181), resolution=(2340, 1080)), "Проверка наличия прогресс-бара")
    assert_exists(Template(r"tpl1738149589491.png", threshold=0.6, rgb=True, record_pos=(0.147, 0.209), resolution=(2340, 1080)), "Проверка наличия версии билда.")

    sleep(3)
    
    assert_exists(Template(r"tpl1739274183598.png", record_pos=(-0.054, 0.017), resolution=(2340, 1080)), "Оффер с Эвелин.")
    
    sleep(3)
    
    touch((0.722, 0.193))
    
    sleep(3)
    
    # Проверка появления тутора на Волшебный Лес
    
    touch(Template(r"tpl1738670401183.png", record_pos=(-0.05, 0.054), resolution=(2340, 1080)))

    new_level = Template(r"tpl1738672705572.png", rgb=True, record_pos=(-0.091, -0.029), resolution=(2340, 1080))
    exists_and_touch(new_level, 2, "Новый уровень")

    inter_check()

    new_mission = Template(r"tpl1738831435689.png", record_pos=(-0.086, 0.021), resolution=(2340, 1080))
    exists_and_touch(new_mission, 2, "Новое задание")

    red_cross = Template(r"tpl1738670764424.png", record_pos=(0.176, -0.152), resolution=(2340, 1080))
    exists_and_touch(red_cross, 2, "Красный крест")

    inter_check()
    exists_and_touch(red_cross, 2, "Красный крест")

    inter_check()
    exists_and_touch(red_cross, 2, "Красный крест")

    inter_check()

    tutor_Ellaphir = Template(r"tpl1738670941099.png", record_pos=(-0.29, -0.01), resolution=(2340, 1080))
    exists_and_touch(tutor_Ellaphir, 2, "Туторный Эллафир")

    tutor_Evelyn = Template(r"tpl1738671067880.png", record_pos=(0.24, -0.02), resolution=(2340, 1080))
    exists_and_touch(tutor_Evelyn, 2, "Туторная Эвелин")

    repeat_touch(tutor_Ellaphir, 2, "Туторный Эллафир", 2)

    travel_icon = Template(r"tpl1738671145031.png", record_pos=(0.264, 0.182), resolution=(2340, 1080))
    exists_and_touch(travel_icon, 2, "Иконка перемещения")

    magic_forest_icon = Template(r"tpl1738671200436.png", target_pos=8, record_pos=(-0.053, 0.003), resolution=(2340, 1080))
    exists_and_touch(magic_forest_icon, 2, "Иконка магического леса")

    repeat_touch(tutor_Ellaphir, 2, "Туторный Эллафир", 4)

    assert_exists(Template(r"tpl1738671346678.png", record_pos=(-0.105, -0.026), resolution=(2340, 1080)), "Туторный указатель со спящими тельцами")

    swipe((0.388, 0.463), (0.411, 0.423))
    sleep(0.02)

    assert_exists(Template(r"tpl1738842755235.png", record_pos=(-0.051, -0.04), resolution=(2340, 1080)), "Туторный указатель с тельцами побольше")

    swipe((0.417, 0.409), (0.444, 0.391))
    sleep(0.02)

    assert_exists(Template(r"tpl1738744637780.png", record_pos=(-0.277, -0.012), resolution=(2340, 1080)), "Эллафир после мерджа")

if __name__ == "__main__":
    main()
