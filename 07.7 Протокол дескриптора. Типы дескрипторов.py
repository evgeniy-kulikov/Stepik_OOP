# 7.7 Протокол дескриптора. Типы дескрипторов
""""""

"""
дескрипторы: позволяют перегружать магические методы, 
чтобы изменять поведение объектов на лету при обращении через точку к атрибутам.
"""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте дескриптор MaxLengthAttribute,
который возвращает имя самого длинного атрибута в экземпляре.
Если несколько атрибутов имеют одинаковую длину, необходимо вернуть значение, 
стоящее последним по лексикографическому порядку без учета регистра букв.
Если у экземпляра отсутствуют свои собственные атрибуты, необходимо вернуть None.
"""
class MaxLengthAttribute:
    def __get__(self, instance, owner):
        if instance.__dict__:
            return sorted(instance.__dict__.keys(), key=lambda x: (len(x), x))[-1]
        return None


# Код для проверки
class MyClass:
    max_length_attribute = MaxLengthAttribute()

obj = MyClass()
obj.name = "Vasiliy"
obj.city = "Saint Peterburg"
obj.zountry = "Rus"
obj.jountry = "Rus"
obj.country = "Rus"
print(obj.max_length_attribute)


# Task 02
"""
Создайте дескриптор RangeValidator, который валидирует значение на принадлежность к определенному интервалу. 
При инициализации класс RangeValidator получает значение начала и конца интервала.

При попытке сохранить нечисловое значение в дескриптор, необходимо вызывать исключение :
TypeError('Неправильный тип данных')

При попытке сохранить значение в дескриптор, которое не принадлежит интервалу, 
необходимо вызывать исключение: 
ValueError(f'Значение должно быть между <начало_интервала> и <конец_интервала>')
"""
class RangeValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    # def __set_name__(self, owner, name):
    #     self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Неправильный тип данных')
        if not self.min_length < value < self.max_length:
            raise ValueError(f"Значение должно быть между {self.min_length} и {self.max_length}")
        # instance.__dict__[self.name] = value

    # def __get__(self, instance, owner):
    #     if instance is None:
    #         return self
    #     else:
    #         return instance.__dict__.get(self.name, None)


# Код для проверки
class Temperature:
    celsius = RangeValidator([-100, 100], 'string')
    kelvin = RangeValidator(0, 273)

temp = Temperature()
try:
    temp.kelvin = 500
except ValueError as ex:
    print(ex)  # Значение должно быть между 0 и 273

try:
    temp.celsius = [1, 2]
except TypeError as ex:
    print(ex)  # Неправильный тип данных



# Task 03
"""

"""
class StringValidation:
    def __init__(self, min_length=None, max_length=None, exclude_chars=None, is_same_register=False):
        self.min_length = min_length
        self.max_length = max_length
        self.exclude_chars = exclude_chars
        self.is_same_register = is_same_register

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки')
        if self.min_length is not None:
            if len(value) < self.min_length:
                raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                                 f'быть не меньше {self.min_length} символов')
        if self.max_length is not None:
            if len(value) > self.max_length:
                raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                                 f'быть не больше {self.max_length} символов')
        if self.exclude_chars is not None:
            if any([el in self.exclude_chars for el in value]):
                raise ValueError(f'Имеются недопустимые символы в атрибуте {self.attribute_name}')
        if self.is_same_register:
            st = ''.join(value.split())
            if not any([st.islower(), st.isupper()]):
                raise ValueError(f'Все буквы должны быть в одном регистре в атрибуте {self.attribute_name}')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'calling __get__ for {self.attribute_name}')
            return instance.__dict__.get(self.attribute_name, None)

# Исходный код
# class StringValidation:
#     def __init__(self, min_length):
#         self.min_length = min_length
#
#     def __set_name__(self, owner_class, attribute_name):
#         self.attribute_name = attribute_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки')
#         if len(value) < self.min_length:
#             raise ValueError(f'Длина атрибута {self.attribute_name} должна '
#                              f'быть не меньше {self.min_length} символов')
#         instance.__dict__[self.attribute_name] = value
#
#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         else:
#             print(f'calling __get__ for {self.attribute_name}')
#             return instance.__dict__.get(self.attribute_name, None)

# Код для проверки
class Person:
    name = StringValidation(is_same_register=True, exclude_chars='tyur', max_length=15, min_length=5)
    last_name = StringValidation(max_length=15, min_length=5, is_same_register=True, exclude_chars='!^&%^@%')

p = Person()
try:
    p.name = 'MICHAIL SECOND'
except ValueError as ex:
    print(ex)  # calling __get__ for name
try:
    p.last_name = 'lermontov'
except ValueError as ex:
    print(ex)  # calling __get__ for last_name
print(p.name, p.last_name)  # MICHAIL SECOND lermontov

