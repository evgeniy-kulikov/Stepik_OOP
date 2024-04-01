#  8.3 dataclass: дополнительные возможности
""""""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Прыжки в воду
По правилам соревнований каждый прыжок оценивается 3 судьями, 
каждых из них должен выставить оценку - вещественное число от 0 до 10. 
Затем находиться среднее арифметическое по выставленным оценкам и умножается на коэффициент сложности прыжка, 
в результате получим значение балла спортсмена. 
Кто наберет самое большое количество баллов то и победит на этих соревнованиях. 

имеется дата-класс Athlet:

from dataclasses import dataclass, field

@dataclass
class Athlet:
    name: str
    coefficient: float
    scores: list = field(default_factory=list)

print(f"Победитель соревнований: {max(sportsmans)}")

дописать класс Athlet таким образом, чтобы его экземпляры могли сортироваться по баллам. 
Это нужно для определения победителя соревнований
"""
from dataclasses import dataclass, field
from statistics import mean

@dataclass(order=True)
class Athlet:
    sort_index: float = field(init=False, repr=False)
    name: str = field(compare=False)
    coefficient: float = field(repr=False, compare=False)
    scores: list = field(default_factory=list, repr=False, compare=False)

    def __post_init__(self):
        self.sort_index = mean(self.scores) * self.coefficient


# Код для проверки
sportsmans = [
    Athlet('Иван', 1.5, [9.0, 8.0, 7.0]),
    Athlet('Петр', 1.0, [10.0, 9.0, 8.0]),
    Athlet('Алексей', 1.2, [8.0, 7.0, 6.0])
]
print(f"Победитель соревнований: {max(sportsmans)}")
# Победитель соревнований: Athlet(name='Иван')


# Task 02
"""
дописать класс Student так, чтобы в нем появились

атрибут guid - уникальная случайно сгенерированная строка длиной 15 символов. 
Для этого воспользуйтесь заготовленной функций generate_guid. 
Атрибут не должен участвовать в инициализации и в методе __repr__

поле email - строковое значение, которое назначает университет студенту. 
Формируется из имени и фамилии в нижнем регистре следующим образом
{first_name}.{last_name}@uni.edu
В инициализации не участвует

поле tuition необязательный атрибут, обозначающий стоимость за обучение. 
По умолчанию студент учиться бесплатно, значит его tuition равно нулю. 
Для платников значение передается при инициализации.   В __repr__ не участвует
Также необходимо сортировать всех студентов сперва по стоимости обучения 
(кто учится бесплатно должны быть первыми), а затем по фамилии и имени.
"""
# Исходный код
# import random
# import string
# from dataclasses import dataclass, field
#
# alphabet = string.ascii_uppercase + string.digits
#
# def generate_guid():
#     guid = ''.join(random.choices(alphabet, k=15))
#     return guid
#
# @dataclass
# class Student:
#     first_name: str
#     last_name: str

import random
import string
from dataclasses import dataclass, field

alphabet = string.ascii_uppercase + string.digits
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def generate_guid():
    guid = ''.join(random.choices(alphabet, k=15))
    return guid  # 'T2TIJWAQW3UYB8H'


@dataclass(order=True)
class Student:
    sort_index: tuple = field(init=False, repr=False)
    guid: str = field(init=False, repr=False, compare=False)
    first_name: str = field(compare=False)
    last_name: str = field(compare=False)
    email: str = field(init=False, compare=False)
    tuition: int = field(default=0, repr=False, compare=False)

    def __post_init__(self):
        self.guid = generate_guid()
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@uni.edu"
        self.sort_index = (self.tuition, self.last_name, self.first_name)


# Код для проверки
jane = Student('Jane', 'Lee', 30000)
assert jane.tuition == 30000
assert len(jane.guid) == 15
print(jane)  # Student(first_name='Jane', last_name='Lee', email='jane.lee@uni.edu')
julia = Student('Julia', 'Doe')
assert julia.tuition == 0
assert len(julia.guid) == 15
print(julia)  # Student(first_name='Julia', last_name='Doe', email='julia.doe@uni.edu')


# Task 03
"""
Создайте дата-класс Product, который хранит информацию о названии продукта и о его цене. 
При выводе товара должна отображаться только информация о его имени. 
Обязательно назовите name атрибут, который хранит название. Цену товара можете назвать как хотите

