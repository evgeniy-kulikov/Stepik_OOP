#  3.5 Публичные, приватные, защищенные атрибуты и методы
""""""

"""
ПУБЛИЧНЫЙ (public)
В Python каждый атрибут класса или экземпляра класса является публичным по умолчанию. 
Они могут быть доступны из любой точки за пределами класса.

ЗАЩИЩЁННЫЙ (protected)
Защищенный (protected) режим
Защищенный режим не закрывает доступ к методам и атрибутам класса. 
Однако существует соглашение в сообществе питонистов: имя с префиксом подчеркивания, 
например _money, следует рассматривать как закрытую часть API 
(будь то функция, метод или элемент данных) для внутреннего служебного использования. 
И именно нижним подчёркиванием в названии атрибута или метода 
мы передаём информацию другому разработчику о том, что перед ним protected атрибут или метод 
и его не следует использовать вне класса. Но все это работает только на уровне соглашений, 
и protected атрибуты и методы остаются доступными вне классов.
"""
class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name         # нижним подчеркиванием указываем
        self._balance = balance   # что атрибут должен быть защищен
        self._passport = passport # от публичного доступа

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

account1 = BankAccount('Bob', 100000, 45484564654)
account1.print_protected_data()  # Bob 100000 45484564654
print(account1._name)  # Bob
print(account1._balance)  # 100000
print(account1._passport)  # 45484564654


"""
Приватный (private) режим
Ограничивает доступ вне класса. Приватные методы создаются при помощи двух нижних подчёркиваний, 
тем самым указывая на приватность атрибута или метода.

Такое сокрытие обработки защищенных атрибутов называется инкапсуляция: 
мы ограждаем всех, кто пользуется нашим классом BankAccount от доступа к защищенным атрибутам, 
но внутри самого класса доступ к ним неограничен. 
А для работы с защищенными атрибутами мы предоставляем пользователю открытый метод 
print_private_data для работы с данными, 
без возможности непосредственного воздействия на защищенные атрибуты.
"""
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):  # доступ к защищенным атрибутам через разрешенный метод:
        return self.__name, self.__balance, self.__passport


account1 = BankAccount('Bob', 100000, 45484564654)
print(account1.print_private_data())  # ('Bob', 100000, 45484564654)
print(account1.__name)  # AttributeError: 'BankAccount' object has no attribute '__name'

"""
Аналогичная ситуация и с приватным методом: 
вне класса нельзя обратиться к его имени, внутри класса мы можем это сделать. 
В примере ниже мы вызываем приватный метод __print_private_data внутри открытого метода public_call
"""
class BankAccount:

    def __init__(self, name, balance, passport):
      self.__name = name
      self.__balance = balance
      self.__passport = passport

    def public_call(self):
      print('work public method')
      self.__print_private_data()

    def __print_private_data(self):
      print('work private method')
      print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
account1.public_call()
# work public method
# work private method
# Bob 100000 45484564654

