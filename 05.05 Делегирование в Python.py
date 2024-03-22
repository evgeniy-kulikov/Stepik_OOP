# 5.5 Делегирование в Python
""""""

"""
Механизм делегирования позволяет «переложить» часть работы на другие объекты. 
"""
# В данном примере мы просто дополнительно вызываем метод родителя в методе дочернего класса.
class Person:
    def walk(self):
        print("Человек идет")


class Doctor(Person):
    def walk(self):
        print("Доктор идет")
        super().walk()  # вызовет функцию walk у родителя

a = Doctor()
a.walk()    # Доктор идет
            # Человек идет



# Обратите внимание, что self мы не передаем при вызове родительского метода через super,
# экземпляр автоматически подставляется.
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        print("Человек идет")


class Doctor(Person):
    def __init__(self, name, surname, age):
        # вызовет функцию __init__ у родителя подставив свой self и значения name,surname
        super().__init__(name, surname)
        self.age = age

    def walk(self):
        super().walk()  # вызовет функцию walk у родителя
        print("Доктор идет")


a = Doctor('Jack', 'White', 25)
print(a.name, a.surname, a.age)  # Jack White 25


"""
Порядок делегирования:

сперва логика, потом делегирование
сперва делегирование, а потом логика
"""
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = None


class Doctor(Person):
    def __init__(self, name, surname, age):
        self.age = age  # логика
        super().__init__(name, surname)  # делегирование


d = Doctor('Sheldon', 'Cooper', 14)
print(d.name, d.surname, d.age)  # Sheldon Cooper None
# Делегирование после логики привело к тому, что возраст Шелдона перезатерся значением None.

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = None


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)  # делегирование
        self.age = age  # логика


d = Doctor('Sheldon', 'Cooper', 14)
print(d.name, d.surname, d.age)  #  Sheldon Cooper 14
# Теперь мы не потеряли значение возраста

"""
Обычно сперва лучше выполнить делегирование, а уже после выполнять свою логику в методе, 
если есть вероятность побочных эффектов.

Но иногда перед делегированием нужно выполнить подготовительные действия, 
которые необходимы будут для родительского метода.
см. пример из Django
"""
# пример из Django
from django.db import models

# importing slugify from django
from django.utils.text import slugify


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)


"""
Вызов super с параметрами type и obj
Во всех примерах до мы вызывали super() вызывается без каких-либо параметров, 
но super() также может принимать два необязятельных параметра:

первый параметр  type — это подкласс,
второй параметр obj — это объект, который является экземпляром подкласса type.
Первый параметр влияет на поиск родительского метода в иерархии

super() -> same as super(__class__, <first argument>)
        super(type) -> unbound super object
        super(type, obj) -> bound super object; requires isinstance(obj, type)
        super(type, type2) -> bound super object; requires issubclass(type2, type
"""
class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        print("Я Хирург")


class MainSurgeon(Surgeon):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Главный Хирург")


s = MainSurgeon()
s.tell_about_yourself()
# Я Доктор
# Я Главный Хирург

"""
Первый параметр говорит: от какого родителя нужно идти вверх для поиска атрибута/метода
"""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Устранить избыточность кода при помощи делегирования
"""
# Исходный код без делегирования
# class Employee:
#     def __init__(self, name, base_pay, bonus):
#         self.name = name
#         self.base_pay = base_pay
#         self.bonus = bonus
#
#     def get_pay(self):
#         return self.base_pay + self.bonus
#
# class SalesEmployee(Employee):
#     def __init__(self, name, base_pay, bonus, sales_incentive):
#         self.name = name
#         self.base_pay = base_pay
#         self.bonus = bonus
#         self.sales_incentive = sales_incentive
#
#     def get_pay(self):
#         return self.base_pay + self.bonus + self.sales_incentive

# Код с задействованием метода делегирования
class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive

# Код для проверки
jack = Employee('Jack', 5000, 1000)
assert jack.name == 'Jack'
assert jack.base_pay == 5000
assert jack.bonus == 1000
assert jack.get_pay() == 6000
john = SalesEmployee('John', 5000, 1000, 2000)
assert john.name == 'John'
assert john.base_pay == 5000
assert john.bonus == 1000
assert john.sales_incentive == 2000
assert john.get_pay() == 8000
print('Good')


# Task 02
"""
создать дочерний класс Square с использованием делегирования
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # Т.к. ничего не переопределяем, то это лишнее (но работоспособное)
    # def area(self):
    #     return super().area()
    #
    # def perimeter(self):
    #     return super().perimeter()


