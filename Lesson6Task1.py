# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    __color = "Чёрный"

    def running(self):
        while True:
            print("Trafficlight is red now!")
            sleep(7)
            print("Trafficlight is yellow now!")
            sleep(2)
            print("Trafficlight is green now!")
            sleep(7)
            print("Trafficlight is yellow now!")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

# Вариант решения
import time

class TrafficLight:


    def running(self):
        while True:
            self.__color = "Красный"
            print(f"{self.__color}")
            time.sleep(7)
            self.__color = "Желтый"
            print(f"{self.__color}")
            time.sleep(2)
            self.__color = "Зеленый"
            print(f"{self.__color}")
            time.sleep(7)


trafficlight = TrafficLight()
trafficlight.running()

# Вариант
import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]], ]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficlight1 = TrafficLight()
trafficlight1.running()


