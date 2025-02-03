# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Main Location
# Use json file "EnergyForSoftLvl6" from the folder
# Version: 1.1.7

__author__ = "syndi"

import logging
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

def exists_and_touch(img): 
    if exists(img):
        touch(img)    

def inter_check(starting=False):
    crosses = [
        Template(r"tpl1738326058621.png", record_pos=(0.466, -0.206), resolution=(2340, 1080))
    ]

    if starting:
        if exists(crosses[0]):  
            wait(crosses[0], timeout=15) 
        else:
            return

    for cross in crosses:
        if exists(cross):
            touch(cross)
            break

def assert_energy_changed(before_img, after_img):
    energy_before_image = exists(before_img)
    energy_after_image = exists(after_img)

    assert_not_equal(energy_before_image, energy_after_image)

def main():  
    
    energy_before = Template(r"tpl1738324204149.png", record_pos=(-0.297, -0.209), resolution=(2340, 1080))
    assert_exists(energy_before, "Энергия до покупки за софту")

    
    img_energy = Template(r"tpl1738324094076.png", threshold=0.65, rgb=True, target_pos=6, record_pos=(-0.279, -0.209), resolution=(2340, 1080))
    exists_and_touch(img_energy)

    sleep(2)    

    
    assert_exists(Template(r"tpl1738244543212.png", record_pos=(-0.084, 0.0), resolution=(2340, 1080)), "Окно покупки энергии")
    
    buy_button = Template(r"tpl1738244600065.png", rgb=True, record_pos=(-0.088, 0.109), resolution=(2340, 1080))
    exists_and_touch(buy_button)

    
    touch(Template(r"tpl1738324278265.png", record_pos=(0.23, -0.136), resolution=(2340, 1080)))
    
    inter_check()
    
    energy_after = Template(r"tpl1738328593395.png", record_pos=(-0.3, -0.211), resolution=(2340, 1080))
     
    assert_energy_changed(energy_before, energy_after)

if __name__ == "__main__":
    main()
