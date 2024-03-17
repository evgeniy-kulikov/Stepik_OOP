# 4.2 Магические методы __len__ и __abs__
""""""

"""
Магический метод __len__ определяет, как объект будет вести себя, 
когда его длина запрашивается с помощью функции len()
"""

# Чтобы класс мог иметь поведение "нахождение длины" необходимо определить метод __len__
# Главное чтобы метод __len__ возвращал целое число не меньше нуля
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __len__(self):
        return len(self.first_name + self.last_name)


john = Person("John", "Doe")
print(len(john))  # 7
print(john.__len__())  # 7


"""
Магический метод __abs__
Определяет поведение операции получения абсолютного значения для объекта.
__abs__ позволяет настраивать, как объект будет вести себя, когда к нему применяется встроенная функция abs()
"""


class Distance:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        print('Call __len__')
        return abs(self)

    def __abs__(self):
        print('Call __abs__')
        return abs(self.point1 - self.point2)


d = Distance(5, 9)
print(len(d))



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Hero, который имеет следующие методы:

метод __len__, который возвращает количество атрибутов экземпляра
 
магический метод __str__, который возвращает строковое представление героя. 
Для этого нужно перечислить все атрибуты в алфавитном порядке на отдельной строке, 
напротив каждого атрибута указать его значение. Вот такой формат должен получится:
атрибут_1: значение_атрибут_1
атрибут_2: значение_атрибут_2
...
атрибут_N: значение_атрибут_N

Если у экземпляра нету атрибутов, необходимо вернуть пустую строку
"""
class Hero:

    def __len__(self):
        return len(self.__dict__)
        # return self.__dict__.__len__()

    def __str__(self):
        if len(self):
            return '\n'.join([f'{k}: {v}' for k, v in sorted(self.__dict__.items())])
        return ''


# Код для проверки
hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
assert str(hero) == '''damage: 10
health: 50'''
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)

villain = Hero()
assert str(villain) == ''
assert len(villain) == 0
villain.level = 15
villain.skill = 'Боец'
villain.armor = 25
assert len(villain) == 3
assert str(villain) == '''armor: 25
level: 15
skill: Боец'''
print(villain)
print('Good')
