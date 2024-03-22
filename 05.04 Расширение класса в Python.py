# 5.4 Расширение класса в Python
""""""

"""
Если добавить в дочерний класс новые атрибуты и методы, 
имена котрых отличаются от атрибутов и методов родительского класса, 
то в результате такого добавления получим, 
что в дочернем классе будут доступны все методы и атрибуты родителя плюс свои собственные, 
то есть более расширенное поведение, чем у его родителя"""

# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Переписать код из темы 4.7 Полиморфизм в Python, Task 03 
с учетом наследования.
"""
class Date():
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"


class DateEurope(Date):

    def format(self):
        return f"{self._day:02}/{self._month:02}/{self._year:04}"


class DateUSA(Date):

    def format(self):
        return f"{self._month:02}/{self._day:02}/{self._year:04}"


# Код для проверки
assert issubclass(DateUSA, Date) == True
assert issubclass(DateEurope, Date) == True
d = DateEurope(5, 12, 2001)
print(d.format())
print(d.isoformat())
assert isinstance(d, DateEurope) == True
assert isinstance(d, Date) == True
d = DateUSA(1, 5, 890)
print(d.format())
print(d.isoformat())
assert isinstance(d, DateEurope) == False
assert isinstance(d, Date) == True
assert isinstance(d, DateUSA) == True
print('Good')


# Task 02
"""
Создать базовый класс PrettyPrint, который будет выводить экземпляр любого дочернего класса. 
Формат вывода :
НазваниеКласса(атрибут1=ЗначениеАтрибута1, атрибут2=ЗначениеАтрибута2, ....)
Если у дочернего класса есть собственная реализация метода __str__, то отрабатывать должен именно он.
"""
class PrettyPrint:

    def __str__(self):
        res = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({res})"

# Код для проверки
class Person(PrettyPrint):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

artem = Person('Artem', 'Egorov', 33)
ivan = Person('Ivan', 'Ivanov', 45)
print(artem)  # Person(first_name=Artem, last_name=Egorov, age=33)
print(ivan)  # Person(first_name=Ivan, last_name=Ivanov, age=45)

