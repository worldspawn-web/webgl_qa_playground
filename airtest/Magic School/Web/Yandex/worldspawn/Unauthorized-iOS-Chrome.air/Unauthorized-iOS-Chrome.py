# -*- encoding=utf8 -*-
__author__ = "Michael 'Worldspawn' Lozickii"

from airtest.core.api import *
import logging
import utils import (
    random_touch   
)

# Logger Setup
logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

auto_setup(__file__)

def main():
    # Conditions Check
    if not exists(Template(r"tpl1737990781606.png", record_pos=(-0.346, 0.177), resolution=(1792, 828))):
        logger.warning('Incorrect Test Start! Check starting conditions.')
    
    # Tutorial Assertions
    assert_exists(Template(r"tpl1737990863489.png", record_pos=(-0.069, 0.004), resolution=(1792, 828)), "Tutorial Item.")
    assert_exists(Template(r"tpl1737990896562.png", record_pos=(0.236, -0.111), resolution=(1792, 828)), "Volume Toggler.")
    assert_exists(Template(r"tpl1737990909839.png", record_pos=(-0.108, -0.109), resolution=(1792, 828)), "Locked Area.")
    # Uncomment if picture swipe is inconsistent
    # swipe((0.433, 0.516), (0.514, 0.429))
    # Can be broken
    swipe(Template(r"tpl1737990967327.png", record_pos=(-0.071, 0.0), resolution=(1792, 828)), vector=[0.0863, -0.0604])
    assert_exists(Template(r"tpl1737991686281.png", threshold=0.6, record_pos=(-0.072, -0.001), resolution=(1792, 828)), "Mascot Appeared on Field")
    assert_exists(Template(r"tpl1737991709421.png", record_pos=(-0.343, 0.175), resolution=(1792, 828)), "Mascot Dialog Avatar.")
    random_touch()
    
if __name__ == "__main__":
    main()
