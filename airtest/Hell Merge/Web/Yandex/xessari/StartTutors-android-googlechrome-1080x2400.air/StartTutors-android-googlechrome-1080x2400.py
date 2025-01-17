# -*- encoding=utf8 -*-

# Hell Merge (Yandex)
# Start Test Window: Empty Google Page
# Mode: Incognito (No Yandex Profile)
# Version: 1.1.7

__author__ = "Andrew 'Xessaki' Ivanov"

# Removes Debug Logs
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
auto_setup(__file__)

# Functions
#def random_touch():
   #sleep(2.0)
   #touch([500, 1020])

# Cache Reset Variations Class
class BrowserCacheVariation:
    def __init__(self, image, record_pos, resolution):
        self.image = image
        self.record_pos = record_pos
        self.resolution = resolution
        
# Cache Resets Variations Define
def init_browsers():
    browser1 = BrowserCacheVariation("tpl1736944115125.png", (0.297, -0.955), (1080, 2400)) # dark panel
    browser2 = BrowserCacheVariation("tpl1736945067386.png", (0.309, -0.954), (1080, 2400)) # white panel w/ no avatar
    browser3 = BrowserCacheVariation("tpl1736945298223.png", (0.18, -0.954), (1080, 2400)) # only settings (tab viewer)
    return [browser1, browser2, browser3]

