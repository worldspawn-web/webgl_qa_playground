__author__ = "Sevostyanov Dmitry"
__branch__ = "Review/dmitry"
__device__ = "Redmi Note 13"

import time
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

auto_setup(__file__)

def repeated_click(poco, position=[0.5, 0.5], count=1, float=1.0, pre_sleep=1):
    #Функция для повторного нажатия в указанные кординаты и ожиданием
    for _ in range(count):
        sleep(pre_sleep)
        poco.click(position)  # Координаты
        sleep(float)  # Ожидание между кликами
        
def multi_click(poco, positions, float=1.0):
     for position in positions:
        poco.click(position)
        sleep(float)

def assert_and_touch(el):
    #Проверка на существование элемента и клика по нему
    if el.exists():
        el.click()
        print(f"Touched {el}...OK!")
    else:
        raise Exception(f"{el} has not been found!")

                    
def wait_for_mascot(el_text="ГЕНЕРАЛ", timeout=120):
    mascot_img = poco(text=el_text)
    mascot_img.wait_for_appearance(timeout)
    

def cheat_win(poco):
    poco.click([0.97, 0.034])
    sleep(1)
    if poco(text="Настройки").exists():
        poco(text="Настройки").click()
        sleep(1)
    
    for _ in range(3):
        poco.swipe([0.5, 0.5], [0.48, 0.6], duration=0.5)
        sleep(0.5)
        
    for _ in range(2):
        poco.swipe([0.545, 0.748], [0.434, 0.79], duration=0.5)
        sleep(0.5)
        
    for _ in range(2):
        poco.swipe([0.434, 0.79], [0.545, 0.748], duration=0.5)
        sleep(0.5)
    
    if poco(text="WIN").exists():
        poco(text="WIN").click()
        sleep(1)
   

def main():
    
    play_btn = poco(text="ИГРАТЬ")
    assert_exists(Template(r"tpl1739799947873.png", record_pos=(0.0, -0.0), resolution=(2400, 1080)), "post-loader screen.")
    assert_and_touch(play_btn)
    
    repeated_click(poco)
    
    play_btn = poco(text="К ЗАДАНИЮ!")
    assert_exists(Template(r"tpl1739866246781.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Button.")
    assert_and_touch(play_btn)
    
    repeated_click(poco, count=4, float=1.5)
    
    play_btn = poco(text="СТАРТ")
    assert_exists(Template(r"tpl1739867200580.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Start first mission.")
    assert_and_touch(play_btn)
    
    #Первая волна
    
    wait_for_mascot()
    
    repeated_click(poco, count=4, float=2.0)
    
    wait_for_mascot()
    
    repeated_click(poco, count=2)
    
    wait_for_mascot("Ты напрямую управляешь поездом, его скоростью и где он остановится. Попробуй остановить поезд в нужном месте.")
    repeated_click(poco)
    # Остановка поезда
    poco.swipe([0.864, 0.639], [0.876, 0.895], duration=12)
    
    
    # Уничтожение первой волны
    wait_for_mascot()
    # Скип ожидания
    repeated_click(poco, position=[0.5, 0.25], count=2)
    # Уничтожение второй волны
    wait_for_mascot()
    # Скип ожидание и диалогового окна
    repeated_click(poco, position=[0.5, 0.25], count=4)

    # Тутор на покупку нового вагона
    
    positions = [[0.940, 0.525], [0.223, 0.871], [0.109, 0.854], [0.917, 0.937], [0.5, 0.5]]
    float=1.0
    multi_click(poco, positions, float)
    touch(Template(r"tpl1739952623957.png", record_pos=(0.473, 0.087), resolution=(2400, 1080)))
    
    cheat_win(poco)

    wait_for_mascot("Получено новое подразделение")
    assert_exists(Template(r"tpl1740117834759.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Getting a new unit.")

    #Получение награды и выход в главное меню
    repeated_click(poco, count=2)
    play_btn = poco(text="В ГЛАВНОЕ МЕНЮ")
    assert_exists(Template(r"tpl1739949240705.png", record_pos=(0.003, -0.001), resolution=(2400, 1080)), "Window-Win.")
    assert_and_touch(play_btn)
    
    
    
    # Переход на глобальную карту
    play_btn = poco(text="К ЗАДАНИЮ!")
    assert_exists(Template(r"tpl1739955713760.png", record_pos=(0.0, 0.001), resolution=(2400, 1080)), "Main menu.")
    assert_and_touch(play_btn)
    
    repeated_click(poco, count=9, float=2.0)
    # Начало второй миссии
    play_btn = poco(text="СТАРТ")
    assert_exists(Template(r"tpl1739867200580.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Start second mission.")
    assert_and_touch(play_btn)
    # Ожидание начала тутора на турель
    wait_for_mascot()
    # Диалоговое окно + тутор на установку турели
    repeated_click(poco, count=3, float=3.0)
    sleep(5)
    positions = [[0.507, 0.501], [0.625, 0.302], [0.694, 0.560], [0.5, 0.5]]
    float = 2.0
    multi_click(poco, positions, float)
    # Покупка вагона и закрытие окна управления поездом
    positions = [[0.936, 0.513], [0.226, 0.852], [0.93, 0.935]]
    float=1.0
    multi_click(poco, positions, float)
    touch(Template(r"tpl1739952623957.png", record_pos=(0.473, 0.087), resolution=(2400, 1080)))
    # Ожидание второй волны
    # Улучшение турели
    positions = [[0.588, 0.595], [0.768, 0.473], [0.768, 0.473],[0.5, 0.5]]
    float=1.0
    multi_click(poco, positions, float)
    cheat_win(poco)
    # Ожидание конца миссии и получение награды
    wait_for_mascot("Получено новое подразделение")
    assert_exists(Template(r"tpl1740118795218.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Getting a new unit.")
    repeated_click(poco)
    wait_for_mascot("Получен новый вагон")
    assert_exists(Template(r"tpl1740118837119.png", record_pos=(0.0, -0.0), resolution=(2400, 1080)), "Getting a new train.")
    repeated_click(poco, float=2.0)


    # выход в главное меню
    play_btn = poco(text="В ГЛАВНОЕ МЕНЮ")
    assert_exists(Template(r"tpl1739949240705.png", record_pos=(0.003, -0.001), resolution=(2400, 1080)), "Window-Win.")
    assert_and_touch(play_btn)
    # Баннер РЖД
    sleep(20)
    touch(Template(r"tpl1740120033277.png", record_pos=(0.29, -0.159), resolution=(2400, 1080)))


    # Запуск третьей миссии
    
    play_btn = poco(text="К ЗАДАНИЮ!")
    assert_exists(Template(r"tpl1740120086305.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Main menu.")
    assert_and_touch(play_btn)
    repeated_click(poco, count=2, float=2.0)
    
    


if __name__ == "__main__":
    main()