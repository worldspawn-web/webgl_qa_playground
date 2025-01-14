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

# Skip Dialog
touch(Template(r"tpl1736858679598.png", record_pos=(0.324, -0.858), resolution=(1080, 2400)))
sleep(7.0)
touch(Template(r"tpl1736858679598.png", record_pos=(0.324, -0.858), resolution=(1080, 2400)))

# Touch before Tutorial Pointer
sleep(7.0)
wait(Template(r"tpl1736858768883.png", record_pos=(-0.005, -0.041), resolution=(1080, 2400)))
touch(Template(r"tpl1736858777773.png", record_pos=(0.002, -0.025), resolution=(1080, 2400)))

# Tutorial Pointer
sleep(5.0)
assert_exists(Template(r"tpl1736858804654.png", record_pos=(0.369, 0.688), resolution=(1080, 2400)), "Tutorial Finger")
touch(Template(r"tpl1736858804654.png", record_pos=(0.369, 0.688), resolution=(1080, 2400)))

# Merge Field Exists
sleep(5.0)
assert_exists(Template(r"tpl1736858868805.png", record_pos=(0.001, 0.051), resolution=(1080, 2400)), "Merge Field")
