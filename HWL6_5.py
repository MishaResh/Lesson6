# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

    def out(self):
        print(f'класс {self.title} начинает {self.draw()}')

class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручки'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки карандаша'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркера'


New_Pen = Pen('Ручка')
New_Pencil = Pencil('Карандаш')
New_Handle = Handle('Маркер')
New_Pen.out()
New_Pencil.out()
New_Handle.out()
