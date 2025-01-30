# -*- encoding=utf8 -*-
from airtest.core.api import *
import logging

auto_setup(__file__)

def random_touch(n = 1):
    for i in range(n):
        touch((0.5, 0.5))
        sleep(1.5)

def dialog_skip(n = 1):
    for i in range(n):
        special_touch("mid", True)
        special_touch("mid", True) # skips dialog animation

def special_touch(coord, noad = False):
    NOAD_OFFSET = 0.08
    
    xyz = {
     "mid": (0.5, 0.5),
     "side": (0.85, 0.5), # right side
    }
    
    x, y = xyz[coord]
    
    if not noad:
        x -= NOAD_OFFSET
        
    touch((x, y))
    sleep(0.5)
    
def inter_check():
    inters = [
        Template(r"tpl1737996707427.png", record_pos=(0.467, -0.201), resolution=(2400, 1080)),
        Template(r"tpl1738059416652.png", rgb=True, record_pos=(0.48, 0.152), resolution=(2400, 1080)),
        Template(r"tpl1738253397425.png", record_pos=(0.427, 0.152), resolution=(2400, 1080)),
        Template(r"tpl1738062145169.png", rgb=True, target_pos=8, record_pos=(0.043, 0.004), resolution=(2400, 1080)),
        Template(r"tpl1738062158043.png", rgb=True, target_pos=8, record_pos=(0.044, -0.005), resolution=(2400, 1080)),
        Template(r"tpl1738062183836.png", rgb=True, target_pos=8, record_pos=(0.043, 0.004), resolution=(2400, 1080)),
        Template(r"tpl1738062207685.png", rgb=True, target_pos=8, record_pos=(0.045, 0.005), resolution=(2400, 1080))
    ]
    
    for inter in inters:
        if exists(inter):
            touch(inter)
            break

def close_window(noads = False):
    templates = [
        Template(r"tpl1737994827349.png", record_pos=(0.098, -0.105), resolution=(2400, 1080)),
        Template(r"tpl1738079004321.png", record_pos=(0.065, -0.062), resolution=(2400, 1080)),
        Template(r"tpl1738080024744.png", record_pos=(0.426, -0.101), resolution=(2400, 1080))
    ]
    
    for _ in range(2):
        cross_found = False
        for cross in templates:
            if exists(cross):
                touch(cross)
                
                if not noads:
                    inter_check()
                    
                return True
        if not cross_found:
            sleep(0.5)
    
    return False

def assert_and_touch(img, note):
    assert_exists(img, note)
    touch(img)
    sleep(0.5)
    
def yandex_pay(btn, noads = False):
    buy_btn = Template(r"tpl1738079835101.png", record_pos=(-0.009, 0.083), resolution=(2400, 1080))
    success_modal = Template(r"tpl1738079873923.png", target_pos=8, record_pos=(-0.006, 0.043), resolution=(2400, 1080))
    
    assert_and_touch(btn, "Purchase Offer Button.")
    wait(Template(r"tpl1738079659812.png", record_pos=(0.339, -0.037), resolution=(2400, 1080)))
    
    if not exists(Template(r"tpl1738079679053.png", record_pos=(-0.287, 0.206), resolution=(2400, 1080))):
        logging.error("QA Purchases are disabled! Turn it on manually to prevent money loss.")
    
    assert_and_touch(buy_btn, "Yandex Payment Button.")
    wait(success_modal)
    assert_and_touch(success_modal, "Payment succeded.")
    sleep(2.5)
    
    if not noads:
        inter_check()
        
    wait(Template(r"tpl1738241746902.png", record_pos=(-0.073, -0.029), resolution=(2400, 1080)))
    close_window(noads)
    
#                                       #
#   Checks for Leafs on the Screen      #
#   ------------------------------      #
#   It's an important regular check     #
#   since leaf timers are random        #
#   and they are blocking the view.     #
#                                       #
#   The best decision I came up with    #
#   is tapping every leaf we see.       #
#   Note: we still can't check drops    #