def main():
    # Auto Cache Reset
    browsers = init_browsers()
    start_app("com.android.chrome")

    if not (exists(Template(r"tpl1736943901499.png", record_pos=(0.001, -0.693), resolution=(1080, 2400)))):
        for browser in browsers:
            if exists(Template(r"" + browser.image, record_pos=browser.record_pos, resolution=browser.resolution)):
                touch(Template(r"" + browser.image, record_pos=browser.record_pos, resolution=browser.resolution, target_pos=6))
                break

        touch(Template(r"tpl1736945440708.png", record_pos=(0.119, -0.432), resolution=(1080, 2400)))
        sleep(1.0)
        wait(Template(r"tpl1736945481294.png", record_pos=(0.28, 0.566), resolution=(1080, 2400)))
        touch(Template(r"tpl1736945481294.png", record_pos=(0.28, 0.566), resolution=(1080, 2400)))
        sleep(2.0)
        
        #Проверяем на отличие интерфейса Google Chrome
        if exists(Template(r"tpl1736945586374.png", record_pos=(-0.187, -0.956), resolution=(1080, 2400), target_pos=4)):
            touch(Template(r"tpl1737115278280.png", record_pos=(-0.43, -0.964), resolution=(1080, 2400)))
        else:
            touch(Template(r"tpl1737115294754.png", record_pos=(-0.431, -0.967), resolution=(1080, 2400)))


    # Hell Merge - Yandex (RU)
    sleep(2.0)
    touch(Template(r"tpl1736872552631.png", record_pos=(-0.167, -0.585), resolution=(1080, 2400)))
    text("https://yandex.ru/games/app/359515?lang=ru")
    keyevent("ENTER")

    sleep(2.0)
    if (exists(Template(r"tpl1736872631342.png", record_pos=(-0.004, 0.378), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872665536.png", record_pos=(0.001, 0.47), resolution=(1080, 2400)))

    # Close Entry Interstitial
    sleep(2.0)
    
    if (exists(Template(r"tpl1737118278396.png", record_pos=(0.401, -0.83), resolution=(1080, 2400)))):
        touch(Template(r"tpl1736872848834.png", record_pos=(0.42, -0.967), resolution=(1080, 2400)))
    #else:
        #touch(Template(r"tpl1736852577544.png", record_pos=(0.427, -0.967), resolution=(1080, 2400)))

    # Loading Screen Banner
    sleep(2.0)
    wait(Template(r"tpl1736852660900.png", record_pos=(0.032, -0.508), resolution=(1080, 2400)))

    # First Tutorial Window
    sleep(14.0)
    wait(Template(r"tpl1736852766557.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1736852766557.png", record_pos=(-0.002, -0.039), resolution=(1080, 2400)), "First Tutorial Window.")

    # Skip Dialogs
    for i in range(2):
        touch(Template(r"tpl1736858679598.png", record_pos=(0.324, -0.858), resolution=(1080, 2400)))
        sleep(8.0)

    # Touch before Tutorial Pointer
    wait(Template(r"tpl1736858768883.png", record_pos=(-0.005, -0.041), resolution=(1080, 2400)))
    sleep(2.0)
    touch((100, 100), times=1)

    # Tutorial Pointer
    sleep(4.0)
    assert_exists(Template(r"tpl1736858804654.png", record_pos=(0.369, 0.688), resolution=(1080, 2400)), "Tutorial Finger")
    touch(Template(r"tpl1736858804654.png", record_pos=(0.369, 0.688), resolution=(1080, 2400)))

    # Merge Field Exists
    sleep(5.0)
    assert_exists(Template(r"tpl1736858868805.png", record_pos=(0.001, 0.051), resolution=(1080, 2400)), "Merge Field")

    # Merge Tutorial Items
    sleep(3.0)
    swipe(Template(r"tpl1736866208284.png", record_pos=(-0.001, 0.047), resolution=(1080, 2400)), vector=[0.1515, 0.002])
    sleep(1.0)
    assert_exists(Template(r"tpl1736866406138.png", record_pos=(0.004, 0.05), resolution=(1080, 2400)), "Updated Merge Row.")
    swipe(Template(r"tpl1736874264407.png", record_pos=(-0.126, 0.043), resolution=(1080, 2400)), vector=[0.2452, 0.0052])

    sleep(1.0)
    assert_exists(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.043), resolution=(1080, 2400)), "Selected New Item.")
    swipe(Template(r"tpl1736866490558.png", record_pos=(0.12, 0.045), resolution=(1080, 2400)), vector=[0.0041, 0.0593])
    assert_exists(Template(r"tpl1736866754994.png", record_pos=(0.116, 0.163), resolution=(1080, 2400)), "Tutorial Generator Appeared.")

    # Multiple Generator Taps
    double_click(Template(r"tpl1736866754994.png"))
    
  # Мерж очков в стартовом туторе
    wait(Template(r"tpl1737116308721.png", record_pos=(0.008, 0.043), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737116332494.png", record_pos=(0.117, 0.045), resolution=(1080, 2400)), vector=[-0.1217, -0.0547], duration=0.01)

    # Мерж касок в стартовом туторе
    wait(Template(r"tpl1737116428573.png", record_pos=(0.001, 0.049), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737116457040.png", record_pos=(0.0, -0.071), resolution=(1080, 2400)), vector=[-0.1322, 0.1122], duration=0.01)

# Выход в парк по стартовому тутору
    wait(Template(r"tpl1737116518792.png", record_pos=(-0.006, 0.018), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1737116532279.png", record_pos=(0.356, 0.713), resolution=(1080, 2400)))

# Выполнение первого задания по тутору
    wait(Template(r"tpl1737116566092.png", record_pos=(0.0, -0.033), resolution=(1080, 2400)))
    touch((500, 1020), times=1)
    sleep(1.0)
    touch(Template(r"tpl1737116778264.png", record_pos=(0.076, 0.194), resolution=(1080, 2400)))
    wait(Template(r"tpl1737116825978.png", record_pos=(0.004, -0.079), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1737116845438.png", record_pos=(0.003, 0.278), resolution=(1080, 2400)))

    wait(Template(r"tpl1737116873316.png", record_pos=(-0.002, -0.026), resolution=(1080, 2400)))
    touch((500, 1020), times=1)
    sleep(1.0)
    touch(Template(r"tpl1737116923090.png", record_pos=(0.384, 0.586), resolution=(1080, 2400)))

    wait(Template(r"tpl1737116948085.png", record_pos=(0.002, 0.048), resolution=(1080, 2400)))
    double_click(Template(r"tpl1737116954306.png", record_pos=(0.1, 0.149), resolution=(1080, 2400)))

    wait(Template(r"tpl1737116993987.png", record_pos=(0.006, 0.144), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737117006332.png", record_pos=(-0.002, 0.049), resolution=(1080, 2400)), vector=[0.1083, 0.0968], duration=0.01)

    wait(Template(r"tpl1737117066908.png", record_pos=(0.006, 0.256), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737117083383.png", record_pos=(0.106, 0.046), resolution=(1080, 2400)), vector=[-0.2045, 0.0479], duration=0.01)

    wait(Template(r"tpl1737117124400.png", record_pos=(0.0, 0.047), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737117136274.png", record_pos=(0.104, 0.255), resolution=(1080, 2400)), vector=[-0.2027, -0.0432], duration=0.01)

    wait(Template(r"tpl1737117177565.png", record_pos=(0.005, 0.151), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737117190383.png", record_pos=(-0.104, 0.149), resolution=(1080, 2400)), vector=[0.1045, 0.0078], duration=0.01)
    sleep(1.0)
    touch(Template(r"tpl1737117224332.png", record_pos=(0.306, 0.618), resolution=(1080, 2400)))

    wait(Template(r"tpl1737117257608.png", record_pos=(0.004, -0.028), resolution=(1080, 2400)))
    touch(Template(r"tpl1737117266447.png", record_pos=(-0.005, -0.137), resolution=(1080, 2400)))
    sleep(2.0)
    touch(Template(r"tpl1737117286970.png", record_pos=(0.001, 0.269), resolution=(1080, 2400)))
    wait(Template(r"tpl1737117316867.png", record_pos=(0.0, -0.031), resolution=(1080, 2400)))
    touch((500, 1020), times=1)
    sleep(1.0)
    touch(Template(r"tpl1737117349279.png", record_pos=(0.382, 0.594), resolution=(1080, 2400)))

    wait(Template(r"tpl1737117372467.png", record_pos=(-0.002, 0.048), resolution=(1080, 2400)))
    double_click(Template(r"tpl1737117379776.png", record_pos=(0.103, 0.148), resolution=(1080, 2400)))
    sleep(1.0)
    swipe(Template(r"tpl1737117426788.png", record_pos=(-0.006, 0.146), resolution=(1080, 2400)), vector=[0.1198, 0.1015], duration=0.01)
    sleep(1.0)
    swipe(Template(r"tpl1737117458026.png", record_pos=(0.102, 0.358), resolution=(1080, 2400)), vector=[-0.1108, -0.0468], duration=0.01)
    sleep(1.0)

    touch(Template(r"tpl1737117494173.png", record_pos=(0.306, 0.617), resolution=(1080, 2400)))

    wait(Template(r"tpl1737117518696.png", record_pos=(-0.004, -0.026), resolution=(1080, 2400)))
    touch(Template(r"tpl1737117526353.png", record_pos=(0.003, -0.15), resolution=(1080, 2400)))
    wait(Template(r"tpl1737117544150.png", record_pos=(0.003, -0.08), resolution=(1080, 2400)))
    touch(Template(r"tpl1737117548476.png", record_pos=(0.005, 0.272), resolution=(1080, 2400)))
    sleep(3.0)
    touch((500, 1020), times=1)
    touch(Template(r"tpl1737117627896.png", record_pos=(0.381, -0.74), resolution=(1080, 2400)))
    touch((300, 1020), times=1)
    sleep(1.0)
    touch(Template(r"tpl1737117662334.png", record_pos=(-0.412, 0.617), resolution=(1080, 2400)))
    wait(Template(r"tpl1737117691240.png", record_pos=(0.001, -0.354), resolution=(1080, 2400)))
    touch(Template(r"tpl1737117695848.png", record_pos=(0.177, -0.314), resolution=(1080, 2400)))
    sleep(2.0)
    touch(Template(r"tpl1737117717773.png", record_pos=(-0.002, -0.146), resolution=(1080, 2400)))

    wait(Template(r"tpl1737117733564.png", record_pos=(0.008, -0.083), resolution=(1080, 2400)))
    touch(Template(r"tpl1737117738994.png", record_pos=(0.003, 0.275), resolution=(1080, 2400)))




    # Next Tutorials have random item drops, which makes autotests way too complex to handle
    # We can create multiple if/else or switch cases for handling randomness, but It will not test any new mechanic.

if __name__ == "__main__":
    main()
