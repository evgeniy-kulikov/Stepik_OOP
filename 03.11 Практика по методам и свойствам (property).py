# 3.11 Практика по методам и свойствам (property)
""""""



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Registration, который пока будет проверять только введенный логин. 
Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

В классе Registration необходимо реализовать:

метод __init__ , принимающий один аргумент — логин пользователя. 
Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3). То есть когда отработает данный код 
def __init__(self, логин):
    self.login = логин # передаем в сеттер login значение логин 
должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

Cвойство геттер login, которое возвращает значение self.__login;
 
Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
строковое значение: если поступают другие типы данных, необходимо вызвать исключение при помощи строки raise TypeError
 
логин, так как является почтой, должен содержать один символ собаки «@». 
В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError
 
логин должен содержать символ точки «.» после символа «@». В случае, если после @ нет точки, 
вызываем исключение при помощи строки raise ValueError
Если значение проходит проверку, новое значение логина сохраняется в атрибут self.__login
"""
import re
class Registration:

    def __init__(self, val):
        self.login = val

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, val: str):
        if not isinstance(val, str):
            raise TypeError('Логин должен быть строкой')
        if not '@' in val:
            raise ValueError(f"Логин {val} должен содержать один символ '@'")
        if val.count('@') > 1:
            raise ValueError(f"Логин {val} должен содержать только один символ '@'")
        # if not '.' in val.split('@')[1]:
        if not re.fullmatch('(?i)[a-z0-9_-]+@[a-z0-9_-]+\.[a-z]{2,}', val):
            raise ValueError(f"Логин {val} должен быть символ '.' после символа '@'")
        self.__login = val


# Код для проверки
try:
    result = Registration("fga")
except ValueError as error:
    print("Логин fga должен содержать один символ '@'")

try:
    result = Registration(1234)
except TypeError as error:
    print("Логин должен быть строкой")

try:
    result = Registration("f@ga@")
except ValueError as error:
    print("Логин f@ga@ должен содержать только один символ '@'")

try:
    result = Registration("fg@a")
except ValueError as error:
    print("В логине fg@a должен быть символ '.' после символа '@'")

try:
    result = Registration("fg.@a")
except ValueError as error:
    print("В логине fg.@a должна быть '.' после символа '@'")

result = Registration("translate@gmail.com")
assert result.login == "translate@gmail.com"
assert result._Registration__login == "translate@gmail.com"

try:
    result.login = "asdsa12asd."
except ValueError as error:
    print("Логин asdsa12asd. должен содержать один символ '@'")

try:
    result.login = "asdsa12@asd"
except ValueError as error:
    print("asdsa12@asd должен быть символ '.' после символа '@'")

result.login = "alligator13@how.do"
assert result.login == "alligator13@how.do"
assert result._Registration__login == "alligator13@how.do"
print('Good')


# Task 02
"""
Дополняем функционал в класс Registration:
1. в метод  __init__ добавляется аргумент: password. Должно сработать свойство сеттер password.
2. Свойство геттер password, возвращает значение self.__password
3. Свойство сеттер password, принимает значение нового пароля. Его перед сохранением проверить на следующее:
* Новое значение пароля должно быть строкой (не список, словарь и т.д. ), 
  в противном случае вызываем исключение TypeError("Пароль должен быть строкой")
* Длина нового пароля должна быть от 5 до 11 символов, 
  в противном случае вызывать исключение ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
* Новый пароль должен содержать хотя бы одну цифру. Для этого создаем staticmethod is_include_digit , 
  который проходит по всем элементам строки и проверяет наличие цифр. 
  В случае отсутствия цифрового символа вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')
* Строка password должна содержать элементы верхнего и нижнего регистра. 
  Создаем staticmethod is_include_all_register, который с помощью цикла проверяет элементы строчки на регистр. 
  В случае ошибки вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
* Строка password помимо цифр должна содержать только латинские символы. 
  Для этого создайте staticmethod is_include_only_latin , 
  который проверяет каждый элемент нового значения на принадлежность к латинскому алфавиту 
  (проверка должна быть как в верхнем, так и нижнем регистре). 
  В случае, если встретится нелатинский символ, 
  вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит').
* Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt. 
  С помощью staticmethod создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле. 
  Если значение совпадет со значением из файла, 
  то в сеттер вызываем исключение: ValueError('Ваш пароль содержится в списке самых легких')
"""

from string import ascii_letters as st, digits as dt
import re
class Registration:

    def __init__(self, val, password):
        self.login = val
        self.password = password

    @staticmethod
    def check_password_dictionary(val: str):
        with open("easy_passwords.txt", "r", encoding="utf-8") as fl:
            # return any([el.strip() == val for el in fl])
            return val in fl.read().split()

    @staticmethod
    def is_include_only_latin(val: str):
        if re.fullmatch('(?a)^\w+$', val):
            return True
        return False
        # return all([el in st or el in dt for el in val])

    @staticmethod
    def is_include_digit(val: str):
        return  any([el.isdigit() for el in val])

    @staticmethod
    def is_include_all_register(val: str):
        return any([el.islower() for el in val]) and any([el.isupper() for el in val])

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, val: str):
        if not isinstance(val, str):
            raise TypeError('Пароль должен быть строкой')
        if not 4 < len(val) < 12:
            raise ValueError(f"Пароль {val} должен быть длиннее 4 и меньше 12 символов")
        if not self.is_include_digit(val):
            raise ValueError(f"Пароль {val} должен содержать хотя бы одну цифру")
        if not self.is_include_all_register(val):
            raise ValueError(f"Пароль {val} должен содержать хотя бы один символ верхнего и нижнего регистра")
        if not self.is_include_only_latin(val):
            raise ValueError(f"Пароль {val} должен содержать только латинский алфавит")
        if self.check_password_dictionary(val):
            raise ValueError(f"Ваш пароль {val} содержится в списке самых легких")

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, val: str):
        if not isinstance(val, str):
            raise TypeError('Логин должен быть строкой')
        if not '@' in val:
            raise ValueError(f"Логин {val} должен содержать один символ '@'")
        if val.count('@') > 1:
            raise ValueError(f"Логин {val} должен содержать только один символ '@'")
        # if not '.' in val.split('@')[1]:
        if not re.fullmatch('(?i)[a-z0-9_-]+@[a-z0-9_-]+\.[a-z]{2,}', val):
            raise ValueError(f"Логин {val} должен содержать символ '.' после символа '@'")
        self.__login = val


# Код для проверки
try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
print('Good')



# Task 03
"""
Создайте класс  File, у которого есть:
метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name. 
Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
 
метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» 
и проставляет атрибут in_trash в значение False
 
метод  remove, который печатает фразу «Файл {name} был удален» 
и проставляет атрибут is_deleted  в значение True
 
метод read, который
печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Прочитали все содержимое файла {self.name}», если файл не удален и не в корзине

метод write, который принимает значение content для записи и 
печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине
"""
class File:

    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f"ErrorReadFileDeleted({self.name})")

        elif self.in_trash:
            print(f"ErrorReadFileTrashed({self.name})")

        else:
            print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            print(f"ErrorWriteFileDeleted({self.name})")

        elif self.in_trash:
            print(f"ErrorWriteFileTrashed({self.name})")

        else:
            print(f"Записали значение {content} в файл {self.name}")

# Код для проверки
f1 = File('puppies.jpg')
assert f1.name == 'puppies.jpg'
assert f1.in_trash is False
assert f1.is_deleted is False
f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
assert f1.is_deleted is True
f1.read()  # ErrorReadFileDeleted(puppies.jpg)
passwords = File('pass.txt')
assert passwords.name == 'pass.txt'
assert passwords.in_trash is False
assert passwords.is_deleted is False
f3 = File('xxx.doc')
assert f3.__dict__ == {'name': 'xxx.doc', 'in_trash': False, 'is_deleted': False}
f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.in_trash = True
f3.is_deleted = False
f3.read()
f3.write('hello')
f3.restore_from_trash()
assert f3.in_trash is False
f3.write('hello')  # Записали значение «hello» в файл cat.jpg
f2 = File('cat.jpg')
f2.write('hello')  # Записали значение «hello» в файл cat.jpg
f2.write([1, 2, 3])  # Записали значение «hello» в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)
print('Good')


# Task 04
"""
В дополнение к классу File создайте класс  Trash у которого есть:
* атрибут класса  content , изначально равный пустому списку
* статик-метод  add, который принимает файл и сохраняет его в корзину: 
  для этого нужно добавить его в атрибут content и проставить файлу атрибут in_trash значение True. 
  Если в метод add передается не экземпляр класса File, необходимо вывести сообщение
  В корзину можно добавлять только файл
