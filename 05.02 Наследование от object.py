# 5.2 Наследование от object и от других встроенных типов
""""""

"""
Каждый раз, когда вы создаете класс, который не наследуется от другого класса, 
python неявным образом создает наследование нового класса от класса object

Во главе любой иерархии всегда стоит класс object

Класс object — это не просто пустой класс, 
в нем уже реализовано достаточно большое количество атрибутов и методов.
"""
class Person:
    pass

p = Person()

print(issubclass(Person, object))  # True
print(isinstance(p, object))  # True


"""
один класс отличается родителем — это класс bool. Он унаследован от класса int

Это значит, что класс bool наследует поведение целых чисел, 
в частности, можно взять два значения True, сложить и получить в результате 2. 
Можно складывать или умножать значения True/False с другими числами.
"""

"""
type является классом (а не функцией). Вот его определение из python:
Класс type может использоваться для двух целей:
- определение типа объекта
- создание нового типа или класс

Вызов type(instance) возвращает класс, от которого был создан экземпляр.
"""
class type(object):
    """
    type(object) -> the object's type
    type(name, bases, dict, **kwds) -> a new type
    """

class Person:
    pass

p = Person()

print(type(p))  # <class '__main__.Person'>

# Если передавать сам класс и затем вызывать type(class), результатом всегда будет type
print(type(Person))  # <class 'type'>


"""
Атрибут __class__
Способ, который позволяет узнать класс, при помощи которого был создан объект, является атрибут __class__.

Вы можете через точку обратиться к атрибуту __class__ у любого объекта и узнаете его тип.
"""
print((45).__class__)  # <class 'int'>


"""
Атрибут __base__
Атрибут __base__ содержит ссылку на прямого родителя для данного класса. 
Для класса object это значение None. Для класса, у которого явно не задан базовый класс, 
атрибут __base__ будет хранить ссылку на класс object. 
"""
class Person:
    pass

class Doctor(Person):
    pass

print(Person.__base__)  # <class 'object'>
print(Doctor.__base__)  # <class '__main__.Person'>



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
создать метод .remove_all(value), который будет удалять сразу все значения, 
которые равны value. Если value отсутствует в списке, ничего делать не нужно. 
Метод в конце своей работы должен вернуть None
"""
class MyList(list):
    def remove_all(self, value):
        while value in self:
            self.remove(value)


# Код для проверки
s = MyList([1, 2, 3, 2, 1, 2])
assert s == [1, 2, 3, 2, 1, 2]
s.remove_all(2)
assert s == [1, 3, 1]
s.remove_all(1)
assert s == [3]
s.remove_all(5)
assert s == [3]
s.remove_all(3)
assert s == []
k = MyList([0]*20)
assert k == [0]*20
k.remove_all(7)
assert k == [0]*20
k.append(8)
k.append(0)
k.append(2)
k.remove_all(0)
assert k == [8, 2]
assert k.remove_all(0) == None
print('Good')


# Task 02
"""
Создайте класс NewInt, который унаследован от целого типа int, 
то есть мы будем унаследовать поведение целых чисел 
и значит экземплярам нашего класса будут поддерживать те же операции, что и целые числа.

Дополнительно в классе NewInt нужно создать:

метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2), 
обозначающее сколько раз нужно продублировать данное число. 
Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
 
метод to_bin, который возвращает двоичное представление числа в качестве целого числа 
(может пригодиться функция bin или форматирование)
"""
class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])
        # return int(f'{self:b}')
        # return int(bin(self).lstrip("0b"))

# Код для проверки
a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35
print(NewInt())  # 0
print('Good')
