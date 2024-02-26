#  2.3 Атрибуты экземпляра класса
""""""

# *  *  *  *  *   Task   *  *  *  *  *

# Task 01
class SuperHero:
    pass

batman = SuperHero()
superman = SuperHero()

batman.can_fly = False
batman.damage = 175

superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'


# Task 02
"""
Имеется пустой класс Config. Написать функцию create_instance, 
которая принимает на вход положительное число N. 
Функция должна создать ЭК , создать у него N атрибутов и вернуть в качестве ответа полученный ЭК.

Атрибуты, должны называться определенным образом и иметь определенное значение. 
В общем виде это можно записать так:
attribute<n> = "value<n>"
"""
class Config:
    pass


def create_instance(n: int) -> Config:
    pass


def create_instance(n: int) -> Config:
    obj = Config()
    for el in range(1, n + 1):
        setattr(obj, f'attribute{el}', f'value{el}')
    return obj

# Ниже расположены проверки для функции create_instance

config_2 = create_instance(2)
assert isinstance(config_2, Config)
assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}

config_4 = create_instance(4)
assert isinstance(config_4, Config)
assert config_4.__dict__ == {'attribute1': 'value1',
                             'attribute2': 'value2',
                             'attribute3': 'value3',
                             'attribute4': 'value4'}

config_7 = create_instance(7)
assert isinstance(config_7, Config)
assert config_7.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
                             'attribute3': 'value3', 'attribute4': 'value4',
                             'attribute5': 'value5',
                             'attribute6': 'value6',
                             'attribute7': 'value7'}

config_10 = create_instance(10)
assert isinstance(config_10, Config)
assert config_10.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
                              'attribute3': 'value3', 'attribute4': 'value4',
                              'attribute5': 'value5', 'attribute6': 'value6',
                              'attribute7': 'value7', 'attribute8': 'value8',
                              'attribute9': 'value9', 'attribute10': 'value10'}

print('good')