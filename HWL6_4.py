# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color, speed, is_police, direction='forward') -> object:
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.direction = direction

    def show_speed(self):
        return self.speed

    def show_police(self):
        return 'Полицейский' if self.is_police == True else ''

    def go(self):
        return self.speed if self.speed > 0 else 0

    def stop(self):
        return self.speed if self.speed == 0 else 0

    def turn(self):
        return self.direction if self.speed > 0 else 'no movement'

    def out(self):
        print(
            f'{self.show_police()} Автомобиль {self.name} {self.color} цвета едет {self.direction} со скоростью {self.show_speed()}')


PoliceCar = Car
SportCar = Car


class TownCar(Car):
    def show_speed(self):
        return 'превышение скорости' if self.speed >= 60 else self.speed


class WorkCar(Car):
    def show_speed(self):
        return 'превышение скорости' if self.speed >= 40 else self.speed


Lada = TownCar('Lada', 'red', 150, False)
Subaru = SportCar('Subaru', 'green', 50, False, 'left')
Fiat = PoliceCar('Fiat', 'yellow', 50, False, 'left')
Hummer = WorkCar('Hummer', 'black', 70, True, 'right')

Lada.out()
Subaru.out()
Fiat.out()
Hummer.out()