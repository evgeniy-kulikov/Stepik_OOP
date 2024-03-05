#  3.8 Вычисляемые свойства
""""""

# пример использования property для создания вычисляемого атрибута .area в классе Square:
class Square:
    def __init__(self, s):
        self.side = s

    @property
    def area(self):
        print('Calculate area...')
        return self.side ** 2

sq = Square(4)
print(sq.area)



#  вариант использования вычисляемых свойств —
#  предоставить автоматически отформатированное значение для данного атрибута:
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    @property
    def price(self):
        return f"${self._price:,.2f}"


banan = Product("Banan", 1.789)
print(banan.price)

"""
Во всех этих примерах значения вычисляемых атрибутов не хранятся в памяти, 
а сами вычисления начинаются только в момент обращения к атрибуту. 
Поэтому такие атрибуты можно назвать «ленивыми»
Ленивое вычисление (lazy evaluation) — это стратегия вычислений, 
при которой вычисления откладываются до момента, 
когда результат действительно потребуется. 
В контексте программирования это означает, что код не выполняет вычисления немедленно, 
как только они становятся доступными, а откладывает их выполнение до фактического запроса значения.
"""

# Кэширование вычисляемых атрибутов
import time


class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

        # при изменении стороны очищается "кэш" и при вызове свойства area оно будет знать,
        # что надо не брать из кэша, а пересчитать
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('Calculate area...')
            time.sleep(0.5)
            self.__area = self.side ** 2
        return self.__area

sq = Square(4)
# Calculate area...
print(sq.area) #  16
print(sq.area) #  16


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Rectangle, у которого есть:
* конструктор __init__, принимающий 2 аргумента: длину и ширину. 
* свойство area, которое возвращает площадь прямоугольника;
"""
class Rectangle():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self.length * self.width

# Код для проверки
r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)
print(r1.area) # 15
print(r2.area) # 6

r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976
print('Good')


# Task 02
"""
Создайте класс Date, у которого есть:
* конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
* свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
* свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";
"""
class Date():
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def date(self):
        return f"{self._day:02}/{self._month:02}/{self._year:04}"

    @property
    def usa_date(self):
        return f"{self._month:02}-{self._day:02}-{self._year:04}"


# Код для проверки
d1 = Date(5, 10, 2001)
assert isinstance(d1, Date)
assert d1.date == '05/10/2001'
assert d1.usa_date == '10-05-2001'
assert isinstance(type(d1).date, property), 'Вы не создали property date'
print(d1.date, d1.usa_date)



# d2 = Date(15, 3, 999)
# assert isinstance(d2, Date)
# assert d2.date == '15/03/0999'
# assert d2.usa_date == '03-15-0999'
# assert isinstance(type(d2).date, property), 'Вы не создали property date'
# print(d2.date, d2.usa_date)
#
# d3 = Date(3, 5, 3)
# assert d3.date == '03/05/0003'
# assert d3.usa_date == '05-03-0003'
# print(d3.date, d3.usa_date)
print('Good')

# Вариант
class Date:
    """
    Реализован отдельный ввод day, month, year
    """
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value
        self.__date = self.__usa_date = None

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value
        self.__date = self.__usa_date = None

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value
        self.__date = self.__usa_date = None

    @property
    def date(self):
        if self.__date is None:
            self.__date = f'{self.__day:02}/{self.__month:02}/{self.__year:04}'
        return self.__date

    @property
    def usa_date(self):
        if self.__usa_date is None:
            self.__usa_date = f'{self.__month:02}-{self.__day:02}-{self.__year:04}'
        return self.__usa_date


# Task 03
"""
Создайте класс Password, который имеет:
* метод __init__, который устанавливает значение атрибута password
* вычисляемое свойство strength, которое определяет стойкость пароля. 
  Если длина пароля меньше 8 символов, то такой пароль считается слабым, 
  свойство должно вернуть строку  "Weak". Сильным паролем считается тот, 
  в котором длина символов 12 и более, в таком случае свойство возвращает строку "Strong". 
  Во всех остальных случаях необходимо вернуть "Medium"
"""
class Password():
    def __init__(self, password):
        self.password = password


    @property
    def strength(self):
        if len(self.password) < 8:
            return f"Weak"
        elif len(self.password) >= 12:
            return f"Strong"
        return f"Medium"


# Код для проверки
pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"
assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"
pass_1.password = "123"
assert pass_1.strength == "Weak"
assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')
assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'
print('Good')
