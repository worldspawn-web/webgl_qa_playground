# -*- encoding=utf8 -*-
# pylint: disable-all

__author__ = "Michael 'Worldspawn' Lozickii"

from airtest.core.api import *
auto_setup(__file__)

# (TODO: REFACTOR WITH start_app cmd)
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

# Merge Tutorial Items
swipe(Template(r"tpl1736866208284.png", record_pos=(-0.001, 0.047), resolution=(1080, 2400)), vector=[0.1515, 0.002])
assert_exists(Template(r"tpl1736866406138.png", record_pos=(0.004, 0.05), resolution=(1080, 2400)), "Updated Merge Row.")
swipe(Template(r"tpl1736866460503.png", record_pos=(-0.12, 0.041), resolution=(1080, 2400)), vector=[0.2475, 0.0037])
assert_exists(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.043), resolution=(1080, 2400)), "Selected New Item.")
swipe(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.045), resolution=(1080, 2400)), vector=[0.0041, 0.0593])
assert_exists(Template(r"tpl1736866754994.png", record_pos=(0.116, 0.163), resolution=(1080, 2400)), "Tutorial Generator Appeared.")

# Multiple Generator Taps
for i in range(2):
    touch(Template(r"tpl1736866754994.png"))
    
# Merge Tutorial Items
    
assert_exists(Template(r"tpl1736867650921.png", record_pos=(-0.003, 0.042), resolution=(1080, 2400)), "Mask appeared.")
swipe(Template(r"tpl1736867667174.png", record_pos=(0.001, 0.045), resolution=(1080, 2400)), vector=[0.0007, -0.0501])
assert_exists(Template(r"tpl1736867693623.png", record_pos=(0.0, -0.08), resolution=(1080, 2400)), "Mask upgraded.")
swipe(Template(r"tpl1736867693623.png", record_pos=(0.001, -0.076), resolution=(1080, 2400)), vector=[-0.1221, 0.1115])
assert_exists(Template(r"tpl1736867759189.png", record_pos=(-0.122, 0.165), resolution=(1080, 2400)), "Gloves appeared - Green Glow.")

# Tutorial Return to Main Scene
assert_exists(Template(r"tpl1736867781677.png", record_pos=(0.351, 0.706), resolution=(1080, 2400)), "Tutorial Pointer to Main Scene.")
touch(Template(r"tpl1736867781677.png", record_pos=(0.351, 0.706), resolution=(1080, 2400)))

wait(Template(r"tpl1736867862490.png", record_pos=(-0.004, -0.034), resolution=(1080, 2400)))
touch(Template(r"tpl1736867872722.png", record_pos=(0.087, 0.219), resolution=(1080, 2400)))

# Complete Quest in a Modal Window
sleep(2.0)
touch(Template(r"tpl1736867872722.png", record_pos=(0.087, 0.219), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736867928344.png", record_pos=(0.005, 0.314), resolution=(1080, 2400)), "Modal Quest Window with a Button.")
touch(Template(r"tpl1736867928344.png", record_pos=(0.001, 0.309), resolution=(1080, 2400)))

# Dialog Before new Tutorial
sleep(6.0)
assert_exists(Template(r"tpl1736867990179.png", record_pos=(-0.014, 0.198), resolution=(1080, 2400)), "New Uncompleted Quest Apepared.")
wait(Template(r"tpl1736868008105.png", record_pos=(0.0, -0.038), resolution=(1080, 2400)))
touch(Template(r"tpl1736867990179.png", record_pos=(-0.019, 0.194), resolution=(1080, 2400)))

wait(Template(r"tpl1736868161970.png", record_pos=(-0.001, -0.035), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736868171701.png", record_pos=(0.366, 0.678), resolution=(1080, 2400)), "Tutorial Finger after Quest Complete.")
touch(Template(r"tpl1736868171701.png", record_pos=(0.366, 0.68), resolution=(1080, 2400)))

