# 5.9 Slots
""""""

"""
Slots. 
- Ограничение атрибутов для класса
- операции над объектом выполняются быстрее
- занимает меньше памяти (из-за отсутствия __dict__)

Фиксированность
После указания __slots__ добавление новых атрибутов в экземпляр класса, 
кроме уже указанных, невозможно

Скорость работы программы
Используемая коллекция для хранения имён переменных в __slots__ 
позволяет ускорить работу программы по сравнению с используемым по умолчанию словарём (__dict__ )

Использование памяти
Уменьшение количества занимаемой памяти при использовании __slots__ связано с тем, 
что в __slots__ хранятся только значения из пространства имён, 
а при использовании __dict__ в память добавляется размер коллекции __dict__
"""
# обычное создание атрибутов
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# p1 = Point(2, 3)
# print(p1.x)
# print(p1.__dict__)
# p1.q = 100
# print(p1.q)


class PointSlots:
    __slots__ = ('x', 'y')  # ограничение атрибутов

    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = PointSlots(2, 3)
print(p2.x)
# print(p2.__dict__)  # ошибка
# p2.q = 100  # ошибка AttributeError



# *  *  *  *  *   Task   *  *  *  *  *

# Task 01
"""

"""
class Person:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"


# Код для проверки
arshavin = Person("Andrew", "Arshavin", 35)
assert arshavin.first_name == 'Andrew'
assert arshavin.last_name == 'Arshavin'
assert arshavin.age == 35
print(arshavin)

mg = Person("Max", "Galkin", 44)
assert mg.first_name == 'Max'
assert mg.last_name == 'Galkin'
assert mg.age == 44
print(mg)

try:
    arshavin.city = 'SPB'
except AttributeError:
    print('Нельзя создавать новые атрибуты')
print('Good')