Затем создайте класс продуктовой корзины Cart, в котором должна быть реализована возможность:
добавлять товары в корзины при помощи метода add_product. 
Добавляется один продукт за один вызов метода
 
посчитать общую сумму содержащихся товаров в корзине при помощи метода get_total
 
возможность применить скидку через apply_discount. 
Данный метод должен принимать размер скидки - целое число от 1 до 100, обозначающее % от цены, 
и сохраняет его в экземпляре класса. 

Если передать любое другое значение, то нужно вызывать исключение:
raise ValueError('Неправильное значение скидки')
Данный метод возвращать ничего не должен

"""
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float = field(repr=False)

@dataclass
class Cart:
    discount: int = field(default=1)
    basket: list = field(default_factory=list)

    def add_product(self, obj):
        if isinstance(obj, Product):
            self.basket.append(obj)

    def get_total(self):
        return sum(el.price for el in self.basket) * self.discount

    def apply_discount(self, sale):
        if type(sale) == int:
            if 0 < sale <= 100:
                self.discount = (100 - sale) / 100
            else:
                raise ValueError('Неправильное значение скидки')

# Код для проверки
product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print(f"Стоимость товаров в корзине без скидки: {cart.get_total()}")
# Применение скидки 10%
cart.apply_discount(10)
print(f"Стоимость товаров в корзине со скидкой 10%: {cart.get_total()}")


# Task 04
"""
Дальнейшая разаработка  Task 03
создать дата-класс Promo, который содержит код промокода и значение его скидки.
Все активные промокоды будут находиться в глобальной переменной ACTIVE_PROMO.

Проверьте, чтобы значение скидки было целым числом и находилось в пределах от 1 до 100, 
обозначает % от цены. При всех остальных значениях будем считать, что промокод не дает скидку 
(как вариант,  можете указать, что значение скидки составляет 0)  

Добавить метод apply_promo в классе Cart, 
который получает на вход код промокода и заведен  ли в переменной ACTIVE_PROMO промокод с таким названием. 
Если существует, то необходимо применить его номинал к корзине товаров. 
Сам метод apply_promo ничего не возвращает, 
только печатает текст "Промокод <promo> успешно применился" или "Промокода <promo> не существует"

А вот при вызове метода get_total должен учитываться промокод или скидка, если они были применены.

Примечание: промокод нельзя использоваться вместе со скидкой. Используется последнее значение, которое применилось.
"""
from dataclasses import dataclass, field

@dataclass
class Promo:
    name: str
    discount: int

    def __post_init__(self):
        if type(self.discount) == int:
            if 0 < self.discount <= 100:
                self.discount = self.discount
        else:
            self.discount = 0

@dataclass
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Cart:
    discount: int = field(default=1)
    basket: list = field(default_factory=list)

    def add_product(self, obj):
        if isinstance(obj, Product):
            self.basket.append(obj)

    def get_total(self):
        return sum(el.price for el in self.basket) * self.discount

    def apply_discount(self, sale):
        if type(sale) == int:
            if 0 < sale <= 100:
                self.discount = (100 - sale) / 100
            else:
                raise ValueError('Неправильное значение скидки')

    def apply_promo(self, code):
        flag = True
        for el in ACTIVE_PROMO:
            if el.name == code:
                self.apply_discount(el.discount)
                print(f"Промокод {code} успешно применился")
                flag = False
                break
        if flag:
            print(f"Промокода {code} не существует")

# Код для проверки. Общее начало
ACTIVE_PROMO = [
    Promo('new', 20),
    Promo('all_goods', 30)
]
product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)
# Product(name='Книга') Product(name='Флешка') Product(name='Ручка')
cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total()) # 160.0

# # Код для проверки 1
# # Применение промокода в 30%
# cart.apply_promo('all_goods')
# print(cart.get_total()) # 112.0

# # Код для проверки 2
# # Применение промокода в 30%
# cart.apply_promo('all_goods')
# # Промокод all_goods успешно применился
# print(cart.get_total())   # 112.0
# # Применение скидки в 10%. Промокод должен отмениться
# cart.apply_discount(10)
# print(cart.get_total())  # 144.0

# # Код для проверки 3
# # Применение несуществующего промокода
# cart.apply_promo('goods')  # Промокода goods не существует
# print(cart.get_total())  # 160.0


# Task 05
"""
Дальнейшая разаработка  Task 04
Добавить новый тип промокода. 
Идея его заключается в том, что он распространяется только на определенные товары в корзине. 

