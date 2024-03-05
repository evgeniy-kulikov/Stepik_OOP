# 3.7.2 Декоратор Property (чтение-запись)
""""""

"""
Право на чтение (Read Access)
Означает, что данные могут быть прочитаны или использованы, но не могут быть изменены или модифицированы.

Право на запись (Write Access)
Дает возможность изменять данные. Можно присваивать новые значения переменным, 
изменять состояние объектов или изменять содержимое файлов и структур данных.
"""

# элементарный вариант использования property — предоставить атрибуты только для чтения
class Person:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self._age


"""
Предоставление атрибутов для чтения и записи

Здесь мы создаем класс Square со свойством-атрибутом .side для чтения и записи. 
В этом случае метод получения (getter) просто возвращает значение стороны квадрата. 
Метод setter преобразует входное значение стороны и присваивает его закрытой переменной ._side, к
оторую вы используете для хранения окончательных данных.

В этой новой реализации Square и его свойства .side следует отметить одну тонкую деталь. 
В этом случае инициализатор класса присваивает входное значение свойству .side напрямую, 
а не сохраняет его в выделенном непубличном атрибуте, таком как ._side.

Почему? Потому что вам нужно убедиться, что каждое значение, представленное как сторона квадрата, 
включая значение инициализации, проходит через метод установки и преобразуется в число с плавающей запятой.

Square также реализует атрибут .area как свойство. Метод getter вычисляет площадь, 
используя сторону квадрата. Метод setter делает нечто любопытное. 
Вместо сохранения входного значения площади в специальном атрибуте он вычисляет сторону квадрата 
и записывает результат вновь в свойство.side.
"""
class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5

sq = Square(42)
# Считываем значения
sq.side
# 42.0
sq.area
# 1764.0

# записаем новое значение
sq.area = 100
# 100.0
sq.side
# 10.0


"""
Предоставление атрибутов только для записи

В этом примере мы создаем экземпляр пользователя Tom с начальным паролем через свойство password.
Метод установки хэширует пароль и сохраняет его в защищенном атрибуте ._hashed_password.
Обратите внимание, что когда вы пытаетесь получить доступ к .password напрямую,
вы получаете AttributeError.
Наконец, присвоение нового значения .password запускает метод установки и создает новый хешированный пароль.

В методе установки .password мы используем os.urandom()
для генерации 32-байтовой случайной строки в качестве "соли" (salt) вашей хеш-функции.
Чтобы сгенерировать хешированный пароль используем hashlib.pbkdf2_hmac().
Затем вы сохраняете полученный хешированный пароль в закрытом атрибуте ._hashed_password.
Это гарантирует, что вы никогда не сохраните открытый текстовый пароль в каком-либо извлекаемом атрибуте.
"""
import hashlib
import os


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Пароль можно только менять, нельзя смотреть")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )

a = User("Tom", 'qwerty')
print(a.name)  # Tom
a.password = "new_qwerty"
print(a._hashed_password)
# b'\xfb\t\xd8\xd9~\xb2\x1a%\x7f\xfb\xfd\xf5\x7f4Nn\xd4\x9e\xb6\xc15cP7\x1fJ/\xf0\xc6\xbfb\xed'


# *  *  *  *  *   Task   *  *  *  *  *


# Task 03
"""
Создайте класс Notebook, у которого есть:
* конструктор __init__, принимающий список записей, в нем могут находиться любые значения. 
  Необходимо сохранить его в защищенном атрибуте ._notes
* свойство notes_list, которое распечатает содержимое атрибута ._notes в виде пронумерованного списка
"""
class Notebook():
    def __init__(self, value:list):
        self._notes = value

    @property
    def notes_list(self):
        for n, el in enumerate(self._notes, 1):
            print(f"{n}.{el}")


# Код для проверки
note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list

note = Notebook(list(range(10, 20)))
note.notes_list
try:
    note.notes_list = [3, 4, 3] # при попытке сохранить новое значение должна быть ошибка
except AttributeError:
    print("ошибка")


# Task 04
"""
Создайте класс Money, у которого есть:

* конструктор __init__, принимающий 2 аргумента: dollars, cents. 
  По входным аргументам вам необходимо создать атрибут экземпляра total_cents. 
* свойство-геттер dollars, которое возвращает количество имеющихся долларов;
* свойство-сеттер dollars, которое принимает целое неотрицательное число — количество долларов 
  и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, 
  при этом значение центов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, 
  нужно печатать на экран сообщение "Error dollars";
* свойство геттер cents, которое возвращает количество имеющихся центов;
* свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100  количество центов 
  и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, 
  при этом значение долларов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, 
  нужно печатать на экран сообщение "Error cents";
* метод __str__ (информация по данному методу), который возвращает строку вида 
  "Ваше состояние составляет {dollars} долларов {cents} центов". 
  Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами
"""
class Money():
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.cents
        else:
            print( "Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = self.dollars * 100 + value
        else:
            print( "Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

# Код для проверки
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
