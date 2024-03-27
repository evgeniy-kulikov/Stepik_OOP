# 7.1 Абстрактные классы
""""""

"""
Абстрактный класс - это класс, который не предназначен для создания объектов напрямую. 
Он является классом-шаблоном для других классов и определяет абстрактные методы, 
которые должны быть реализованы в дочерних классах. 

Абстрактный класс является абстракцией того, что должны делать его наследники, 
но не определяет, как именно это должно быть сделано.

Абстрактный метод - это метод, который объявлен в абстрактном классе, но не имеет реализации. 
Он служит как бы шаблоном для метода, который должен быть реализован в подклассах. 

В Python абстрактные классы реализуются с помощью модуля abc (аббревиатура от Abstract Base Classes). 
Для создания абстрактного класса нам понадобиться класс ABC, 
а для создания абстрактного метода - декоратор abstractmethod. 
Оба эти объекта импортируются из стандартного модуля abc
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):  # ОБЯЗАНЫ реализовывать
        pass

s = Circle(2)
print(s.area())  # 12.56


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте абстрактный класс Employee, имеющий абстрактный метод calculate_salary().

Реализуйте два класса HourlyEmployee и SalariedEmployee, унаследованные от Employee, 
реализующие метод calculate_salary() для расчета заработной платы по часам и окладу соответственно.

Класс HourlyEmployee при инициализации должен создавать атрибуты hours_worked и hourly_rate. 

Класс SalariedEmployee при инициализации должен создавать только атрибут monthly_salary. 
"""
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Код для проверки
hourly_employee = HourlyEmployee(100, 25)
assert hourly_employee.hours_worked == 100
assert hourly_employee.hourly_rate == 25
assert hourly_employee.calculate_salary() == 2500

salaried_employee = SalariedEmployee(4000)
assert salaried_employee.monthly_salary == 4000
assert salaried_employee.calculate_salary() == 4000
print("Good")


# Task 02
"""
https://stepik.org/lesson/922344/step/7?unit=928230
"""
from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class MySQLDatabase(Database):

    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):

    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")


# Код для проверки
mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

mysql_db.connect()
mysql_db.execute(
    "SELECT * FROM customers;")
mysql_db.disconnect()

postgresql_db.connect()
postgresql_db.execute(
    "SELECT * FROM customers;")
postgresql_db.disconnect()
print("Good")