Доработать дата-класс Promo, чтобы он мог принимать список товаров, на который будет распространяться промокод. 
Если список товаров не передать при создании, то данный промокод применяется ко всей корзине целиком. 

Также необходимо доработать метод add_product в классе Cart. 
Необходимо добавить возможность передавать в него количество товара, которое добавляется в корзину (по умолчанию = 1).
"""
from dataclasses import dataclass, field

@dataclass
class Promo:
    name: str
    discount: int = None
    discounted: list = field(default_factory=list)  # Товары с индивидуальной скидкой

    def __post_init__(self):
        if type(self.discount) == int:
            if 0 < self.discount <= 100:
                self.discount = self.discount
            else:
                self.discount = 0

@dataclass
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Cart:
    discount_all: int = field(default=1)  # Скидка на все товары
    basket: list = field(default_factory=list)

    def add_product(self, obj, cnt=1, promo=1):  # Товар, Количество, Скидка товара
        if all([isinstance(obj, Product), type(cnt) == int, cnt > 0]):
            self.basket.append([obj, cnt, promo])

    def get_total(self):
        return sum(el[0].price * el[1] * el[2] for el in self.basket) * self.discount_all

    def apply_discount(self, sale: int, discounted: list = []):
        if all([type(sale) == int, 0 < sale <= 100]):
            if not len(discounted):
                self.discount_all = (100 - sale) / 100
                for el in self.basket:  # Удаление ранее установленных индивидуальных скидок
                    el[2] = 1
            else:
                self.discount_all = 1  # Удаление ранее установленной общей скидки
                promo_goods = [el.name for el in discounted]  # Имена товаров с индивидуальной скидкой
                for el in self.basket:
                    if el[0].name in promo_goods:
                        el[2] = (100 - sale) / 100 # Установление индивидуальной скидки
        else:
            raise ValueError('Неправильное значение скидки')

    def apply_promo(self, code):
        flag = True
        for el in ACTIVE_PROMO:
            if el.name == code:
                self.apply_discount(el.discount, el.discounted)
                print(f"Промокод {code} успешно применился")
                flag = False
                break
        if flag:
            print(f"Промокода {code} не существует")


# Код для проверки. Общее начало
book = Product('Книга', 100.0)
usb = Product('Флешка', 50.0)
pen = Product('Ручка', 10.0)

# Код для проверки 1
ACTIVE_PROMO = [
    Promo('new', 20, [pen]),
    Promo('all_goods', 30),
]
cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print(cart.get_total()) # 1010.0
cart.apply_promo('all_goods')
print(cart.get_total())  # 707.0
# Применение промокода в 20% на ручку
cart.apply_promo('new')
print(cart.get_total())  # 1008.0
cart.apply_promo('all_goods')
print(cart.get_total())  # 707.0


# # Код для проверки 2
# ACTIVE_PROMO = [
#     Promo('new', 20, [pen]),
#     Promo('all_goods', 30),
#     Promo('only_book', 40, [book]),
# ]
# cart = Cart()
# cart.add_product(book, 10)
# cart.add_product(pen)
# print(cart.get_total())
# # Применение промокода в 40% на книгу
# cart.apply_promo('only_book')
# print(cart.get_total())

# # Код для проверки 3
# ACTIVE_PROMO = [
#     Promo('new', 20, [pen]),
#     Promo('all_goods', 30),
#     Promo('only_book', 40, [book]),
# ]
# cart = Cart()
# cart.add_product(book, 10)
# cart.add_product(pen)
# cart.add_product(usb, 5)
# print(cart.get_total())
# # Применение промокода в 30% на все
# cart.apply_promo('all_goods')
# print(cart.get_total())

# # Код для проверки 4
# ACTIVE_PROMO = [
#     Promo('new', 20, [pen]),
#     Promo('all_goods', 30),
#     Promo('only_book', 40, [book]),
# ]
# cart = Cart()
# cart.add_product(book, 10)
# cart.add_product(pen)
# cart.add_product(usb, 5)
# print(cart.get_total())
# # Применение промокода в 30% на все
# cart.apply_promo('all_goods')
# # Применение промокода в 50% на все
# cart.apply_discount(50)
# print(cart.get_total())