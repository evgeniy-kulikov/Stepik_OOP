# 3.6 Геттеры и сеттеры, property атрибуты
""""""

"""
Гораздо приятнее обращаться к геттерам и сеттерам, словно они атрибуты. 
Для этого вам необходимо определить геттер и сеттер, как свойство, при помощи property

property  — это функция, которая позволяет вам превращать атрибуты класса в свойства или управляемые атрибуты. 
Поскольку property() — это встроенная функция, вы можете использовать ее, ничего не импортируя.

Примечание. Обычно property называют встроенной функцией. 
Однако property — это класс, предназначенный для работы как функция, а не как обычный класс. 
Вот почему большинство разработчиков Python называют это функцией. 
Это также причина, по которой property() не следует соглашению Python по именованию классов.
С помощью property вы можете прикрепить методы получения (getter) и установки (setter) к заданным атрибутам класса. 
Таким образом, вы можете обрабатывать внутреннюю реализацию этого атрибута, 
не раскрывая методы получения и установки в вашем API. 
Вы также можете указать способ обработки удаления атрибута 
и предоставить соответствующую строку документации для ваших свойств.


property(fget=None, fset=None, fdel=None, doc=None)

Параметры:

fget=None — функция для получения значения атрибута
fset=None — функция для установки значения атрибута
fdel=None — функция для удаления атрибута
doc=None — строка, для строки документации атрибута

Возвращаемое значение property — это сам управляемый атрибут. 
Когда вы обращаетесь к управляемому атрибуту, как в obj.attr, 
тогда Python автоматически вызывает fget(). Когда вы присваиваете атрибуту новое значение, 
как в obj.attr = value, тогда Python вызывает fset(), используя входное значение в качестве аргумента. 
Наконец, если вы запустите оператор del obj.attr, то Python автоматически вызовет fdel().

Примечание. Первые три аргумента функции property должны принимать функциональные объекты. 
Вы можете думать об объекте функции как об имени функции без вызывающей пары круглых скобок.
Четвертым аргументом вы можете передать строку документации doc для вашего свойства.
"""

class Person:
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        self._name = value

    def _del_name(self):
        del self._name

    name = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="The name property."
    )

person = Person('Jack')
person.name  # Jack

person.name = 'Tom'
person.name  # Tom

del person.name
person.name  # AttributeError: 'Person' object has no attribute '_name'

# *  *  *  *  *   Task   *  *  *  *  *

# Task 01
class BankAccount():
    def __init__(self, number, balance):
        self._account_number = number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance



# Task 02
"""
Создайте класс Employee, который имеет следующие методы:

* метод __init__, который устанавливает значения приватных атрибутов __name  и __salary: имя работника и его зарплату
* приватный геттер метод для атрибута __name
* приватный геттер метод для атрибута __salary
* приватный сеттер метод для атрибута __salary: 
  он должен позволять сохранять в атрибут __salary только положительные числа. 
  В остальных случаях не сохраняем переданное значение в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
* свойство title, у которого есть только геттер из пункта 2.
* свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.
"""
class Employee():
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, salary):
        if type(salary) in (int, float) and salary > 0:  # Защита от передачи в параметр значения True/False
        # if isinstance(salary, (int, float)) and salary > 0:
            self.__salary = salary
        else:
            return print(f"ErrorValue:{salary}")

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)


# Код для проверки
employee = Employee("John Doe", 50000)
assert employee.title == "John Doe"
assert employee._Employee__name == "John Doe"

employee.reward = 70000
assert employee.reward == 70000
employee.reward = 'hello'  # Печатает ErrorValue:hello
employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
assert employee.reward == 70000
employee._Employee__set_salary(55000)
assert employee._Employee__get_salary() == 55000
print('Good')


# Task 03
"""
Создайте класс UserMail, у которого есть:

* конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. 
  Их необходимо сохранить в экземпляр, как атрибуты login и __email (обратите внимание, приватный атрибут).
* метод геттер get_email, который возвращает приватный атрибут __email.
* метод сеттер set_email, который принимает в виде строки новую почту. 
  Метод должен проверять, что в новой почте есть только один символ @ и после нее есть точка. 
  Если данные условия выполняются, новая почта сохраняется в атрибут __email,
  в противном случае выведите сообщение "ErrorMail:<почта>".
* создайте свойство email, у которого геттером будет метод get_email, а сеттером  метод set_email.
"""
import  re
class UserMail():
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        if isinstance(email, str):
            email = ''.join(email.split()) # Проверка на отсутствие пробелов в теле строки
            # if email.count('@') == 1 and '.' in email.split('@')[-1] and email.split('@')[-1].count('.') == 1:
            res = re.match(r'[^@]+@[^@\.]+\.[^@\.]+', email)
            if res is not None:
                self.__email = email
            else:
                return print(f'ErrorMail:{email}')
        else:
            return print(f'ErrorMail:{email}')

    email = property(fget=get_email,
                    fset=set_email)


# Код для проверки
k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
print('Good')
