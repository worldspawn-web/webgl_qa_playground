# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Main Location
# Use json file "MagicFosrestAppear" from the folder
# Version: 1.1.7

__author__ = "syndi"

import logging
from airtest.core.api import *
from utils import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

def main():
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