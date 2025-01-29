# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Empty Google Page
# Version: 1.1.7

__author__ = "syndi"

import logging
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

auto_setup(__file__)
start_app("com.android.chrome")

if exists(Template(r"tpl1738073032776.png", record_pos=(0.432, -0.948), resolution=(1080, 2340))):
    touch(Template(r"tpl1738073032776.png", record_pos=(0.432, -0.948), resolution=(1080, 2340)))
    if exists(Template(r"tpl1738073080861.png", record_pos=(0.168, -0.688), resolution=(1080, 2340))):
        touch(Template(r"tpl1738073080861.png", record_pos=(0.168, -0.688), resolution=(1080, 2340)))

if exists(Template(r"tpl1738072833855.png", record_pos=(-0.065, -0.945), resolution=(1080, 2340))):
    touch(Template(r"tpl1738072833855.png", record_pos=(-0.065, -0.945), resolution=(1080, 2340)))
    sleep(3.0)
    text("https://yandex.ru/games/app/359422?lang=ru")

assert_exists(Template(r"tpl1737106168601.png", record_pos=(0.003, 0.74), resolution=(1080, 2340)), "Please fill in the test point.")
touch(Template(r"tpl1737106174493.png", record_pos=(0.008, 0.736), resolution=(1080, 2340)))

wait(Template(r"tpl1738074176756.png", record_pos=(0.463, -0.201), resolution=(2340, 1080)))

if exists(Template(r"tpl1738073532964.png", record_pos=(0.464, -0.204), resolution=(2340, 1080))):
    touch(Template(r"tpl1738073532964.png", record_pos=(0.464, -0.204), resolution=(2340, 1080)))

assert_exists(Template(r"tpl1738148391338.png", record_pos=(0.039, -0.002), resolution=(2340, 1080)), "Please fill in the test point.")

sleep(7.0)

wait(Template(r"tpl1738071922510.png", record_pos=(0.03, -0.03), resolution=(2340, 1080)))

assert_exists(Template(r"tpl1738071922510.png", record_pos=(0.03, -0.03), resolution=(2340, 1080)), "Please fill in the test point.") or \
assert_exists(Template(r"tpl1738072079270.png", record_pos=(0.002, -0.11), resolution=(2340, 1080)), "Please fill in the test point.")

assert_exists(Template(r"tpl1738071758047.png", record_pos=(0.024, 0.194), resolution=(2340, 1080)), "Please fill in the test point.")
assert_exists(Template(r"tpl1738149589491.png", record_pos=(0.147, 0.209), resolution=(2340, 1080)), "Please fill in the test point.")

# ждусь исправлений