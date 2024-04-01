#  09.1 Перечисления Enum
""""""

"""
Во многих языках программирования, имеется специальный тип данных, 
для хранения конечного набора значений. 
Этот тип данных известен как перечисление или enum(от англ. enumerations).

В стандартной библиотеке Python есть модуль enum, 
поддерживающий перечисления через класс Enum
"""


from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


print(Season.SPRING)  # Season.SPRING
print(Season.SPRING.name)  # SPRING
print(Season.SPRING.value)  # 1

print(Season(3).name)  # AUTUMN  (Доступ к ключу, через его значение)
print( Season['WINTER'].value)  # 4  (Доступ к значению, через ключ)


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
"""
from enum import Enum

class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"

print(Direction.WEST.name)  # WEST
print(Direction.SOUTH.value)  # S


# Task 02
"""
Создать перечисление Size, в котором хранятся размеры одежды:
"""
from enum import Enum

class Size(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"
    XXL = "extra extra large"
