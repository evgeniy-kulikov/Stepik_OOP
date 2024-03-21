# 5.3 Переопределение методов в Python
""""""

"""
Наследование представляет собой очень мощный и крутой механизм, 
помогающий писать код красиво, структурировано и без дублирования. 
Достигается это за счет использования трех методик:
- Переопределение (Overriding)
- Расширение (Extending)
- Делегирование (Delegation)


Переопределение метода («Method overriding») — концепция в ООП, 
позволяющая дочернему классу обеспечивать специфическую (свою собственную) реализацию метода, 
уже реализованного в родительском классе.
"""

"""
Переопределение метода  заключается в создании в 
дочернем классе Doctor метода ровно с таким же названием can_sleep. 
как и у родительского класса.
"""
class Person:
    def can_sleep(self):
        print("Person can sleep")


class Doctor(Person):
    def can_sleep(self):  # Переопределенный метод
        print("Doctor can sleep")



# Обратите внимание на родительский метод combo, цель которого запустить другие методы.
class Person:
    def breath(self):
        print("Человек дышит")

    def walk(self):
        print("Человек ходит")

    def combo(self):
        self.breath()
        self.walk()


class Doctor(Person):

    def breath(self):
        print("ДОКТОР дышит")


a = Doctor()
a.combo()
# ДОКТОР дышит
# Человек ходит

b = Person()
b.combo()
# Человек дышит
# Человек ходит


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Определите дочерние классы Cube и Power4 (возведение в 4-ую степень) от класса Square так, 
чтобы они переопределяли метод get_value() и возвращали результат.
"""
class Square:
    def get_value(self, a):
        return a * a

class Cube(Square):
    def get_value(self, a):
        return a ** 3

class Power4(Square):
    def get_value(self, a):
        return a ** 4

# Код для проверки
assert issubclass(Cube, Square)
assert issubclass(Power4, Square)
cube = Cube()
assert cube.get_value(2) == 8
assert cube.get_value(-17) == -4913
power4 = Power4()
assert power4.get_value(5) == 625
assert power4.get_value(25) == 390625
print('Good')