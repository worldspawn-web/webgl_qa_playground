# -*- encoding=utf8 -*-
# Magic School (Yandex)
# Start Test Window: Empty Google Page
# Version: 1.1.7

__author__ = "syndi"

import logging
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

def inter_check(starting=False):
    crosses = [
        Template(r"tpl1738073532964.png", record_pos=(0.464, -0.204), resolution=(2340, 1080)),
    ]

    if starting:
        wait(crosses[0], timeout=15)

    for cross in crosses:
        if exists(cross):
            touch(cross)
            break

game_url = "https://yandex.ru/games/app/359422?lang=ru"

def exists_and_touch(img):
    if exists(img):
        touch(img)
        return True
    return False

def main():
    auto_setup(__file__)
    start_app("com.android.chrome")

    img_name_light = Template(r"tpl1738163458836.png", record_pos=(0.005, -0.579), resolution=(1080, 2340))
    img_name_dark = Template(r"tpl1738163566332.png", record_pos=(-0.011, -0.581), resolution=(1080, 2340))

    if exists_and_touch(img_name_light):
        text(game_url)
    else:
        exists_and_touch(img_name_dark)
        text(game_url)

    inter_check(True)
    inter_check()

    ya_play_btn = Template(r"tpl1737106168601.png", record_pos=(0.003, 0.74), resolution=(1080, 2340))
    if exists(ya_play_btn):
        touch(ya_play_btn)

    assert_exists(Template(r"tpl1738148391338.png", record_pos=(0.039, -0.002), resolution=(2340, 1080)), "Проверка наличия экрана загрузки.")
    assert_exists(Template(r"tpl1738071922510.png", record_pos=(0.03, -0.03), resolution=(2340, 1080)), "Проверка наличия лого рус.")
    assert_exists(Template(r"tpl1738160756396.png", threshold=0.6, rgb=True, record_pos=(0.012, 0.181), resolution=(2340, 1080)), "Проверка наличия прогресс-бара")
    assert_exists(Template(r"tpl1738149589491.png", threshold=0.6, rgb=True, record_pos=(0.147, 0.209), resolution=(2340, 1080)), "Проверка наличия версии билда.")

if __name__ == "__main__":
    main()



