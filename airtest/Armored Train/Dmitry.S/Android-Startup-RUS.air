__author__ = "Sevostyanov Dmitry"
__branch__ = "Review/dmitry"
__device__ = "Redmi Note 13"

import time
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

auto_setup(__file__)

def repeated_click(poco, position=[0.5, 0.5], count=1, float=1):
    #Функция для повторного нажатия в указанные кординаты и ожиданием
    for _ in range(count):
        poco.click(position)  # Координаты
        sleep(float)  # Ожидание между кликами
        
def multi_click(poco, positions, float=1):
     for position in positions:
        poco.click(position)
        sleep(float)

def poco_exists(el):
    #Проверка на существование элемента и клика по нему
    if el.exists():
        el.click()
    else:
        raise Exception("Button has not been found")

                    
def wait_for_mascot(el_text="ГЕНЕРАЛ", timeout=200): # Ожидание нужного текста на экране
    mascot_img = poco(text=el_text)
    mascot_img.wait_for_appearance(timeout)
    
  
def main():
    
    play_btn = poco(text="ИГРАТЬ")
    assert_exists(Template(r"tpl1739799947873.png", record_pos=(0.0, -0.0), resolution=(2400, 1080)), "post-loader screen.")
    poco_exists(play_btn)
    
    repeated_click(poco)
    
    play_btn = poco(text="К ЗАДАНИЮ!")
    assert_exists(Template(r"tpl1739866246781.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Button.")
    poco_exists(play_btn)
    
    repeated_click(poco, count=4, float=1.5)
    
    play_btn = poco(text="СТАРТ")
    assert_exists(Template(r"tpl1739867200580.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Start first mission.")
    poco_exists(play_btn)
    
    #Первая волна
    
    wait_for_mascot()
    
    repeated_click(poco, count=4, float=2)
    
    wait_for_mascot()
    
    repeated_click(poco, count=2)
    
    wait_for_mascot("Ты напрямую управляешь поездом, его скоростью и где он остановится. Попробуй остановить поезд в нужном месте.")
    repeated_click(poco)
    # Остановка поезда
    poco.swipe([0.864, 0.639], [0.876, 0.895], duration=12) # Добавил скорость свайпа
    
    
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
    float=1
    multi_click(poco, positions, float)
    touch(Template(r"tpl1739952623957.png", record_pos=(0.473, 0.087), resolution=(2400, 1080)))

    # Уничтожение третьей волны
    wait_for_mascot("Получено новое подразделение")
    assert_exists(Template(r"tpl1740117834759.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Please fill in the test point.")

    #Получение награды и выход в главное меню
    repeated_click(poco, count=2)
    play_btn = poco(text="В ГЛАВНОЕ МЕНЮ")
    assert_exists(Template(r"tpl1739949240705.png", record_pos=(0.003, -0.001), resolution=(2400, 1080)), "Window-Win.")
    poco_exists(play_btn)

    # Переход на глобальную карту
    play_btn = poco(text="К ЗАДАНИЮ!")
    assert_exists(Template(r"tpl1739955713760.png", record_pos=(0.0, 0.001), resolution=(2400, 1080)), "Main menu.")
    poco_exists(play_btn)
    
    repeated_click(poco, count=9, float=2)
    # Начало второй миссии
    play_btn = poco(text="СТАРТ")
    assert_exists(Template(r"tpl1739867200580.png", record_pos=(-0.001, -0.001), resolution=(2400, 1080)), "Start second mission.")
    poco_exists(play_btn)
    # Ожидание начала тутора на турель
    wait_for_mascot()
    # Диалоговое окно + тутор на установку турели
    repeated_click(poco, count=3, float=2)
    positions = [[0.507, 0.501], [0.625, 0.302], [0.694, 0.560], [0.5, 0.5]]
    float = 2
    multi_click(poco, positions, float)
    # Покупка вагона и закрытие окна управления поездом
    positions = [[0.936, 0.513], [0.226, 0.852], [0.93, 0.935]]
    float=1
    multi_click(poco, positions, float)
    touch(Template(r"tpl1739952623957.png", record_pos=(0.473, 0.087), resolution=(2400, 1080)))
    # Ожидание второй волны
    wait_for_mascot("Пропустить ожидание")
    repeated_click(poco, position=[0.5, 0.25])
    # Улучшение турели
    positions = [[0.588, 0.595], [0.768, 0.473], [0.768, 0.473],[0.5, 0.5]]
    float=1
    multi_click(poco, positions, float)
    wait_for_mascot("Пропустить ожидание")
    repeated_click(poco, position=[0.5, 0.25])
    # Ожидание конца миссии и получение награды
    wait_for_mascot("Получено новое подразделение")
    assert_exists(Template(r"tpl1740118795218.png", record_pos=(0.0, 0.0), resolution=(2400, 1080)), "Getting a new unit.")
    repeated_click(poco)
    wait_for_mascot("Получен новый вагон")
    assert_exists(Template(r"tpl1740118837119.png", record_pos=(0.0, -0.0), resolution=(2400, 1080)), "Getting a new train.")
    repeated_click(poco, float=2)


    # выход в главное меню
    play_btn = poco(text="В ГЛАВНОЕ МЕНЮ")
    assert_exists(Template(r"tpl1739949240705.png", record_pos=(0.003, -0.001), resolution=(2400, 1080)), "Window-Win.")
    poco_exists(play_btn)
    # Баннер РЖД
    sleep(20)
    touch(Template(r"tpl1740120033277.png", record_pos=(0.29, -0.159), resolution=(2400, 1080)))



if __name__ == "__main__":
    main()