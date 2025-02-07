__author__ = "syndi"
from airtest.core.api import *
auto_setup(__file__)

def exists_and_touch(img, time, note): 
    if assert_exists(img, note):
        touch(img)
        sleep(time)

def red_cross_check(starting=False):
    red_crosses = [
        Template(r"tpl1738670764424.png", record_pos=(0.176, -0.152), resolution=(2340, 1080))
    ]

    if starting:
        exists(red_crosses[0])  

    for cross in red_crosses:
        if exists(cross):
            touch(cross)
            break 