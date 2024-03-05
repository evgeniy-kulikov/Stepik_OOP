# 3.7.1 Декоратор Property
""""""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('Get balance')
        return self.__balance

    def set_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('Delete balance')
        del self.__balance

    # создаем свойство balance при помощи функции property,
    # в атрибутах которой мы описываем какой метод должен быть геттером, сеттером и делитером.
    balance = property(fget=get_balance,
                       fset=set_balance,
                       fdel=delete_balance)

    # У объекта  property() есть три метода:
    # .getter() позволяет определить геттер
    # .setter() позволяет определить сеттер
    # .deleter() позволяет определить делитер
    # Аналогичный функционал через вызов методов
    balance = property()
    balance = balance.getter(get_balance)
    balance = balance.setter(set_balance)
    balance = balance.deleter(delete_balance)




"""
Оставим для простоты только геттеры:
В последней строке мы декорируем метод my_balance при помощи функции property. 
После такой манипуляции у экземпляров класса BankAccount доступно только свойство my_balance 
(обратите внимание на букву p перед именем my_balance, она обозначает свойство). 
Метод my_balance в списке имен мы не видим
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def my_balance(self):  # метод
        print('Get balance')
        return self.__balance

    my_balance = property(my_balance)  # свойство


"""
Декораторы — это функции, которые принимают другую функцию в качестве аргумента, 
добавляют к ней некоторую дополнительную функциональность и возвращают функцию с измененным поведением.
Можем воспользоваться синтаксическим сахаром декораторов и переписать код при помощи оператора @
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):  # Теперь это свойство
        print('Get balance')
        return self.__balance

# Будем использовать метод setter для создания сеттера через декоратор
# Главное, чтобы у метода сеттера было тоже самое имя, что и у вашего свойства.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):  # Теперь это свойство
        print('Get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):  # Теперь это свойство
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

"""
Аналогичным образом через имеющееся свойство вызываем метод deleter
в самом декораторе для определения у нашего свойства
Имена всех наших методов имеют одинаковое название my_balance. Это нужно, 
чтобы функциональность геттера, сеттера и делитера находилась в одном свойстве  - my_balance
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('Delete balance')
        del self.__balance


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Celsius, который представляет температуру в градусах Цельсия. 
Задача класса - конвертировать температуру из градусов Цельсия в градусы Фаренгейта, 
а также обеспечить контроль за корректностью введенных значений.

Класс Celsius, должен иметь:
* метод __init__, который принимает значение температуры в градусах по Цельсию и сохраняет в атрибут экземпляра.
* метод to_fahrenheit, который выполняет конвертацию температуры из градусов Цельсия в градусы Фаренгейта по формуле
  °F = (°C × 9/5) + 32
  и возвращает результат этой конвертации.
* свойство-геттер temperature, которое предоставляет доступ к значению температуры
* свойство-сеттер temperature, которое выполняется при установке нового значения температуры. 
  Если значение меньше -273.15 градусов Цельсия (абсолютный ноль), вызывается исключение ValueError. 
  В противном случае, происходит установка нового значения температуры.
"""
class Celsius():
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def temperature(self):
        return self._celsius

    @temperature.setter
    def temperature(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Должно быть число')
        elif value < -273.15:
            raise ValueError('Некоректное значение (меньше -273.15)')
        else:
            self._celsius = value


# Код для проверки
celsius = Celsius(25)
assert celsius.temperature == 25
assert celsius.to_fahrenheit() == 77.0

celsius.temperature = 30
assert celsius.temperature == 30
assert celsius.to_fahrenheit() == 86.0
print('Good')


# Task 02
"""

"""
class File():
    def __init__(self, value):
        self._size_in_bytes = value

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f"{self._size_in_bytes} B"
        elif self._size_in_bytes < 1024 ** 2:
            return F"{self._size_in_bytes / 1024:.2f} KB"
        elif self._size_in_bytes < 1024 ** 3:
            return F"{self._size_in_bytes / 1024 ** 2:.2f} MB"
        elif self._size_in_bytes >= 1024 ** 3:
            return F"{self._size_in_bytes / 1024 ** 3:.2f} GB"

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Должно быть число')
        else:
            self._size_in_bytes = value


# Код для проверки
file = File(5)
assert file.size == "5 B"
file.size = 1023
assert file.size == "1023 B"
file.size = 1024
assert file.size == "1.00 KB"

file_1 = File(1500000)
assert file_1._size_in_bytes == 1500000
assert file_1.size == "1.43 MB"

file_2 = File(1500)
assert file_2.size == "1.46 KB"

file_3 = File(2789326322)
assert file_3.size == "2.60 GB"
file_3.size = 1073741824
assert file_3.size == "1.00 GB"
print('Good')


# Вариант
import copy
class File:
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        size_name = ['B', 'KB', 'MB', 'GB']
        i = 0
        s = copy.copy(self._size_in_bytes)
        while s >= 1024 and i < len(size_name) - 1:
            s /= 1024
            i += 1
        return f"{(self._size_in_bytes, format(self._size_in_bytes / 1024 ** i, '.2f'))[bool(i)]} {size_name[i]}"

    @size.setter
    def size(self, val):
        self._size_in_bytes = val

file = File(1024 ** 5)
print(file.size)