def leafs_checker():
    universal_leaf = Template(r"tpl1738236310604.png", record_pos=(-0.026, -0.023), resolution=(2400, 1080))
    
    while exists(universal_leaf):
        touch(universal_leaf)
        sleep(0.3)
        
def reload_page(fs = True):
    if fs:
        assert_and_touch(Template(r"tpl1738235196505.png", rgb=True, record_pos=(-0.436, -0.202), resolution=(2400, 1080)), "Exit Fullscreen Mode.")
    
    assert_and_touch(Template(r"tpl1738235389865.png", rgb=True, target_pos=6, record_pos=(0.356, -0.158), resolution=(2400, 1080)), "Browser Panel (Settings).")
    assert_and_touch(Template(r"tpl1738235428774.png", rgb=True, target_pos=6, record_pos=(0.349, -0.152), resolution=(2400, 1080)), "Reload Page.")
    
    wait(Template(r"tpl1738235490644.png", record_pos=(0.412, -0.1), resolution=(2400, 1080)))
    inter_check()
    sleep(6.0)
    assert_and_touch(Template(r"tpl1738236758454.png", record_pos=(-0.434, -0.097), resolution=(2400, 1080)), "Enter Fullscreen Mode.")
    
#                                               #
#   Touches Selected Generator Until Player:    #
#   - has no energy left                        #
#   - has no selected generators left           #
#                                               #

def use_generators(color):
    generators = {
        "blue": [
            Template(r"tpl1738237396669.png", threshold=0.65, rgb=True, record_pos=(0.069, -0.007), resolution=(2400, 1080)),
            Template(r"tpl1738239092514.png", rgb=True, record_pos=(0.044, 0.102), resolution=(2400, 1080)),
            Template(r"tpl1738255361048.png", rgb=True, record_pos=(0.009, -0.004), resolution=(2400, 1080)),
        ],
        "dark_blue": [],
        # ....
    }
    
    errors = {
        "blue": Template(r"tpl1738239340355.png", rgb=True, record_pos=(-0.134, 0.042), resolution=(2400, 1080)),
        "dark_blue": Template(r"tpl1738239340355.png", rgb=True, record_pos=(-0.134, 0.042), resolution=(2400, 1080))
    }
    
    gen_energy = Template(r"tpl1738237465752.png", record_pos=(0.072, -0.05), resolution=(2400, 1080))
    
    while True:
        generator_found = False
        energy_found = False
        
        if exists(Template(r"tpl1738255561230.png", record_pos=(-0.101, 0.004), resolution=(2400, 1080))):
            close_window(noads=True)
            return
        
        for generator in generators[color]:
            if exists(generator):
                touch(generator)
                sleep(0.5)
                generator_found = True
                break
                
        if exists(gen_energy):
            while exists(gen_energy):
                touch(gen_energy)
                sleep(0.5)
            energy_found = True
            
        if exists(errors[color]):
            return
                
        if not generator_found and not energy_found:
            print("Haven't found anything...")
            return

def goto(scene):
     # Go back to Main Scene -> Magic Forest
    train_btn = Template(r"tpl1738259382782.png", record_pos=(0.454, 0.172), resolution=(2400, 1080))
    destination = {
        "main": Template(r"tpl1738259443754.png", target_pos=8, record_pos=(-0.136, 0.007), resolution=(2400, 1080)),
        "forest": Template(r"tpl1738259493524.png", target_pos=8, record_pos=(0.042, 0.01), resolution=(2400, 1080)),
        "dragon": Template(r"tpl1738259608185.png", target_pos=8, record_pos=(0.22, 0.05), resolution=(2400, 1080))
    }
    

    assert_and_touch(train_btn, "Train Button Exists.")
    sleep(1.0)
    touch(destination[scene])
    sleep(6.0)
    wait(train_btn, interval=5, timeout=120)
        
__all__ = ['special_touch', 'inter_check', 'close_window', 'assert_and_touch', 'random_touch', 'dialog_skip', 'leafs_checker', 'reload_page', 'use_generators', 'goto']