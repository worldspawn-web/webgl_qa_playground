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

start_app("com.android.chrome")

first_block_success = False

try:
    if exists(Template(r"tpl1737026725431.png", record_pos=(-0.126, -0.565), resolution=(1080, 2340))):
        touch(Template(r"tpl1737021940232.png", record_pos=(-0.131, -0.571), resolution=(1080, 2340)))
        sleep(3.0)
        text("https://yandex.ru/games/app/359422?lang=ru")
    else:
        touch(Template(r"tpl1737030756465.png", record_pos=(-0.128, -0.569), resolution=(1080, 2340)))
        sleep(3.0)
        text("https://yandex.ru/games/app/359422?lang=ru")
except:
    
    try:
        if exists(Template(r"tpl1737026546455.png", record_pos=(0.435, -0.935), resolution=(1080, 2340))):
            touch(Template(r"tpl1737026546455.png", record_pos=(0.435, -0.935), resolution=(1080, 2340)))
            sleep(3.0)

        if exists(Template(r"tpl1737026662468.png", record_pos=(0.152, -0.411), resolution=(1080, 2340))):
            touch(Template(r"tpl1737026662468.png", record_pos=(0.152, -0.411), resolution=(1080, 2340)))
        else:
            touch(Template(r"tpl1737030587463.png", record_pos=(0.143, -0.407), resolution=(1080, 2340)))

        sleep(3.0)

        if exists(Template(r"tpl1737026684077.png", record_pos=(-0.005, -0.026), resolution=(1080, 2340))):
            assert_exists(Template(r"tpl1737026684077.png", record_pos=(-0.005, -0.026), resolution=(1080, 2340)), "Please fill in the test point.")
        else:
            assert_exists(Template(r"tpl1737030622610.png", record_pos=(-0.001, -0.024), resolution=(1080, 2340)), "Please fill in the test point.")

        sleep(3.0)

        if exists(Template(r"tpl1737026690879.png", record_pos=(0.227, 0.494), resolution=(1080, 2340))):
            touch(Template(r"tpl1737026690879.png", record_pos=(0.227, 0.494), resolution=(1080, 2340)))
        else:
            touch(Template(r"tpl1737030677064.png", record_pos=(0.218, 0.494), resolution=(1080, 2340)))

        sleep(3.0)

        if exists(Template(r"tpl1737026711239.png", record_pos=(-0.426, -0.937), resolution=(1080, 2340))):
            touch(Template(r"tpl1737026711239.png", record_pos=(-0.426, -0.937), resolution=(1080, 2340)))
        else:
            touch(Template(r"tpl1737030724835.png", record_pos=(-0.426, -0.939), resolution=(1080, 2340)))

        sleep(3.0)

        if exists(Template(r"tpl1737026916816.png", record_pos=(-0.113, -0.565), resolution=(1080, 2340))):
            assert_exists(Template(r"tpl1737026916816.png", record_pos=(-0.113, -0.565), resolution=(1080, 2340)), "Please fill in the test point.")
        else:
            assert_exists(Template(r"tpl1737030769251.png", record_pos=(-0.109, -0.556), resolution=(1080, 2340)), "Please fill in the test point.")

        sleep(3.0)

        if exists(Template(r"tpl1737021940232.png", record_pos=(-0.131, -0.571), resolution=(1080, 2340))):
            touch(Template(r"tpl1737021940232.png", record_pos=(-0.131, -0.571), resolution=(1080, 2340)))
        else:
            touch(Template(r"tpl1737030804015.png", record_pos=(-0.118, -0.557), resolution=(1080, 2340)))
            text("https://yandex.ru/games/app/359422?lang=ru")
    except:
        pass

assert_exists(Template(r"tpl1737106144850.png", record_pos=(0.416, -0.795), resolution=(1080, 2340)), "Please fill in the test point.")
touch(Template(r"tpl1737106151185.png", record_pos=(0.428, -0.806), resolution=(1080, 2340)))
assert_exists(Template(r"tpl1737106168601.png", record_pos=(0.003, 0.74), resolution=(1080, 2340)), "Please fill in the test point.")
touch(Template(r"tpl1737106174493.png", record_pos=(0.008, 0.736), resolution=(1080, 2340)))
assert_exists(Template(r"tpl1737106251164.png", record_pos=(0.044, 0.007), resolution=(2340, 1080)), "Please fill in the test point.")

