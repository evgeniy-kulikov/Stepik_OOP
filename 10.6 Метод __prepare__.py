# 10.6 Метод __prepare__
""""""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Ниже представлен код, в котором содержится ошибка
По какой то причине в классе MyClass не создались атрибуты weapon и health
Найдите и исправьте ошибку в коде 
"""
# class CustomDict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value)
#
#     def __getitem__(self, key):
#         return int(super().__getitem__(key))
#
# class MyMeta(type):
#     @staticmethod
#     def __prepare__(name, bases):
#         d = CustomDict()
#         d['weapon'] = 'blaster'
#         d['health'] = 100
#         return CustomDict()
#
#     def __new__(cls, name, bases, cls_dict):
#         return super().__new__(cls, name, bases, cls_dict)
#
# class MyClass(metaclass=MyMeta):
#     pass

class CustomDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))


class MyMeta(type):
    @staticmethod
    def __prepare__(name, bases):
        d = CustomDict()
        d['weapon'] = 'blaster'
        d['health'] = 100
        return d

    def __new__(cls, name, bases, cls_dict):
        return super().__new__(cls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta):
    pass


# Код для проверки
assert hasattr(MyClass, 'weapon')
assert hasattr(MyClass, 'health')
print('Good')

