# -*- encoding=utf8 -*-

# Magic School (Yandex)
# Start Test Window: Empty Google Page
# Version: 1.1.7

__author__ = "syndi"

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
auto_setup(__file__)

# Шаблоны изображений
TPL_1 = Template(r"tpl1737026725431.png", record_pos=(-0.126, -0.565), resolution=(1080, 2340))
TPL_2 = Template(r"tpl1737021940232.png", record_pos=(-0.131, -0.571), resolution=(1080, 2340))
TPL_3 = Template(r"tpl1737030756465.png", record_pos=(-0.128, -0.569), resolution=(1080, 2340))
TPL_4 = Template(r"tpl1737026546455.png", record_pos=(0.435, -0.935), resolution=(1080, 2340))
TPL_5 = Template(r"tpl1737026662468.png", record_pos=(0.152, -0.411), resolution=(1080, 2340))
TPL_6 = Template(r"tpl1737030587463.png", record_pos=(0.143, -0.407), resolution=(1080, 2340))
TPL_7 = Template(r"tpl1737026684077.png", record_pos=(-0.005, -0.026), resolution=(1080, 2340))
TPL_8 = Template(r"tpl1737030622610.png", record_pos=(-0.001, -0.024), resolution=(1080, 2340))
TPL_9 = Template(r"tpl1737026690879.png", record_pos=(0.227, 0.494), resolution=(1080, 2340))
TPL_10 = Template(r"tpl1737030677064.png", record_pos=(0.218, 0.494), resolution=(1080, 2340))
TPL_11 = Template(r"tpl1737026711239.png", record_pos=(-0.426, -0.937), resolution=(1080, 2340))
TPL_12 = Template(r"tpl1737030724835.png", record_pos=(-0.426, -0.939), resolution=(1080, 2340))
TPL_13 = Template(r"tpl1737026916816.png", record_pos=(-0.113, -0.565), resolution=(1080, 2340))
TPL_14 = Template(r"tpl1737030769251.png", record_pos=(-0.109, -0.556), resolution=(1080, 2340))
TPL_15 = Template(r"tpl1737030804015.png", record_pos=(-0.118, -0.557), resolution=(1080, 2340))
TPL_16 = Template(r"tpl1737106144850.png", record_pos=(0.416, -0.795), resolution=(1080, 2340))
TPL_17 = Template(r"tpl1737106151185.png", record_pos=(0.428, -0.806), resolution=(1080, 2340))
TPL_18 = Template(r"tpl1737106168601.png", record_pos=(0.003, 0.74), resolution=(1080, 2340))
TPL_19 = Template(r"tpl1737106174493.png", record_pos=(0.008, 0.736), resolution=(1080, 2340))
TPL_20 = Template(r"tpl1737106251164.png", record_pos=(0.044, 0.007), resolution=(2340, 1080))


start_app("com.android.chrome")

try:
    if exists(TPL_1):
        touch(TPL_2)
        sleep(3.0)
        text("https://yandex.ru/games/app/359422?lang=ru")
    else:
        touch(TPL_3)
        sleep(3.0)
        text("https://yandex.ru/games/app/359422?lang=ru")
except:
    try:
        if exists(TPL_4):
            touch(TPL_4)
            sleep(3.0)

        if exists(TPL_5):
            touch(TPL_5)
        else:
            touch(TPL_6)

        sleep(3.0)

        if exists(TPL_7):
            assert_exists(TPL_7, "Please fill in the test point.")
        else:
            assert_exists(TPL_8, "Please fill in the test point.")

        sleep(3.0)

        if exists(TPL_9):
            touch(TPL_9)
        else:
            touch(TPL_10)

        sleep(3.0)

        if exists(TPL_11):
            touch(TPL_11)
        else:
            touch(TPL_12)

        sleep(3.0)

        if exists(TPL_13):
            assert_exists(TPL_13, "Please fill in the test point.")
        else:
            assert_exists(TPL_14, "Please fill in the test point.")

        sleep(3.0)

        if exists(TPL_2):
            touch(TPL_2)
        else:
            touch(TPL_15)

        
        text("https://yandex.ru/games/app/359422?lang=ru")
        sleep(3.0)
    except:
        pass

assert_exists(TPL_16, "Please fill in the test point.")
touch(TPL_17)
assert_exists(TPL_18, "Please fill in the test point.")
touch(TPL_19)
assert_exists(TPL_20, "Please fill in the test point.")