"""
При желании, обратиться к приватным атрибутам в обход разрешенного доступа 
через метод print_private_data вполне возможно. 
Для этого мы можем узнать список имен, доступных в нашем классе,  при помощи функции dir:
"""
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def public_call(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
print(dir(account1))  # просмотр атрибутов нашего экземпляра класса
"""
['_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', 
'_BankAccount__print_private_data', '__class__', '__delattr__', '__dict__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'public_call']


Обратите внимание на такие названия, как:
_BankAccount__balance
_BankAccount__name
_BankAccount__passport
_BankAccount__print_private_data
Именно через них мы сможем получить доступ к приватным данным вне класса:
"""
account1 = BankAccount('Bob', 100000, 45484564654)
print(account1._BankAccount__balance)  # 100000
print(account1._BankAccount__name)  # Bob
print(account1._BankAccount__passport)  # 45484564654
account1._BankAccount__print_private_data()  # Bob 100000 45484564654



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def __calculate_average(self):
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
print(average_calculator._AverageCalculator__calculate_average())


# Task 02
class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass

maker = PizzaMaker()
maker._make_barbecue()
maker._PizzaMaker__make_pepperoni()


# Task 03
class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Направление: {self.__branch}")

    def access_private_method(self):
        self.__display_details()

# Код для проверки
adam = Student("Adam Smith", 25, "Information Technology")
adam.access_private_method()
adam._Student__display_details()


# Task 04
"""
Создайте класс BankDeposit, который имеет следующие методы:
* метод __init__, который устанавливает значения атрибутов name, balance и rate: 
  владелец депозита, значение депозита и годовая процентная ставка.
* приватный метод __calculate_profit, который возвращает количество денег, 
  которое заработает владелец счета через год с учетом его годовой ставки.
* публичный метод get_balance_with_profit, который возвращает общее количество средств, 
  которое будет у владельца депозита через год.
"""
class BankDeposit:
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * self.rate * 0.01


    def get_balance_with_profit(self):
        return self.__calculate_profit() + self.balance

# Код для проверки
account = BankDeposit("John Connor", 1000, 5)
assert account._BankDeposit__calculate_profit() == 50.0
assert account.get_balance_with_profit() == 1050.0
print('Good')


# Task 05
"""
Создайте класс Library, который имеет следующие методы:
* метод __init__, который принимает список названий книг и сохраняет его в приватном атрибуте __books.
* приватный метод check_availability, который принимает название книги и возвращает True, 
  если книга присутствует в библиотеке, в противном случае возвращается False.
* публичный метод search_book, который ищет книгу в библиотеке при помощи приватного метода check_availability. 
  Возвращает True, если нашел,  иначе False.
* публичный метод return_book, который принимает название книги, которую нужно вернуть в библиотеку 
  (добавить в конец атрибута __books), ничего возвращать не нужно.
* защищенный метод checkout_book, который принимает на вход название книги. Если книга имеется в наличии, 
  ее необходимо выдать читателю и удалить из списка книг. Метод в таком случае должен вернуть True , 
  как знак того, что операция выдачи книги прошла успешно. Если книга отсутствовала, необходимо вернуть False.
"""
class Library:
    def __init__(self, books: list):
        self.__books = books

    def __check_availability(self, book):
        return book in self.__books

    def search_book(self, book):
        return self.__check_availability(book)

    def return_book(self, book):
        self.__books.append(book)

    def _checkout_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            return True
        return False

    # def _checkout_book(self, book):
    #     is_exist = self.__check_availability(book)
    #     if is_exist:
    #         self.__books.remove(book)
    #     return is_exist


# Код для проверки
library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
assert library.search_book("Moby-Dick") == True
assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]
assert library.return_book("Moby-Dick") is None
print('Good')


# Task 06
"""
Создайте класс Employee, который имеет следующие методы:
* метод __init__, который устанавливает значения атрибутов name, __position, __hours_worked и __hourly_rate.
* приватный метод calculate_salary, который считает зарплату сотрудника, умножая отработанные часы на часовую оплату. 
  Метод должен вернуть посчитанную зарплату.
* защищенный метод _set_position, который принимает название должности и 
  изменяет пользователю значение атрибута __position.
* публичный метод get_position, который возвращает атрибут __position.
* публичный метод get_salary, который возвращает результат вызова приватного метода calculate_salary.
* публичный метод get_employee_details, который возвращает информацию о работнике в виде следующий строки
"Name: {name}, Position: {position}, Salary: {salary}"

Здесь значение salary должно рассчитываться при помощи приватного метода calculate_salary.
"""
class Employee:
    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def _set_position(self, new_position):
        self.__position = new_position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"


# Код для проверки
employee = Employee("Джеки Чан", 'manager', 20, 40)
assert employee.name == 'Джеки Чан'
assert employee._Employee__hours_worked == 20
assert employee._Employee__hourly_rate == 40
assert employee._Employee__position == 'manager'
assert employee.get_position() == 'manager'
assert employee.get_salary() == 800
assert employee._Employee__calculate_salary() == 800
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
employee._set_position('Director')
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'
print('Good')
