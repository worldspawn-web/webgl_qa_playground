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
swipe(Template(r"tpl1736869933581.png", record_pos=(0.119, 0.047), resolution=(1080, 2400)), vector=[-0.1247, -0.0533])
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

# New Quest Appeared
sleep(6.0)
assert_exists(Template(r"tpl1736867990179.png", record_pos=(-0.014, 0.198), resolution=(1080, 2400)), "New Uncompleted Quest Apepared.")

# New Tutorial Dialog
wait(Template(r"tpl1736868008105.png", record_pos=(0.0, -0.038), resolution=(1080, 2400)))
touch(Template(r"tpl1736867990179.png", record_pos=(-0.019, 0.194), resolution=(1080, 2400)))

# Pointer to the Next Tutorial
wait(Template(r"tpl1736868161970.png", record_pos=(-0.001, -0.035), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736868171701.png", record_pos=(0.366, 0.678), resolution=(1080, 2400)), "Tutorial Finger after Quest Complete.")
touch(Template(r"tpl1736868171701.png", record_pos=(0.366, 0.68), resolution=(1080, 2400)))

wait(Template(r"tpl1736869076867.png", record_pos=(0.001, 0.053), resolution=(1080, 2400)))

# Tutorial Volume Toggler
assert_exists(Template(r"tpl1736869088108.png", record_pos=(0.202, -0.858), resolution=(1080, 2400)), "Volume toggler.")

# Multiple Generator Touch

for i in range(2):
    touch(Template(r"tpl1736869109559.png", record_pos=(0.119, 0.163), resolution=(1080, 2400)))

# Tutorial Merge
swipe(Template(r"tpl1736870144017.png", record_pos=(0.002, 0.044), resolution=(1080, 2400)), vector=[0.1174, 0.1142])
assert_exists(Template(r"tpl1736870175024.png", record_pos=(0.12, 0.283), resolution=(1080, 2400)), "Next Level Merge Item Appeared.")
swipe(Template(r"tpl1736870195012.png", record_pos=(0.119, 0.05), resolution=(1080, 2400)), vector=[-0.237, -0.0004])
assert_exists(Template(r"tpl1736870216885.png", record_pos=(-0.12, 0.047), resolution=(1080, 2400)), "Next Level Merge Item Appeared.")
swipe(Template(r"tpl1736870303672.png", record_pos=(0.118, 0.276), resolution=(1080, 2400)), vector=[-0.2283, -0.1021])
assert_exists(Template(r"tpl1736870321652.png", record_pos=(-0.118, 0.042), resolution=(1080, 2400)), "Next Level Merge Item Appeared.")
swipe(Template(r"tpl1736870321652.png", record_pos=(-0.119, 0.045), resolution=(1080, 2400)), vector=[0.1263, 0.0545])
assert_exists(Template(r"tpl1736870356992.png", record_pos=(0.003, 0.16), resolution=(1080, 2400)), "Next Level Merge Item Appeared - Green Glow")
assert_exists(Template(r"tpl1736870363772.png", record_pos=(0.357, 0.708), resolution=(1080, 2400)), "Pointer Back to the Main Scene")
touch(Template(r"tpl1736870363772.png", record_pos=(0.353, 0.708), resolution=(1080, 2400)))

# Reward for Completed Quest Tutorial
sleep(4.0)
wait(Template(r"tpl1736870425461.png", record_pos=(0.001, -0.039), resolution=(1080, 2400)))
touch(Template(r"tpl1736870457991.png", record_pos=(0.002, -0.034), resolution=(1080, 2400)))
wait(Template(r"tpl1736870476242.png", record_pos=(0.005, -0.105), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736870485315.png", record_pos=(-0.005, 0.314), resolution=(1080, 2400)), "Complete Button.")
touch(Template(r"tpl1736870485315.png", record_pos=(-0.003, 0.313), resolution=(1080, 2400)))

# New Tutorial Pointer
sleep (5.0)
wait(Template(r"tpl1736870526101.png", record_pos=(0.0, -0.04), resolution=(1080, 2400)))
touch(Template(r"tpl1736870571495.png", record_pos=(-0.186, 0.048), resolution=(1080, 2400)))
sleep(3.0)
assert_exists(Template(r"tpl1736870598061.png", record_pos=(0.366, 0.673), resolution=(1080, 2400)), "Pointer to the Merge Scene.")
touch(Template(r"tpl1736870598061.png", record_pos=(0.369, 0.681), resolution=(1080, 2400)))

# New Tutorial on Merge Field
wait(Template(r"tpl1736870663511.png", record_pos=(0.004, -0.098), resolution=(1080, 2400)))

for i in range(2):
    touch(Template(r"tpl1736870737643.png", record_pos=(0.122, 0.163), resolution=(1080, 2400)))

swipe(Template(r"tpl1736870816341.png", record_pos=(0.12, 0.037), resolution=(1080, 2400)), vector=[0.0015, 0.1712])
assert_exists(Template(r"tpl1736870836430.png", record_pos=(0.121, 0.406), resolution=(1080, 2400)), "Next Level Merge Item Appeared.")
swipe(Template(r"tpl1736870836430.png", record_pos=(0.122, 0.404), resolution=(1080, 2400)), vector=[-0.1153, -0.0526])
assert_exists(Template(r"tpl1736870878020.png", record_pos=(0.002, 0.285), resolution=(1080, 2400)), "Next Level Merge Item Appeared - Green Glow")
assert_exists(Template(r"tpl1736870885815.png", record_pos=(0.355, 0.706), resolution=(1080, 2400)), "Pointer to the Main Scene.")
touch(Template(r"tpl1736870885815.png", record_pos=(0.357, 0.705), resolution=(1080, 2400)))

# Reward for Completed Quest Tutorial No.2
wait(Template(r"tpl1736870929160.png", record_pos=(-0.002, -0.033), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736870959280.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)), "Completed Quest Icon")
touch(Template(r"tpl1736870959280.png", record_pos=(0.006, -0.032), resolution=(1080, 2400)))
wait(Template(r"tpl1736870995117.png", record_pos=(0.003, -0.096), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736871003800.png", record_pos=(0.001, -0.148), resolution=(1080, 2400)), "Required Item - Green Glow.")
assert_exists(Template(r"tpl1736871010500.png", record_pos=(0.003, 0.106), resolution=(1080, 2400)), "Reward for the Quest.")
assert_exists(Template(r"tpl1736871015640.png", record_pos=(-0.005, 0.308), resolution=(1080, 2400)), "Complete Button.")
touch(Template(r"tpl1736871015640.png", record_pos=(0.001, 0.302), resolution=(1080, 2400)))

# Angel Dialog Appearance
wait(Template(r"tpl1736871066245.png", record_pos=(-0.003, -0.038), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736871075380.png", record_pos=(0.362, -0.859), resolution=(1080, 2400)), "Skip Unnecessary Dialog Button.")
touch(Template(r"tpl1736871075380.png", record_pos=(0.362, -0.862), resolution=(1080, 2400)))

# Quest List Tutorial
wait(Template(r"tpl1736871115150.png", record_pos=(-0.002, -0.356), resolution=(1080, 2400)))
touch(Template(r"tpl1736871115150.png", record_pos=(0.007, -0.607), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736871169202.png", record_pos=(-0.387, 0.703), resolution=(1080, 2400)), "Pointer to the Quest Window.")
touch(Template(r"tpl1736871169202.png", record_pos=(-0.399, 0.699), resolution=(1080, 2400)))
wait(Template(r"tpl1736871195379.png", record_pos=(0.003, -0.037), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736871209723.png", record_pos=(-0.157, -0.334), resolution=(1080, 2400)), "Required Item for the Quest.")
assert_exists(Template(r"tpl1736871215329.png", record_pos=(0.195, -0.36), resolution=(1080, 2400)), "Show Quest Location Button.")
touch(Template(r"tpl1736871215329.png", record_pos=(0.201, -0.366), resolution=(1080, 2400)))
wait(Template(r"tpl1736871249038.png", record_pos=(-0.002, -0.038), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736871258021.png", record_pos=(0.01, -0.007), resolution=(1080, 2400)), "Pointer to the Uncompleted Quest.")
touch(Template(r"tpl1736871258021.png", record_pos=(0.005, -0.031), resolution=(1080, 2400)))
wait(Template(r"tpl1736871285899.png", record_pos=(-0.006, -0.083), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1736871294282.png", record_pos=(0.006, 0.109), resolution=(1080, 2400)), "Rewards for the Uncompleted Quest.")
assert_exists(Template(r"tpl1736871302609.png", record_pos=(0.001, 0.318), resolution=(1080, 2400)), "Play Button.")
touch(Template(r"tpl1736871302609.png", record_pos=(-0.004, 0.319), resolution=(1080, 2400)))
wait(Template(r"tpl1736871598388.png", record_pos=(0.001, -0.073), resolution=(1080, 2400)))

