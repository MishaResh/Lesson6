# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать
# класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить
# работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: {}

    def __init__(self, name, surname, position, _income={'wage': 100, 'bonus': 50}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage']+ self._income['bonus']
Ivanov = Worker('Иванов', 'Иван','Дворник',{'wage': 100,'bonus': 60})

print(f'ФИО ={Ivanov.get_full_name()} зарплата {Ivanov.get_total_income()}')