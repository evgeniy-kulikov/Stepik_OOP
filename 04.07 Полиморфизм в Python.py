# 4.7 Полиморфизм в Python
""""""

# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Поправьте код так, чтобы все заработало.
"""

class Duck:
    def swim(self):
        print("I'm a duck, and I can swim.")

    def quack(self):
        print("I'm a duck, and I can quack.")


class RoboticBird:
    def swim(self):
        print("I'm a robotic bird, and I can swim.")

    def quack(self):
        print("I'm a robotic bird, and I can quack.")


class Fish:
    def swim(self):
        print("I'm a fish, and I can swim")

    def quack(self):
        print("I'm a fish, and I can't quack")


# Task 02
"""
Создайть классы UnitedKingdom, Spain
"""
class UnitedKingdom:

    @staticmethod
    def get_capital():
        print("London is the capital of Great Britain.")

    @staticmethod
    def get_language():
        print("English is the primary language of Great Britain.")


class Spain:

    @staticmethod
    def get_capital():
        print("Madrid is the capital of Spain.")

    @staticmethod
    def get_language():
        print("Spanish is the primary language of Spain.")


# Task 03
"""
Создайть классы DateUSA, DateEurope
"""
class DateUSA:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format(self):
        return f"{self.month:02}/{self.day:02}/{self.year:04}"

    def isoformat(self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"


class DateEurope:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format(self):
        return f"{self.day:02}/{self.month:02}/{self.year:04}"

    def isoformat(self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"


# Применение наследования
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def isoformat(self):
        return f'{self.year:04}-{self.month:02}-{self.day:02}'


class DateUSA(Date):
    def format(self):
        return f'{self.month:02}/{self.day:02}/{self.year:04}'


class DateEurope(Date):
    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'


# Task 04
"""
Дописать  класс BankAccount таким образом, 
чтобы его экземпляры могли участвовать в операции сортировки списка, 
в котором могут находиться только числа и другие экземпляры класса BankAccount
"""

from functools import total_ordering

@total_ordering
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.balance == other
        if isinstance(other, BankAccount):
            return self.balance == other.balance

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.balance < other
        if isinstance(other, BankAccount):
            return self.balance < other.balance

# Код для проверки
values = [BankAccount('Petrovich', 400), 500, BankAccount('Andrey', 200), 100, BankAccount('Zina', 150)]
values.sort()
print(*values)  # 100 Zina Andrey Petrovich 500


# Task 05
"""
Дописать  классы BankAccount и Numbers таким образом,
чтобы его экземпляры могли участвовать
в операции сложения с числами и c другими экземплярами классов BankAccount и Numbers
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        if isinstance(other, BankAccount):
            return self.balance + other.balance

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return self.name


class Numbers:
    def __init__(self, values: list):
        self._values = values

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return sum(self._values) + other
        if isinstance(other, Numbers):
            return sum(self._values) + sum(other._values)

    def __radd__(self, other):
        return self.__add__(other)


# Реализация только через __radd__
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __radd__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other

    def __str__(self):
        return self.name


class Numbers:
    def __init__(self, values: list):
        self._values = sum(values)

    def __radd__(self, other):
        if isinstance(other, Numbers):
            return self._values + other._values
        if isinstance(other, (int, float)):
            return self._values + other

lst = [1, BankAccount('Tom', 4), 2, Numbers([5, 6]), 3, BankAccount('Tom', 4), Numbers([5, 6])]
print(sum(lst))  # 36

lst = [BankAccount('Tom', 4),  Numbers([5, 6])]
print(sum(lst))  # 15

lst = [Numbers([5, 6]), BankAccount('Tom', 4)]
print(sum(lst))  # 15