* статик-метод  clear, который запускает процесс очистки файлов в корзине. 
  Необходимо для всех файлов, хранящихся в атрибуте content , 
  в порядке их добавления в корзину вызвать метод файла remove. 
  Атрибут content  после очистки должен стать пустым списком. 
  Сама процедура очистки должна начинаться фразой: Очищаем корзину 
  и заканчиваться фразой: Корзина пуста
* статик-метод  restore, который запускает процесс восстановления файлов из корзины. 
  Необходимо для всех файлов, хранящихся в атрибуте content , 
  в порядке их добавления в корзину вызвать метод файла restore_from_trash. 
  Атрибут content  после очистки должен стать пустым списком. 
  Сама процедура восстановления должна начинаться фразой: Восстанавливаем файлы из корзины
  и заканчиваться фразой: Корзина пуста
"""
class Trash:

    content: list = []

    @staticmethod
    def add(val):
        if isinstance(val, File):
            Trash.content.append(val)
            val.in_trash = True
        else:
            print('В корзину можно добавлять только файл')

    @staticmethod
    def clear():
        print("Очищаем корзину")
        for el in Trash.content:
            File.remove(el)
        Trash.content = []
        print("Корзина пуста")

    @staticmethod
    def restore():
        print("Восстанавливаем файлы из корзины")
        for el in Trash.content:
            File.restore_from_trash(el)
        Trash.content = []
        print("Корзина пуста")


class File:

    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f"ErrorReadFileDeleted({self.name})")

        elif self.in_trash:
            print(f"ErrorReadFileTrashed({self.name})")

        else:
            print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            print(f"ErrorWriteFileDeleted({self.name})")

        elif self.in_trash:
            print(f"ErrorWriteFileTrashed({self.name})")

        else:
            print(f"Записали значение {content} в файл {self.name}")


# # Код для проверки класса File и Trash
f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')
for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False
f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')
assert Trash.content == []
Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)
f1.read()
Trash.add(f1)
f1.read()
for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True
for f in [f2, passwords, f3, f1]:
    assert f in Trash.content
Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'
Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)
for f in [passwords, f2, f1]:
    assert f in Trash.content
Trash.clear()
for file in [passwords, f2, f1]:
    assert file.is_deleted is True
assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'
f1.read()


# Task 05
"""
Создать класс Product с атрибутами name и price  
"""
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price



# Task 06
"""
создадим класс User, который содержит:
* метод __init__, принимающий на вход логин пользователя и необязательный аргумент — баланс его счета (по умолчанию 0). 
  Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
* метод __str__, возвращающий строку вида 
  Пользователь {login}, баланс - {balance}
* Cвойство геттер balance, которое возвращает значение self.__balance;
* Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
* метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
* метод is_money_enough, который принимает числовое значение и проверяет, 
  имеется ли у пользователя такая сумма на балансе. Данный метод должен возвращать булево значение: 
  если такая сумма есть – True, если нет – False:
* метод payment  принимает числовое значение, которое должно списаться с баланса пользователя. 
  Если на счете у пользователя не хватает средств, то необходимо вывести фразу
  'Не хватает средств на балансе. Пополните счет' и отказ в платеже. 
  Если средств хватает, списываем с баланса у пользователя указанную сумму.
  (Постарайтесь внутри реализации воспользоваться методом is_money_enough)
