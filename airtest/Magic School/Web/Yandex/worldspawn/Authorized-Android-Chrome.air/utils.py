__author__ = "Michael 'Worldspawn' Lozickii"

from airtest.core.api import *
import logging
auto_setup(__file__)

def random_touch():
    touch((0.5, 0.5))
    sleep(1.0)
    
def multiple_touches(n):
    for i in range(n):
        random_touch()
        sleep(2.25)
        
def inter_check():
    inters = [
        Template(r"tpl1737996707427.png", record_pos=(0.467, -0.201), resolution=(2400, 1080)),
        Template(r"tpl1738059416652.png", rgb=True, record_pos=(0.48, 0.152), resolution=(2400, 1080)),
        Template(r"tpl1738062145169.png", rgb=True, target_pos=8, record_pos=(0.043, 0.004), resolution=(2400, 1080)),
        Template(r"tpl1738062158043.png", rgb=True, target_pos=8, record_pos=(0.044, -0.005), resolution=(2400, 1080)),
        Template(r"tpl1738062183836.png", rgb=True, target_pos=8, record_pos=(0.043, 0.004), resolution=(2400, 1080)),
        Template(r"tpl1738062207685.png", rgb=True, target_pos=8, record_pos=(0.045, 0.005), resolution=(2400, 1080))
    ]
    
    for inter in inters:
        if exists(inter):
            touch(inter)
            break
        
def close_window():
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
                inter_check()
                return True
        if not cross_found:
            sleep(0.5)
    
    return False

def assert_and_touch(func, note):
    assert_exists(func, note)
    touch(func)
    sleep(2.0)
    
def yandex_pay(btn):
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

__all__ = ['random_touch', 'multiple_touches', 'close_window', 'inter_check', 'assert_and_touch', 'yandex_pay']
