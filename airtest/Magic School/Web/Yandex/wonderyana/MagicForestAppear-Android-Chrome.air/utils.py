__author__ = "syndi"
from airtest.core.api import *
auto_setup(__file__)

def exists_and_touch(img, time, note): 
    if assert_exists(img, note):
        touch(img)
        sleep(time)
        
def exists_image(img, note):
    return assert_exists(img, note)
        
def inter_check(starting=False):
    crosses = [
        Template(r"tpl1738744401286.png", record_pos=(0.464, -0.201), resolution=(2340, 1080))
    ]

    if starting:
        exists(crosses[0])

    for cross in crosses:
        if exists(cross):
            touch(cross)
            break

def repeat_touch(img, time, note, count):
    for _ in range(count):
        exists_and_touch(img, time, note)