"""
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, val):
        self.__balance = val

    def deposit(self, val):
        if type(val) in (int, float):
            self.__balance += val

    def is_money_enough(self, val):
        if type(val) in (int, float):
            return val <= self.__balance

    def payment(self, val):
        if self.is_money_enough(val):
            self.__balance -= val
        else:
            print('Не хватает средств на балансе. Пополните счет')

# Код для проверки
billy = User('billy@rambler.ru')
print(billy)
print(billy.is_money_enough(350))
billy.deposit(100)
billy.deposit(300.7)
print(billy.is_money_enough(350.4))
print(billy)
billy.payment(500)
billy.payment(150)
print(billy)
jack = User('jack@gmail.ru', 800)
print(jack)



# Task 07
"""
Создание класса корзины, куда пользователь будет складывать товары. 
Для этого нам понадобятся ранее созданные классы User и Product

Создаем класс Cart, который содержит:
* метод __init__, принимающий на вход экземпляр класса User . Его необходимо сохранить в атрибуте user . 
  Помимо этого, метод  должен создать атрибут goods — пустой словарь (лучше использовать defaultdict). 
  Он нужен будет для хранения товаров и их количества 
  (ключ словаря — экземпляр класса Product, значение — количество). 
  И еще нам понадобится создать защищенный атрибут .__total со значением 0. 
  В нем будет храниться итоговая сумма заказа
* метод add принимает на вход экземпляр класса Product 
  и необязательный аргумент — количество товаров (по умолчанию 1). 
  Метод add  должен увеличить в корзине (атрибут goods) количество указанного товара  
  на переданное значение количества и пересчитать атрибут self.__total
* метод remove  принимает на вход экземпляр класса Product и 
  необязательный аргумент — количество товаров (по умолчанию 1).  
  Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара  
  на переданное значение количества и пересчитать атрибут self.__total. 
  Количество товара в корзине не может стать отрицательным, как и итоговая сумма;
* свойство геттер total , которое возвращает значение self.__total;
* метод order  должен использовать метод payment  из класса User и передать в него итоговую сумму корзины. 
  В случае, если средств пользователю хватило, вывести сообщение «Заказ оплачен», 
  в противном случае - «Проблема с оплатой»;
* метод print_check , печатающий на экран чек. Он должен начинаться со строки
  ---Your check---
  Затем выводится состав корзины в алфавитном порядке по названию товара в виде
  {Имя товара} {Цена товара} {Количество товара} {Сумма} 
  И заканчивается чек строкой
  ---Total: {self.total}---
"""
from collections import defaultdict  # опционпльно для варианта 2*

class Cart:

    def __init__(self, user: object):
        if isinstance(user, User):
            self.user = user
        self.__total = 0
        self.goods = dict()

    def add(self, prod, cnt=1):
        if isinstance(prod, Product):
            if prod in self.goods and cnt > 1:

                # Через setdefault все ниже можно пропустить
                # self.goods[product] = self.goods.setdefault(product, 0) + cnt

                self.goods[prod] += cnt
            else:  # для варианта 2* блок else можно опустить
                self.goods[prod] = cnt
            self.__total += cnt * prod.price

    def remove(self, prod, cnt=1):
        if isinstance(prod, Product):
            if prod in self.goods and self.goods[prod] >= cnt and cnt > 1:
                self.goods[prod] -= cnt
                self.__total -= cnt * prod.price
            else:
                self.__total -= self.goods[prod]  * prod.price
                del self.goods[prod]


    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print("---Your check---")
        for key, val in sorted(self.goods.items(), key=lambda el: el[0].name):
            print(f"{key.name} {key.price} {val} {key.price * val}")
        print(f"---Total: {self.total}---")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, val):
        self.__balance = val

    def deposit(self, val):
        if type(val) in (int, float):
            self.__balance += val

    def is_money_enough(self, val):
        if type(val) in (int, float):
            return val <= self.__balance

    def payment(self, val):
        if self.is_money_enough(val):
            self.__balance -= val
            return True
        print('Не хватает средств на балансе. Пополните счет')
        return False

# Код для проверки
billy = User('billy@rambler.ru')
lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
print(cart_billy.goods[lemon] == 5)
print('Good')
