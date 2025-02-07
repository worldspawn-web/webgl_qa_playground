# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Main Location
# Use json file "20thLevel" from the folder
# Version: 1.1.7

__author__ = "syndi"

import logging
from airtest.core.api import *
from utils import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

def main():
    
    touch(Template(r"tpl1738939578138.png", record_pos=(0.272, -0.151), resolution=(2340, 1080)))
    
    red_cross_check()
    
    swipe((0.384, 0.715), (0.649, 0.594))

    
    island_for_hard = Template(r"tpl1738933977547.png", record_pos=(-0.029, 0.112), resolution=(2340, 1080))
    exists_and_touch(island_for_hard, 2, "Остров за харду")
    
    
    buy_button = Template(r"tpl1738935995565.png", record_pos=(-0.041, 0.149), resolution=(2340, 1080))
    exists_and_touch(buy_button, 2, "Кнопка покупки")
    
    
    assert_exists(Template(r"tpl1738936529629.png", record_pos=(-0.044, 0.048), resolution=(2340, 1080)), "Остров за харду")

if __name__ == "__main__":
    main()