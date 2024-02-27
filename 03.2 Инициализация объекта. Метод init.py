# 3.2 Инициализация объекта. Метод init
""""""
class Car:

    def set_values(self, new_model, new_engine):
        self.model = new_model
        self.engine = new_engine

bmw_3 = Car()
print(bmw_3.__dict__)  # {}
bmw_3.set_values('BMW', 3)
print(bmw_3.__dict__)  # {'model': 'BMW', 'engine': 3}


#  Магический метод __init__ будет срабатывать при создании объекта.
class Car:
    "Класс для определения характеристик машин"

    def __init__(self, new_model, new_engine):
        print('вызывается method init')
        self.model = new_model
        self.engine = new_engine


bmw_3 = Car('BMW', 3)  # вызывается метод __init__
print(bmw_3.__dict__)  # {'model': 'BMW', 'engine': 3}
audi_q4 = Car('Audi', 2.5)  # вызывается метод __init__
print(audi_q4.__dict__)   # {'model': 'Audi', 'engine': 2.5}

"""
На самом деле при создании ЭК Python сначала запускает 
метод-конструктор __new__ для нового объекта 
и по сути создаёт пространство имён (атрибут __dict__), 
после которого запускается метод __init__ , инициализирующий атрибуты. 
"""
class Car:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Car.")
        return super().__new__(cls)

    def __init__(self, new_model, new_engine):
        print("2. Initialize the new instance of Car.")
        self.model = new_model
        self.engine = new_engine

bmw_3 = Car('BMW', 3) # вызывается метод __init__
print(bmw_3.__dict__)  # {'model': 'BMW', 'engine': 3}


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Vehicle, у которого есть:
Конструктор __init__, принимающий максимальную скорость и пробег. 
Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно.
"""


class Vehicle():

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# Task 02
"""
Исправить код
"""
# Код с ошибками
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = 30
#
#     def greet(self):
#         return f"Hello, my name is {self.name.upper()}, and I am {self.age} years"


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name}, and I am {self.age} years old'


# Task 03
"""
Создать класс Laptop()
"""

class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'
        # return print('Экземпляр создан')

laptop1 = Laptop('Rubin', 'Ламповый цветной', 240)
laptop2 = Laptop('Horizont', 'Ламповый ч/б', 170)


# Task 04
"""
Создайте класс SoccerPlayer, у которого есть:

Конструктор __init__, принимающий 2 аргумента: name, surname. 
Также во время инициализации необходимо создать 2 атрибута экземпляра: 
goals и assists — общее количество голов и передач игрока, изначально оба значения должны быть 0.

Метод score, который принимает количество голов, забитых игроком. 
По умолчанию данное значение равно единице. 
Метод должен увеличить общее количество забитых голов игрока на переданное значение.

Метод make_assist, который принимает количество передач, сделанных игроком за матч. 
По умолчанию данное значение равно единице. 
Метод должен увеличить общее количество сделанных передач игроком на переданное значение.

Метод statistics, который вывод на экран статистику игрока в виде:
<Фамилия> <Имя> - голы: <goals>, передачи: <assists>
"""


class SoccerPlayer():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0  # атрибут создается без принятия аргумента функции def __init__(self)
        self.assists = 0

    def score(self, add=1):
        self.goals += add

    def make_assist(self, add=1):
        self.assists += add

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


# Task 05
"""
Создайте класс Zebra, внутри которого есть метод which_stripe , 
который поочередно печатает фразы «Полоска белая», 
«Полоска черная», начиная с фразы «Полоска белая».
"""
class Zebra():
    def __init__(self):
        self.color = 1

    def which_stripe(self):
        print('Полоска белая' if self.color % 2 else 'Полоска черная')
        self.color += 1

    # def which_stripe(self):
    #     if self.color % 2:
    #         print('Полоска белая')
    #     else:
    #         print('Полоска черная')
    #     self.color += 1

    def run_away(self):
        print('Oh, Sugar Honey Ice Tea')


# Task 06
"""
Создайте класс Person, у которого есть:

Конструктор __init__, принимающий имя, фамилию и возраст. 
Их необходимо сохранить в атрибуты экземпляра first_name , last_name, age. 

Метод full_name, который возвращает строку в виде "<Фамилия> <Имя>".

Метод is_adult, который возвращает True, 
если человек достиг 18 лет и False в противном случае.
"""
class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age >= 18
