# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Main Location
# Use json file "NewLocationTravel" from the folder
# Version: 1.1.7

__author__ = "syndi"

import logging
from airtest.core.api import *
from utils import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

def main():
    travel_icon = Template(r"tpl1738591864974.png", threshold=0.65, record_pos=(0.264, 0.185), resolution=(2340, 1080))
    exists_and_touch(travel_icon, 2, "Иконка перемещения")
    
    magic_forest_icon = Template(r"tpl1738592754372.png", target_pos = 8, record_pos=(-0.053, 0.009), resolution=(2340, 1080))

    exists_and_touch(magic_forest_icon, 2, "Кнопка перехода магического леса")

    inter_check()
    
    assert_exists(Template(r"tpl1738592868339.png", record_pos=(-0.255, 0.012), resolution=(2340, 1080)), "Элафир")

if __name__ == "__main__":
    main()