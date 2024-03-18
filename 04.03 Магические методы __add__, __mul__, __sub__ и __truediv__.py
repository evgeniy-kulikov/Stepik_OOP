# 4.3 Магические методы __add__, __mul__, __sub__ и __truediv__
""""""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Rectangle, который имеет следующие методы:

метод __init__, 
который устанавливает значения атрибутов width и height: ширина и высота прямоугольника

магический метод __add__, 
который описывает сложение двух прямоугольников. 
Результатом такого сложения должен быть новый прямоугольник, 
в котором ширина и высота получились в результате сложения исходных прямоугольников. 
Новый прямоугольник нужно вернуть в качестве результата вызова метода __add__. 
Сложения с другими типами данных реализовывать не нужно

магический метод __str__, 
который возвращает строковое представление  прямоугольника в следующем виде:
Rectangle({width}x{height})
"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Должен быть классом Rectangle")
        return self.__class__(self.width.__add__(other.width), self.height.__add__(other.height))

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"
        # return f"{self.__class__.__name__}({self.width}x{self.height})"


# Код для проверки
r1 = Rectangle(5, 10)
assert r1.width == 5
assert r1.height == 10
print(r1)

r2 = Rectangle(20, 5)
assert r2.width == 20
assert r2.height == 5
print(r2)

r3 = r2 + r1
assert isinstance(r3, Rectangle)
assert r3.width == 25
assert r3.height == 15
print(r3)


# Task 02
"""
Создайте класс  Order, который имеет следующие методы:

метод __init__, 
который устанавливает значения атрибутов cart и customer: список покупок и имя покупателя
 
магический метод __add__, 
который описывает добавления товара в список покупок. 
Результатом такого сложения должен быть новый заказ, 
в котором все покупки берутся из старого заказа и в конец добавляется новый товар. 
Покупатель в заказе остается прежним
 
магический метод __radd__, 
который описывает добавления товара в список покупок при правостороннем сложении. 
Результатом такого сложения должен быть новый заказ, 
в котором все покупки берутся из старого заказа и в начало списка покупок добавляется новый товар. 
Покупатель в заказе остается прежним

магический метод __sub__, 
который описывает исключение товара из списка покупок. 
Результатом вычитания должен быть новый заказ
 
магический метод __rsub__, 
который описывает исключение товара из списка покупок при правостороннем вычитании. 
Результатом должен быть таким же как и при __sub__
"""
class Order:
    def __init__(self, cart: list, customer: str):
        self.cart = cart
        self.customer = customer

    def __add__(self, other: str):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other: str):
        return Order([other] + self.cart , self.customer)

    def __sub__(self, other: str):
        if other in self.cart:
            self.cart.remove(other)
        return Order(self.cart, self.customer)

    def __rsub__(self, other):
        return self.__sub__(other)


# Код для проверки
order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')


# Task 03
"""
Создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

конструктор __init__, принимающий произвольное количество аргументов. 
Среди всех переданных аргументов необходимо оставить только целые числа 
и сохранить их в атрибут values в виде списка. 
Причем значения должны хранится в порядке неубывания. 
В случае, если целых чисел не передано, нужно в атрибут values сохранять пустой список; 

переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. 
При этом значения должны быть упорядочены по возрастанию;
"Пустой вектор", если наш вектор не хранит в себе значения

переопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться
с целым числом, в результате должен получиться новый Vector, 
у которого каждый элемент атрибута values увеличен на число
с другим вектором такой же длины. 
В результате должен получиться новый Vector, состоящий из суммы элементов, 
расположенных на одинаковых местах. Если длины векторов различаются, 
выведите сообщение "Сложение векторов разной длины недопустимо";
В случае, если вектор складывается с другим типом(не числом и не вектором), 
нужны вывести сообщение "Вектор нельзя сложить с <значением>"

переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
на целое число. В результате должен получиться новый Vector, 
у которого каждый элемент атрибута values умножен на переданное число;
на другой вектор такой же длины. В результате должен получиться новый Vector, 
состоящий из произведения элементов, расположенных на одинаковых местах. 
Если длины векторов различаются, выведите сообщение "Умножение векторов разной длины недопустимо";
В случае, если вектор умножается с другим типом(не числом и не вектором), 
нужны вывести сообщение "Вектор нельзя умножать с <значением>";
"""
class Vector:
    def __init__(self, *args):
        if args:
            self.values = sorted([el for el in args if type(el) == int])
        else:
            self.values = []

    def __add__(self, other):
        if type(other) == int:
            return Vector(*[el + other for el in self.values])
        elif isinstance(other, Vector):
            if len(self) == len(other):
                return Vector(*[sum(el) for el in zip(self.values, other.values)])
            else:
                print("Сложение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if type(other) == int:
            return Vector(*[el * other for el in self.values])
        elif isinstance(other, Vector):
            if len(self) == len(other):
                return Vector(*[a * b for a, b in zip(self.values, other.values)])
            else:
                print("Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")

    def __len__(self):
        return len(self.values)

    def __str__(self):
        if self.values:
            return f"Вектор({', '.join(map(str, self.values))})"
        return 'Пустой вектор'


# Код для проверки
v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
assert isinstance(v5, Vector), 'Результатом сложения должен быть новый Vector'
print('Good')
