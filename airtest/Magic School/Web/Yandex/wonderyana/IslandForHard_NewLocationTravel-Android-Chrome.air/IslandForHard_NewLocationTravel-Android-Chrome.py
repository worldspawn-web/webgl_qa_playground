# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Main Location
# Use json file "NewLocationTravel" from the folder
# Version: 1.6.14
__author__ = "syndi"

import logging
from airtest.core.api import *
from utils import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

def main():
    touch(Template(r"tpl1738939578138.png", record_pos=(0.272, -0.151), resolution=(2340, 1080)))
    
    cross_check()
    cross_check()
    cross_check()

    swipe((0.384, 0.715), (0.649, 0.594))

    
    island_for_hard = Template(r"tpl1738933977547.png", record_pos=(-0.029, 0.112), resolution=(2340, 1080))
    exists_and_touch(island_for_hard, 2, "Остров за харду")
    
    
    buy_button = Template(r"tpl1738935995565.png", record_pos=(-0.041, 0.149), resolution=(2340, 1080))
    exists_and_touch(buy_button, 2, "Кнопка покупки")
    
    
    assert_exists(Template(r"tpl1738936529629.png", record_pos=(-0.044, 0.048), resolution=(2340, 1080)), "Остров за харду")
    
    travel_icon = Template(r"tpl1738591864974.png", threshold=0.65, record_pos=(0.264, 0.185), resolution=(2340, 1080))
    exists_and_touch(travel_icon, 2, "Иконка перемещения")
    
    magic_forest_icon = Template(r"tpl1738592754372.png", target_pos = 8, record_pos=(-0.053, 0.009), resolution=(2340, 1080))

    exists_and_touch(magic_forest_icon, 2, "Кнопка перехода магического леса")

    sleep(2.0)
    
    inter_check()

    assert_exists(Template(r"tpl1740055071313.png", record_pos=(0.266, 0.116), resolution=(2340, 1080)), "Иконка обмена в МС")
      
    swipe((0.658, 0.418), (0.633, 0.445))
    swipe((0.552, 0.463), (0.53, 0.513)) 

if __name__ == "__main__":
    main()