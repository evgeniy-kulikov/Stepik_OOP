# 4.9 Остальные магические методы
""""""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        return self + other
        # return self.__add__(other)

b = BankAccount('vanya', 100)
print(b + 200)  # 300
print(300 + b)  # 400
print(b.balance)  # 100

b += 150
print(b)  # 250
# print(b.balance)  # AttributeError: 'int' object has no attribute 'balance'

# Если нужно, чтобы после сложения по операции += в переменной b
# оставался экземпляр банковского счета с измененной суммой денег, то необходим
# Метод __iadd__
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __iadd__(self, other):
        print('__iadd__')
        if isinstance(other, (int, float)):
            self.balance += other
        return self


b = BankAccount('vanya', 100)
print(id(b), type(b), b.balance)  # 2085137595984 <class '__main__.BankAccount'> 100
b += 150  # __iadd__
print(id(b), type(b), b.balance)  # 2085137595984 <class '__main__.BankAccount'> 250
"""
При операции += python сперва попытается вызвать метод __iadd__ у объекта. 
Если метод __iadd__  у объекта имеется, значит вызывается он. 
Если метод __iadd__ не реализован, то будет вызван метод __add__ для выполнения сложения, 
а затем результат будет присвоен переменной слева от +=
"""

# Если же вы хотите работать с неизменяемыми объектами,
# то вам нельзя менять состояние экземпляра self.
# Но вы можете создать новый экземпляр и вернуть его качестве результата:
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __iadd__(self, other):
        """Возвращает новый объект"""
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented


"""
Метод __contains__
__contains__ 
это магический метод, который позволяет вам проверить, 
присутствует ли определенное значение в объекте или нет. 
Метод __contains__ возвращает логическое значение True, если элемент присутствует в последовательности 
и имеет значение False в противном случае.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.marks = age


john = Student("John", [5, 4, 5, 3, 4])
print(5 in john)  # TypeError: argument of type 'Student' is not iterable

class Student:
    def __init__(self, name, age):
        self.name = name
        self.marks = age

    def __contains__(self, item):
        return item in self.marks


john = Student("John", [5, 4, 5, 3, 4])
print(5 in john)  # True
print(2 in john)  # False



"""
данном случае метод __contains__ вам не поможет. 
Потому что поиск выполняется не в самом объекте Person, 
а в списке: обходятся все элементы списка и значения сравниваются между собой на равенство, 
если равенство (метод __eq__) не реализовано, тогда проверяется на совпадение идентификаторов. 
Поэтому в нашем примере мы будем всегда видеть отрицательный результат проверки. 
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people_list = [Person("John", 25), Person("Tom", 30), Person("Bob", 35)]

if Person("John", 25) in people_list:
    print("Yes, 'John' in people_list")
else:
    print("No, 'John' is not in people_list")
# No, 'John' is not in people_list

"""
определим метод __eq__ и будем сравнивать экземпляры по атрибутам
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

people_list = [Person("John", 25), Person("Tom", 30), Person("Bob", 35)]

if Person("John", 25) in people_list:
    print("Yes, 'John' in people_list")
else:
    print("No, 'John' is not in people_list")
# Yes, 'John' in people_list



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс AttributeChecker, который имеет:
магический метод __contains__, принимающий имя атрибута и возвращает True, 
если этот атрибут существует в экземпляре класса, и False в противном случае.
"""
class AttributeChecker:

    def __contains__(self, item):
        return item in self.__dict__
        # return hasattr(self, item)


# Тест 1: Проверка наличия отсутствующего атрибута
check = AttributeChecker()
assert "name" not in check
assert "age" not in check
setattr(check, 'name', 'Russell')
check.age = 10

# Тест 2: Проверка добавления атрибутов
assert "name" in check
assert "age" in check

# Тест 3: Проверка атрибутов другого ЭК
check_2 = AttributeChecker()
assert "name" not in check_2
assert "age" not in check_2

# Тест 4: Проверка наличия атрибутов после удаления
delattr(check, "name")
assert "name" not in check
assert "age" in check

print("Good")
