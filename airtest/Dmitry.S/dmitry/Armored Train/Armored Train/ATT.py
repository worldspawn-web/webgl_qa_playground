# -*- encoding=utf8 -*-
__author__ = "Sevostyanov Dmitry"
__branch__ = "Review/dmitry"
__device__ = "Redmi Note 13"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

auto_setup(__file__)

def repeated_click(poco, position=[0.5, 0.5], count=1, interval=1):
    #Функция для повторного нажатия в указанные кординаты и ожиданием
    for _ in range(count):
        poco.click(position)  # Координаты
        sleep(interval)  # Ожидание между кликами
        
def multi_click(poco, positions, interval=1):
     # Функция для последовательного нажатия на разные коордианаты(прим.Туторы)
     for position in positions:
        poco.click(position)
        sleep(interval)

def poco_exists(el):
    #Проверка на существование элемента и клика по нему
    if el.exists():
        el.click()
    else:
        raise Exception("Button has not been found")

def main():
    
    play_btn = poco(text="ИГРАТЬ")
    assert_exists(Template(r"tpl1739799947873.png", record_pos=(0.0, -0.0), resolution=(2400, 1080)), "post-loader screen.")
    poco_exists(play_btn)
    
    
    repeated_click(poco, position=[0.5, 0.5], count=1, interval=1)
    
    
    play_btn = poco(text="К ЗАДАНИЮ!")
    assert_exists(Template(r"tpl1739866246781.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Button.")
    poco_exists(play_btn)
    repeated_click(poco, position=[0.5, 0.5], count=4, interval=1)
    
    #repeated_click(poco, position=[0.5, 0.5], count=2, interval=1)
    #repeated_click(poco, position=[0.5, 0.5], count=2, interval=1)
    
    play_btn = poco(text="СТАРТ")
    assert_exists(Template(r"tpl1739867200580.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Start first mission.")
    poco_exists(play_btn)
    
    #Первая волна
    sleep(12)
    repeated_click(poco, position=[0.5, 0.5], count=3, interval=1)
    sleep(8)
    repeated_click(poco, position=[0.5, 0.5], count=2, interval=8)
    
    # Остановка поезда
    poco.swipe([0.864, 0.639], [0.876, 0.895])
    
    # Уничтожение первой волны
    sleep(18)
    # Скип ожидания
    repeated_click(poco, position=[0.5, 0.25], count=2, interval=1)
    # Уничтожение второй волны
    sleep(30)
    # Скип ожидание и диалогового окна
    repeated_click(poco, position=[0.5, 0.25], count=4, interval=1)
    #repeated_click(poco, position=[0.5, 0.5], count=1, interval=65)
    #repeated_click(poco, position=[0.5, 0.5], count=3, interval=2)
    # Тутор на покупку нового вагона
    
    positions = [[0.940, 0.525], [0.223, 0.871], [0.109, 0.854], [0.917, 0.937], [0.5, 0.5]]
    interval = 0.5
    multi_click(poco, positions, interval)
    touch(Template(r"tpl1739952623957.png", record_pos=(0.473, 0.087), resolution=(2400, 1080)))

    
    #poco.click([0.940, 0.525])
    #poco.click([0.223, 0.871])
    #poco.click([0.109, 0.854])
    #poco.click([0.917, 0.937])
    
    
    
    # Уничтожение третьей волны
    sleep(35)
    #repeated_click(poco, position=[0.5, 0.5], count=1, interval=60)
    #Получение награды и выход в главное меню
    repeated_click(poco, position=[0.5, 0.5], count=2, interval=1)
    play_btn = poco(text="В ГЛАВНОЕ МЕНЮ")
    assert_exists(Template(r"tpl1739949240705.png", record_pos=(0.003, -0.001), resolution=(2400, 1080)), "Window-Win.")
    poco_exists(play_btn)


if __name__ == "__main__":
    main()