# Код для проверки
rect_1 = Rectangle(3, 2)
assert rect_1.area() == 6
assert rect_1.perimeter() == 10
rect_2 = Rectangle(10, 5)
assert rect_2.area() == 50
assert rect_2.perimeter() == 30
sq_1 = Square(4)
assert sq_1.area() == 16
assert sq_1.perimeter() == 16
sq_2 = Square(10)
assert sq_2.area() == 100
assert sq_2.perimeter() == 40
print('Good')


# Task 03
"""
Создайть базовый класс  Person, у которого есть:

конструктор __init__, который должен принимать на вход имя и номер паспорта 
и записывать их в атрибуты name, passport

метод display, который печатает на экран сообщение «<имя>: <паспорт>»;

Затем создайте подкласс Employee , 
унаследованный от Person. В нем должен быть реализован:

метод  __init__, который принимает именно в таком порядке четыре значения: 
имя, паспорт, зарплату и отдел. 
Их нужно сохранить в атрибуты  name, passport, salary,department. 
При этом создание атрибутов name, passport необходимо делегировать базовому классу Person
"""


class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f"{self.name}: {self.passport}")


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


# Код для проверки
assert issubclass(Employee, Person)
emp = Person("just human", 123456)
emp.display()
assert emp.__dict__ == {'name': 'just human', 'passport': 123456}
emp2 = Employee("Geek2", 534432, 321321, 'Roga & Koputa')
emp2.display()
assert emp2.__dict__ == {'salary': 321321, 'department': 'Roga & Koputa',
                         'name': 'Geek2', 'passport': 534432}
print('Good')


# Task __
"""
Тест
"""
class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        super().tell_about_yourself()
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        super().tell_about_yourself()
        print("Я Хирург")


class MainSurgeon(Surgeon):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Главный Хирург")


s = MainSurgeon()
s.tell_about_yourself()
# Я Человек
# Я Доктор
# Я Главный Хирург


# Task __
"""
Тест
"""
class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        super(Doctor, self).tell_about_yourself()
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Хирург")


class MainSurgeon(Surgeon):
    def tell_about_yourself(self):
        super(Doctor, self).tell_about_yourself()
        print("Я Главный Хирург")


s = MainSurgeon()
s.tell_about_yourself()
# Я Человек
# Я Главный Хирург


# Task __
"""
Тест
"""
class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        print("Я Хирург")


d = Doctor()
d.tell_about_yourself()
# Ошибка




# Task 04
"""
https://stepik.org/lesson/682564/step/12?thread=solutions&unit=681376
"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f"Total {self.name} fare is: {self.fare()}")


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=50):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):
    def __init__(self, name, mileage, capacity=4):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.35


# Код для проверки
sc = Vehicle('Scooter', 100, 2)
sc.display()
merc = Bus("Mercedes", 120000)
merc.display()
polo = Taxi("Volkswagen Polo", 15000)
polo.display()
t = Taxi('x', 111)
assert t.__dict__ == {'name': 'x', 'mileage': 111, 'capacity': 4}
t.display()
b = Bus('t', 123)
assert b.__dict__ == {'name': 't', 'mileage': 123, 'capacity': 50}
b.display()
print('Good')


# Task 05
"""
В этой задаче у нас будет один родительский класс Transport и три дочерних класса: Car, Boat, Plane.

