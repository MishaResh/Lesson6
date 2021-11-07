# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
# полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _lehgth: int
    _width: int

    def __init__(self, lehgth, width, weight=25, thickness=5):
        self._lehgth = lehgth
        self._width = width
        self._weight = weight
        self._thickness = thickness

    def total_weight(self):
        return self._lehgth * self._width * self._weight * self._thickness


new_weight = Road(1000,20)

print(f'Вес асфальта длинной {new_weight._lehgth}  м., шириной {new_weight._width} м. '
      f'толщиной {new_weight._thickness} см., равен {new_weight.total_weight() / 1000} тонн')
