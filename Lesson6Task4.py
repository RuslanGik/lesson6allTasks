# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также
# методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    '''Автомобиль'''

    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        print(f'New car: {self.name} (color {self.color}')

    def go(self, speed=30):
        self.speed = speed
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        self.speed = 0
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула: {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'

class TownCar(Car):
    '''Городскаой автомобиль'''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля: {self.speed}."


class WorkCar(Car):
    '''Грузовой автомобиль'''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля: {self.speed}."


class SportCar(Car):
    '''Спортивный автомобиль'''


class PoliceCar(Car):
    '''Полицейский автомобиль'''
    is_police = True


police_car = PoliceCar("BMW", "Black", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()

print()
sport_car = SportCar('"Спорт"', 'Фиолетовый', 130)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Каблучок"', 'зеленый', 45)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')

