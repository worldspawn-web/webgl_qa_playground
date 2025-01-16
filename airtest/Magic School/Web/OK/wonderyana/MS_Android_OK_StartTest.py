# -*- encoding=utf8 -*-
__author__ = "syndi"

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *

auto_setup(__file__)
start_app("ru.ok.android")
touch(Template(r"tpl1736937321898.png", record_pos=(0.428, 0.897), resolution=(1080, 2340)))
touch(Template(r"tpl1736937339070.png", record_pos=(0.346, 0.006), resolution=(1080, 2340)))
touch(Template(r"tpl1736926498599.png", record_pos=(-0.392, 0.521), resolution=(1080, 2340)))

assert_exists(Template(r"tpl1736926513565.png", record_pos=(0.016, 0.004), resolution=(2340, 1080)), "Please fill in the test point.")
wait(Template(r"tpl1736927303549.png", record_pos=(0.012, -0.118), resolution=(2340, 1080)))

if exists(Template(r"tpl1736926751289.png", record_pos=(0.003, -0.007), resolution=(2340, 1080))):
    assert_exists(Template(r"tpl1736926689512.png", record_pos=(0.009, -0.012), resolution=(2340, 1080)), "Please fill in the test point.")
else:
    wait(Template(r"tpl1736939018013.png", record_pos=(-0.122, 0.154), resolution=(2340, 1080)))
    assert_exists(Template(r"tpl1736939311425.png", record_pos=(-0.118, 0.152), resolution=(2340, 1080)), "Please fill in the test point.")

