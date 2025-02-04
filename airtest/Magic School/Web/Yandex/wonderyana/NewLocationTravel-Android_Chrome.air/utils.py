__author__ = "syndi"

import logging
from airtest.core.api import *
auto_setup(__file__)

def exists_and_touch(img, time, note): 
    if exists(img):
        touch(img)
        sleep(time)

def inter_check(starting=False):
    crosses = [
        Template(r"tpl1738592308449.png", record_pos=(0.465, -0.2), resolution=(2340, 1080))
    ]

    if starting:
        exists(crosses[0])

    for cross in crosses:
        if exists(cross):
            touch(cross)
            break