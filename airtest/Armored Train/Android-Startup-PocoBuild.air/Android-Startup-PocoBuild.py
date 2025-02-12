# -*- encoding=utf8 -*-
__author__ = "Michael 'Worldspawn' Lozickii"
__branch__ = "aqa/unity_poco"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

auto_setup(__file__)
poco = UnityPoco()

########################
#   HELPER FUNCTIONS   #
########################

def assert_and_touch(img, note = "", poco = False, delay = 1.0):
    if poco:
        if img.exists():
            img.click()
        print(note)
        return
    
    if assert_exists(img, note):
        touch(img)
        sleep(delay)
        return
    
def random_touch(delay = 1.0):
    touch((0.5, 0.5))
    sleep(delay)

###################
#   TESTS START   #
###################

def main():
    assert_exists(Template(r"tpl1739382112852.png", record_pos=(-0.003, -0.001), resolution=(2400, 1080)), "Post-Loader Screen.")
    assert_and_touch(poco(text="PLAY"), "Post Loader Play Button", True)
    
    # Main Scene Tutorial
    assert_exists(Template(r"tpl1739383777982.png", record_pos=(-0.0, -0.0), resolution=(2400, 1080)), "Tutorial Mascot Appeared.")
    random_touch()
    
    assert_exists(Template(r"tpl1739383067899.png", record_pos=(-0.0, -0.001), resolution=(2400, 1080)), "Tutorial Finger.")

if __name__ == "__main__":
    main()
