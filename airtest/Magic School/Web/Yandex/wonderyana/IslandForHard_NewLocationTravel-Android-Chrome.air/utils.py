__author__ = "syndi"
from airtest.core.api import *
auto_setup(__file__)

def exists_and_touch(img, time, note): 
    if assert_exists(img, note):
        touch(img)
        sleep(time)

def cross_check(starting=False):
    crosses = [
        Template(r"tpl1738670764424.png", record_pos=(0.176, -0.152), resolution=(2340, 1080))
    ]

    if starting:
        exists(crosses[0])

    for cross in crosses:
        if exists(cross):  
            touch(cross)
            break 

def inter_check(starting=False):
    crosses = [
        Template(r"tpl1738829833784.png", record_pos=(0.465, -0.2), resolution=(2340, 1080))
    ]

    if starting:
        exists(crosses[0])

    for cross in crosses:
        if exists(cross):
            touch(cross)
            break


   