from airtest.core.api import *

# Functions
def random_touch():
    sleep(2.0)
    touch([500, 1020])

def fullscreen_window_check():
    window = Template(r"tpl1737976810731.png", target_pos=3, record_pos=(-0.005, -0.684), resolution=(828, 1792))
    if exists(window):
        touch(window)
        
def inter_check():
    templates = [
        Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)),
        Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400))
    ]
    
    sleep(3.0)
    
    for inter in templates:
        if exists(inter):
            touch(inter)
            break
            
__all__ = ['inter_check', 'fullscreen_window_check', 'random_touch']