В классе Transport должны быть реализованы:
метод __init__, который создает атрибуты brand, max_speed и kind. 
Значения атрибутов brand, max_speed , kind поступают при вызове метода __init__. 
При этом значение kindне является обязательным и по умолчанию имеет значение None;
метод __str__, который будет возвращать строку формата: 
"Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".

В классе Car должны быть реализованы:
метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue. 
Все значения этих атрибутов передаются при вызове класса Car. 
Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind родительскому классу Transport , 
при этом атрибуту kindпередайте значение "Car";
свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина <gasoline_residue> л";
свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value, увеличивает уровень топлива gasoline_residue на переданное значение и затем вывести фразу 'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'. Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.

В классе Boat должны быть реализованы:
метод __init__, принимающий три значения brand, max_speed, owners_name. 
Их нужно сохранить в соответствующие атрибуты. При этом внутри инициализации нужно делегировать 
создание атрибутов brand, max_speed , kind родительскому классу Transport , 
в атрибут kind при этом передайте значение "Boat";
метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.

В классе Planeдолжны быть реализованы:
метод __init__, создающий у экземпляра атрибуты brand, max_speed, capacity. 
Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind родительскому классу Transport , 
при этом атрибуту kind передайте значение "Plane";
метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.
"""
class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} " \
               f"марки {self.brand} " \
               f"может развить скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина {self.__gasoline_residue} л"

    @gasoline.setter
    def gasoline(self, val):
        if isinstance(val, int):
            self.__gasoline_residue += val
            print(f"Объем топлива увеличен на {val} л "
                  f"и составляет {self.__gasoline_residue} л")
        else:
            print("Ошибка заправки автомобиля")


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"


# Код для проверки
p1 = Transport('Chuck', 50)
print(p1)
assert isinstance(p1, Transport)
assert p1.kind == None
assert p1.brand == 'Chuck'
assert p1.max_speed == 50
assert p1.__dict__ == {'kind': None, 'brand': 'Chuck', 'max_speed': 50}

c1 = Car('RRR', 50, 150, 999)
print(c1)

assert isinstance(c1, Car)
assert c1.kind == "Car"
assert c1.brand == 'RRR'
assert c1.max_speed == 50
assert c1.mileage == 150
assert c1.gasoline == 'Осталось бензина 999 л'
c1.gasoline = 100
assert c1.gasoline == 'Осталось бензина 1099 л'
assert c1.__dict__ == {'kind': 'Car', 'brand': 'RRR', 'max_speed': 50,
                       'mileage': 150, '_Car__gasoline_residue': 1099}

b1 = Boat('XXX', 1150, 'Arkasha')
print(b1)
assert isinstance(b1, Boat)
assert b1.kind == "Boat"
assert b1.brand == 'XXX'
assert b1.max_speed == 1150
assert b1.owners_name == 'Arkasha'

pla = Plane('www', 2150, 777)
print(pla)
assert isinstance(pla, Plane)
assert pla.kind == "Plane"
assert pla.brand == 'www'
assert pla.max_speed == 2150
assert pla.capacity == 777

transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
print(first_car.gasoline)  # Осталось бензина на 350 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr
print('Good')


# Task 06
"""
https://stepik.org/lesson/682564/step/14?unit=681376
"""
from functools import total_ordering

class Initialization:
    def __init__(self, capacity: int, food: list):
        if not isinstance(capacity, int):
            print("Количество людей должно быть целым числом")
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):
    def __init__(self, capacity: int, food: list):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity: int, food: list):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


@total_ordering
class SweetTooth (Initialization):
    def __init__(self, capacity: int, food: list):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity == other.capacity
        return f"Невозможно сравнить количество сладкоежек с {other}"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity < other.capacity
        return f"Невозможно сравнить количество сладкоежек с {other}"


# Код для проверки
p1 = Initialization('Chuck', [])
assert isinstance(p1, Initialization)
assert not hasattr(p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ['Arkasha'])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ['Arkasha']

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
print('Good')
