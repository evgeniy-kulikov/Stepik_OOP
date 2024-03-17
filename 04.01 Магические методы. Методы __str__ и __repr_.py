#  4.1 Магические методы. Методы __str__ и __repr__
""""""

"""
Метод __str__ предназначен для создания строкового представления объекта, 
которое лучше подходит для чтения человеком. 
Он вызывается функцией str() или при попытке вывести объект с помощью функции print(). 
Метод __str__ должен возвращать строку, которая описывает объект в удобном для чтения формате.

Метод __repr__ предназначен для создания строкового представления объекта, 
которое воспроизводит его точное представление. 
Он вызывается функцией repr()  для получения объекта обратно из строки. 
Метод __repr__ должен возвращать строку, которая содержит действительный код Python, 
позволяющий создать точную копию объекта.

Когда мы выводим объект с помощью функции print(), она обычно использует метод __str__, если он определен. 
Если метод __str__ отсутствует, то будет использован метод __repr__. 
Однако, если мы вызываем функцию repr() напрямую или выводим объект в интерактивной оболочке, 
то будет использован метод __repr__.

Таким образом, разница между __str__ и __repr__ заключается в целях использования:
__str__ предназначен для представления объекта в читаемой форме
__repr__ предназначен для представления объекта в точном и воспроизводимом виде


user = User("Vasya", "Pypkin")
print(f"{repr(user)}")
# или лучше воспользоваться !r
print(f"{user!r}")
"""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Person, у которого есть:
конструктор __init__, принимающий 3 аргумента: name, surname, gender. 
Атрибут gender может принимать только 2 значения: «male» и «female», по умолчанию «male». 
Если в атрибут gender передается любое другое значение, печатать сообщение: 
«Не знаю, что вы имели в виду? Пусть это будет мальчик!» 
и проставить атрибут gender значением «male»
 
переопределить метод __str__ следующим образом: 
если объект - мужчина (атрибут gender = «male»), возвращать строку «Гражданин <Фамилия> <Имя>»
если объект - женщина (атрибут gender = «female»), возвращать строку «Гражданка <Фамилия> <Имя>»
"""
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender in ['female', 'male']:
            self.gender = gender
        else:
            print("Не знаю, что вы имели в виду? Пусть это будет мальчик!")
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        return f"Гражданка {self.surname} {self.name}"

# Код для проверки

p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели в виду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"
print('Good')


# Task 02
"""
Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

конструктор __init__, принимающий произвольное количество аргументов. 
Среди всех переданных аргументов необходимо оставить только целые числа 
и сохранить их в атрибут values в виде списка;
 
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
- «Вектор(<value1>, <value2>, <value3>, ...)», если вектор не пустой. 
  При этом значения должны быть упорядочены по возрастанию.
- «Пустой вектор», если наш вектор не хранит в себе значения
"""
class Vector:

    def __init__(self, *args):
        self.values = [el for el in args if type(el) == int]

    def __str__(self):
        if self.values:
            return f"Вектор({', '.join(map(str, sorted(self.values)))})"
            # return f"Вектор({', '.join([str(el) for el in sorted(self.values)])})"
        return f"Пустой вектор"


# Код для проверки
v1 = Vector(1, 2, 3)
assert isinstance(v1, Vector)
assert str(v1) == 'Вектор(1, 2, 3)'
v2 = Vector()
assert isinstance(v2, Vector)
assert str(v2) == 'Пустой вектор'
v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
assert isinstance(v3, Vector)
assert sorted(v3.values) == [1, 2, 3]
assert str(v3) == 'Вектор(1, 2, 3)'
v4 = Vector([4, 5], 'hello')
assert str(v2) == 'Пустой вектор'
assert v2.values == []
v5 = Vector(1, 2, True)
assert isinstance(v5, Vector)
assert str(v5) == 'Вектор(1, 2)'
print(v1)
print(v2)
print(v3)
print(v4)
print('Good')


# Task 03
"""
Создайте класс GroceryItem, который имеет следующие методы:

метод __init__, который устанавливает значения атрибутов name, price и quantity: 
название товара, его цену и количество

магический метод __str__, который возвращает строковое представление товара в следующем виде:
Name: {name}
Price: {price}
Quantity: {quantity}
 
магический метод __repr__, который возвращает однозначное строковое представление объекта
GroceryItem({name}, {price}, {quantity})
"""
class GroceryItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
        # return f"GroceryItem({self.name}, {self.price}, {self.quantity})"


# Код для проверки
banana = GroceryItem('Banana', 10, 5)
assert banana.__str__() == """Name: Banana
Price: 10
Quantity: 5"""
assert repr(banana) == 'GroceryItem(Banana, 10, 5)'
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
assert dragon_fruit.__str__() == """Name: Dragon fruit
Price: 5
Quantity: 350"""
assert repr(dragon_fruit) == 'GroceryItem(Dragon fruit, 5, 350)'
print(dragon_fruit)
print(f"{dragon_fruit!r}")
print('Good')
