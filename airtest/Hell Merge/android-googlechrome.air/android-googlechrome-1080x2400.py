# -*- encoding=utf8 -*-
# pylint: disable-all

__author__ = "Michael 'Worldspawn' Lozickii"

from airtest.core.api import *
auto_setup(__file__)

# Start Test Window: Empty Google Page with no url
# Mode: Incognito (No Yandex Profile)


# Hell Merge - Yandex (RU)
touch(Template(r"tpl1736852394461.png", record_pos=(-0.094, -0.442), resolution=(1080, 2400)))
text("https://yandex.ru/games/app/359515?lang=ru")
keyevent("ENTER")

# Close Entry Interstitial
sleep(5.0)
touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))

# Loading Screen Banner
sleep(4.0)
wait(Template(r"tpl1736852660900.png", record_pos=(0.032, -0.508), resolution=(1080, 2400)))

# First Tutorial Window
sleep(10.0)
wait(Template(r"tpl1736852766557.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736852766557.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)), "First Tutorial Window.")


