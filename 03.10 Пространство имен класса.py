#  3.10 Пространство имен класса
""""""

class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    @staticmethod
    def make_backend():
        print('Python and go')

    @staticmethod
    def make_frontend():
        print('Python and go')

it1 = DepartmentIT()

"""
в глобальной области видимости этого модуля будет только два имени:
название класса DepartmentIT и имя переменной it1

для класса DepartmentIT будут доступны следующие имена:
DepartmentIT.PYTHON_DEV
DepartmentIT.GO_DEV
DepartmentIT.REACT_DEV
DepartmentIT.make_backend
DepartmentIT.make_frontend


Атрибут экземпляра тоже имеет доступ к локальной области класса, 
и через него можно получать доступ к атрибутам класса, методам, 
а также к атрибутам экземпляра, которые хранятся в атрибуте __dict__
it1.PYTHON_DEV
it1.GO_DEV
it1.REACT_DEV
it1.make_backend
it1.make_frontend

!!! ВАЖНО  !!!
методы и атрибуты класса находятся на одном уровне в локальной области видимости класса DepartmentIT. 
Это значит, что если имя не будет найдено в методе, 
то далее поиск не осуществляется в локальной области видимости класса, 
а идет сразу в глобальную область модуля.
"""



#  Как  получить доступ к атрибутам внутри метода?

class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def get_info(self):
        """
        Через экземпляр self
        Внутри метода доступна ссылка на экземпляр, через который можно получить доступ к атрибутам класса.
        """
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def get_info_class_name(self):
        """
        Через название самого класса
        Можно прописать название самого класса и затем через точку обратиться к нужному атрибуту.
        """
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @classmethod
    def get_info_class_cls(cls):
        """
        Через класс cls
        В методах класса доступна переменная cls, через которую тоже можно  получать доступ к атрибутам.
        """
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)



class Department:
    PYTHON_DEV = 4
    GO_DEV = 3

    def hiring_python_dev(self):
        self.PYTHON_DEV += 1


it1 = Department()
it1.hiring_python_dev()
it1.hiring_python_dev()
print(it1.PYTHON_DEV) # выводит 6, все нормально
print(Department.PYTHON_DEV) # выводит 4, почему?
# при первом вызове метода создается атрибут экземпляра.
# Его значение высчитывается на основании атрибута класса.
# При втором вызове и последующих — берется значение атрибута экземпляра.


# Атрибут класса как список
class DepartmentIT:
    PYTHON_DEV = []
    # PYTHON_DEV = 4
    GO_DEV = 3

    def hiring_python_dev(self, val):
        # self.PYTHON_DEV += 1
        self.PYTHON_DEV.append(val)

it1 = DepartmentIT()
print(it1.__dict__)  # {}
it1.hiring_python_dev(1)
print(it1.__dict__)  # {}
it1.hiring_python_dev(2)
print(it1.__dict__)  # {}

it2 = DepartmentIT()
print(it2.__dict__)  # {}
it2.hiring_python_dev(3)
print(it2.__dict__)  # {}
print(it2.PYTHON_DEV)  # [1, 2, 3]
print(DepartmentIT.PYTHON_DEV)  # [1, 2, 3]


# Чтобы не создавался атрибут экземпляра,
# а менялось значение атрибута класса,
# нужно в присвоении прописать название класса вместо self
class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3

    def hiring_python_dev(self):
        DepartmentIT.PYTHON_DEV += 1

    # Варианты
    @staticmethod
    def hiring_python_dev_static():
        DepartmentIT.PYTHON_DEV += 1

    @classmethod
    def hiring_python_dev_class(cls):
        cls.PYTHON_DEV += 1

it1 = DepartmentIT()
it1.hiring_python_dev()
it1.hiring_python_dev()
print(it1.__dict__)  # {}
print(it1.PYTHON_DEV)  # 6
print(DepartmentIT.PYTHON_DEV)  # 6


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Robot, у которого есть:
* атрибут класса population. В этом атрибуте будет храниться общее количество роботов, изначально принимает значение 0;
* конструктор __init__, принимающий 1 аргумент name. 
  Данный метод должен сохранять атрибут name и печатать сообщение вида "Робот <name> был создан". 
  Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
* метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
* метод say_hello, который печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
* метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"
"""
class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1


    def destroy(self):
        print(f"Робот {self.name} был уничтожен")
        Robot.population -= 1

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')


# Код для проверки
droid1 = Robot("R2-D2")
assert droid1.name == 'R2-D2'
assert Robot.population == 1
droid1.say_hello()
Robot.how_many()
droid2 = Robot("C-3PO")
assert droid2.name == 'C-3PO'
assert Robot.population == 2
droid2.say_hello()
Robot.how_many()
droid1.destroy()
assert Robot.population == 1
droid2.destroy()
assert Robot.population == 0
Robot.how_many()
print('Good')


# Task 02
"""
Создайте базовый класс User, у которого есть:
* метод __init__, принимающий имя пользователя и его роль. 
  Их необходимо сохранить в атрибуты экземпляра name и role соответственно

Затем создайте класс Access , у которого есть:
* приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
* приватный статик-метод __check_access , который принимает название роли и возвращает True, 
  если роль находится в списке __access_list , иначе — False
* публичный статик-метод get_access , который должен принимать экземпляр класса User 
  и проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access. 
  Если у пользователя достаточно прав, выведите на экран сообщение
  «User <name>: success», если прав недостаточно  «AccessDenied»
  Если передается тип данных, отличный от экземпляр класса User, необходимо вывести сообщение:
  «AccessTypeError»
"""
class User:

    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @classmethod
    def __check_access(cls, role: str):
        return role in cls.__access_list

    @staticmethod
    def get_access(obj: object):
        if isinstance(obj, User):
        # if obj.__class__ is User:
            if Access.__check_access(obj.role):
                print(f"User {obj.name}: success")
            else:
                print('AccessDenied')
        else:
            print('AccessTypeError')


# Код для проверки
user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError
print('Good')


# Task 03
"""
Создайте класс BankAccount, который имеет:
* атрибут класса bank_name со значением "Tinkoff Bank"
* атрибут класса address со значением  "Москва, ул. 2-я Хуторская, д. 38А"
* метод __init__, который устанавливает значения атрибутов name и balance: 
  владелец счета и значение счета.
* класс метод create_account, который возвращает новый экземпляр класса BankAccount. 
  Метод принимает имя клиента и сумму взноса.
* класс метод bank_info, который возвращает информацию о банке в виде:
  «{bank_name} is located in {address}»
"""
class BankAccount:

    bank_name = "Tinkoff Bank"
    address = "Москва, ул. 2-я Хуторская, д. 38А"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        # Создается новый Экземпляр класса внутри метода этого же класса
        return cls(name, balance)

    @classmethod
    def bank_info(cls):
        return f"{cls.bank_name} is located in {cls.address}"

# Код для проверки
oleg = BankAccount.create_account("Олег Тинкофф", 1000)
assert isinstance(oleg, BankAccount)
assert oleg.name == 'Олег Тинкофф'
assert oleg.balance == 1000
assert BankAccount.bank_info() == 'Tinkoff Bank is located in Москва, ул. 2-я Хуторская, д. 38А'

ivan = BankAccount.create_account("Ivan Reon", 50)
assert isinstance(ivan, BankAccount)
assert ivan.name == 'Ivan Reon'
assert ivan.balance == 50
print('Good')

