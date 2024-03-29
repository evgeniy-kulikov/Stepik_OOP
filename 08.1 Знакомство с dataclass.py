#  8.1 Знакомство с dataclass
""""""

"""
Dataclass предоставляют удобный способ создания классов, 
которые могут быть использованы для хранения и обработки данных.

Преимущества dataclass
При использовании dataclass вы получаете:

* более короткий и выразительный код
* автоматически реализованный метод __init__
* автоматически реализованные метод __repr__ 
* автоматически реализованные метод __eq__ 
* аннотированные атрибуты
"""
# Привычная реализация
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Customer {self.name}, balance={self.balance}"


#  Функция dataclass
from dataclasses import dataclass

@dataclass
class Customer:
    name: any
    balance: any

jack = Customer('jack', 500)
print(jack)  # Customer(name='jack', balance=500)
print(jack.name, jack.balance) # jack 500


# Функция make_dataclass
from dataclasses import make_dataclass

Person = make_dataclass('Person', ['first_name', 'last_name', 'age'])

artem = Person('Artem', 'Egorov', 33)
print(artem.first_name)  # Artem
print(artem.age)  # 33
print(artem)  # Person(first_name='Artem', last_name='Egorov', age=33)


#  Значения по умолчанию в привычной реализации
class InventoryItem:
    def __init__(self, name, price=9.99, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity


#  Значения по умолчанию в dataclass
"""
Будьте аккуратны с обязательными атрибутами. 
Они внутри класса должны перечисляться в самом верху, 
затем должны идти необязательные атрибуты. 
Если вы не будете соблюдать это правило, возникнет исключение:
TypeError: non-default argument 'name' follows default argument
"""
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1


# Функция field
"""
При работе со значениями, по умолчанию, в классах данных есть одна особенность — 
нельзя указывать изменяемые типы данных в качестве значения по умолчанию. 
Значит, никаких списков, словарей и множеств указать нельзя.
"""
from dataclasses import dataclass, field


@dataclass
class InventoryItem:
    name: str
    quantity: int = 1
    price: float = 9.99
    colors: list = ['black', 'white']
# ValueError: mutable default <class 'list'> for field colors is not allowed: use default_factory



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
из обычного класса Student  сделать дата-класс

class Student:
    def __init__(self, name, surname, student_id, faculty, specialty):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.specialty = specialty
"""
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    surname: str
    student_id: int
    faculty: str
    specialty: str


# Task 02
"""
создать dataclass Point, который должен хранить два целых атрибута x и y .
На основании класса Point создайте
точку с координатами (5, 7) и сохраните ее в  переменную point1
точку с координатами (-10, 12) и сохраните ее в  переменную point2
Выведите сперва point1 потом на отдельной строке point2
"""
from dataclasses import dataclass, is_dataclass

@dataclass
class Point:
    x: int
    y: int

point1 = Point(5, 7)
point2 = Point(-10, 12)
print(point1)
print(point2)

# Код для проверки
assert is_dataclass(Point), 'Point не dataclass'
assert isinstance(point1, Point)
assert isinstance(point2, Point)
assert point1.x == 5
assert point1.y == 7
assert point2.x == -10
assert point2.y == 12


# Task 03
"""
Создайте дата-класс  Location
В нем должны быть описаны следующие атрибуты

name — обязательный, тип строка
longitude — необязательный, вещественный тип, значение по умолчанию 0
latitude  необязательный, вещественный тип, значение по умолчанию 11.5

Создайте ЭК Location со значениями name='Stonehenge', longitude=51, latitude=1.5  
и сохраните его в переменную stonehenge
"""
from dataclasses import dataclass

@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5

stonehenge = Location('Stonehenge', 51, 1.5)


# Task 04
"""
Создайте датакласс  Person
В нем должны быть описаны следующие атрибуты

first_name — обязательный, тип строка
last_name — обязательный, строковый тип
hobbies — необязательный, представляет собой множество, значение по умолчанию  пустое множество
"""
from dataclasses import dataclass, field

@dataclass
class Person:
    first_name: str
    last_name: str
    hobbies: str = field(default_factory=set)



