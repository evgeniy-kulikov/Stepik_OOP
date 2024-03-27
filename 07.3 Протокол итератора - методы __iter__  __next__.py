#  7.3 Протокол итератора: магические методы __iter__ и __next__
""""""

"""
Итерация представляет собой процесс 
повторения выполнения определенных действий или операций в программе несколько раз. 

«Итерируемый объект» - это объект, который можно обходить при помощи цикла for 
это объект, который поддерживает итерацию.

Любой объект, который можно передать во встроенную функцию iter() 
будет считаться итерируемым объектом

Итератором в python называется объект, 
который возвращает следующий элемент последовательности 
или выбрасывает исключение StopIteration, если не осталось элементов. 
Отличительной особенностью итератора является его умение работать со встроенной функцией next()

Встроенная функция iter() работает следующим образом:

Смотрит на наличие магического метода __iter__  у объекта, если данный метод имеется, 
происходит его вызов. Метод  __iter__   обязательно должен вернуть итератор
 
Если метод __iter__  отсутствует, проверяется наличие метода __getitem__ . 
Если метод __getitem__ присутствует у объекта, python создаст итератор, 
который будет извлекать элементы объекта по порядку, начиная с нулевого индекса
 
Если оба метода не реализованы в объекте, 
тогда произойдет исключение TypeError: object is not iterable
"""

# Чтобы класс мог использоваться в качестве аргумента встроенной функции iter(), становясь итерируемым объектом,
# необходимо реализовать в нем магический метод __iter__ и вернуть в качестве результата итератор
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

ivan = Student('Ivan', 'Sidorov')
for s in ivan:
    print(s)  # TypeError: 'Student' object is not iterable


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __iter__(self):
        print('Вызываю __iter__')
        return iter(self.name)


ivan = Student('Ivan', 'Sidorov')
for s in ivan:
    print(s, end=' ')  # I v a n


#  способ сделать объект итерируемым это определить в нем магический метод __getitem__
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __getitem__(self, item):
        print('__getitem__')
        return self.name[item]

ivan = Student('Ivan', 'Sidorov')

# print(iter(ivan))  # <iterator object at 0x00000254999C7FA0>

for el in ivan:
    print(el, end=' ')
# __getitem__
# I __getitem__
# v __getitem__
# a __getitem__
# n __getitem__

"""
Итерируемым объектом в python является любой объект, 
имеющий методы __iter__ или __getitem__, 
которые возвращают итераторы или могут принимать индексы. 
В итоге итерируемый объект – это объект, который может предоставить нам итератор.

Итератор – это объект-перечислитель, 
который знает в каком порядке обходить элементы некого объекта. 
Он выдает по одному элементы последовательности, 
либо бросает исключение StopIteration, если элементов больше нет.
"""

s = 'Python'
for letter in s:
    print(letter)


# За кулисами python  на самом деле выполняет следующий код
s = 'Python'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


"""
Чтобы объект мог считаться итератором внутри него должно быть реализовано два метода:

магический метод __next__, в котором описывается  порядок выдачи элементов объекта. 
Когда элементы закончатся метод __next__ должен выкидывать исключение StopIteration.
 
магический метод __iter__, который возвращает self. 
Это позволяет использовать итератор там, где ожидается итерируемый объект, 
например в цикле for или в аргументе функции iter()
"""
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.index = 0

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        if self.index >= len(self.name):
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.name[self.index - 1]

ivan = Student('Ivan', 'Sidorov')
for s in ivan:
    print(s, end=" ")

# __iter__
# __next__
# I __next__
# v __next__
# a __next__
# n __next__


# вариант реализации итератора через отдельный класс.
"""
Имеется класс Counter, который является итерируемым объектом, 
так как в нем реализован метод __iter__. 
Но класс Counter не является итератором, потому что отсутствует метод __next__. 
Реализация итератора вынесена в отдельный класс IteratorCounter. 
При инициализации экземпляра IteratorCounter мы передаем экземпляр класса Counter, 
чтобы иметь доступ к значениям границ итерирования.
"""
class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return IteratorCounter(self)


class IteratorCounter:
    def __init__(self, counter: Counter):
        self.counter = counter

    def __next__(self):
        self.counter.current += 1
        if self.counter.current <= self.counter.high:
            return self.counter.current
        raise StopIteration


for el in Counter(0, 3):
    print(el, end=" ")  # 0 1 2 3


"""
Но при такой реализации класс IteratorCounter пока нельзя назвать итератором, 
потому что он не является итерируемым.
В нем отсутствует метод __iter__ и значит при попытке получить итератор 
при помощи функции iter() мы упадем с ошибкой.

Поэтому для полной реализации протокола итератора в классе IteratorCounter 
нужно добавить метод __iter__, который будет возвращать сам экземпляр

def __iter__(self):
    return self
"""
class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return IteratorCounter(self)


class IteratorCounter:
    def __init__(self, counter: Counter):
        self.counter = counter

    def __next__(self):
        self.counter.current += 1
        if self.counter.current <= self.counter.high:
            return self.counter.current
        raise StopIteration

    def __iter__(self):
        return self


r = iter(IteratorCounter(Counter(2, 4)))
print(next(r))  # 2
print(next(r))  # 3
print(next(r))  # 4
print(next(r))  # StopIteration





# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте итерируемый объект SequenceIterable, 
который принимает контейнер данных в виде списка в момент инициализации и сохраняет его в атрибуте ЭК
Сделать класс SequenceIterable итерируемым объектом
"""
class SequenceIterable:
    def __init__(self, value: list):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.value[self.index - 1]


# Код для проверки
container = SequenceIterable([[1, 5, 4, 6, 43], True, 'hello'])
for i in container:
    print(i)
# [1, 5, 4, 6, 43]
# True
# hello

# Вариант
class SequenceIterable(list):
    def __init__(self, iter_list: list):
        super().__init__(iter_list)



# Task 02
"""
Создайте класс Countdown, который должен принимать начальное значение 
и вести обратный отсчет до нуля, возвращая каждое значение в последовательности каждый раз, 
когда вызывается __next__. Когда обратный отсчет достигает нуля, итератор должен вызвать исключение StopIteration. 
Для этого вам понадобиться реализовать:

метод __init__. Он должен принимать одно положительное число - начало отсчета
 
методы __iter__ и __next__ для итерирования по значениям класса Countdown. 
"""

class Countdown:
    def __init__(self, start):
        self.start = start
        self.index = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.index = self.start
            raise StopIteration
        self.index -= 1
        return self.index


# Код для проверки
el = Countdown(3)
for i in el:
    print(i, end=" ")  # 3 2 1 0

for i in el:
    print(i, end=" ")  # 3 2 1 0



# Код для проверки
for i in Countdown(3):
    print(i, end=" ")  # 3 2 1 0

count = Countdown(2)

assert hasattr(count, '__next__') is True
assert hasattr(count, '__iter__') is True

iterator = iter(count)
assert next(iterator) == 2
assert next(iterator) == 1
assert next(iterator) == 0
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('Элементы итератора Countdown(7)')
for i in Countdown(7):
    print(i)

print('-' * 10)
print('Элементы итератора Countdown(10)')
for i in Countdown(10):
    print(i)

# Вариант
# Разовая итерация ЭК
class Countdown:
    def __init__(self, value):
        self.index = value + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.index

# Код для проверки
el = Countdown(3)
for i in el:
    print(i, end=" ")  # 3 2 1 0

for i in el:
    print(i, end=" ")  # пусто


# Task 03
"""
Создайте класс PowerTwo, который возвращает следующую степень двойки, 
начиная с нулевой степени (20=1). Внутри класса реализуйте:

метод __init__. Он должен принимать одно положительное число - степень двойки, 
до которой нужно итеририроваться включительно
 
методы __iter__ и __next__ для итерирования по степеням двойки
"""
class PowerTwo:
    def __init__(self, number):
        if isinstance(number, int) and number >= 0:
            self.number = number
            self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.number:
            self.index = 0
            raise StopIteration
        self.index += 1
        return 2 ** self.index

# Код для проверки
numbers = PowerTwo(2)
assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)

num = PowerTwo(4)
for i in num: # итерируемся до 4й степени двойки
    print(i, end=" ")

for i in num: # итерируемся до 4й степени двойки
    print(i, end=" ")


# Task 04
"""
Ниже в коде представлена реализация карточной колоды при помощи классов Card и Deck.
Исправьте код так, чтобы не было ошибок, и вывод программы соответствовал тестовому значению
"""
# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#
# class Deck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#
#     def __init__(self):
#         self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#
# deck = Deck()
# for card in deck:
#     print(card)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return iter(self.cards)

    # роль __next__ взял на себя список  ranks


deck = Deck()
for card in deck:
    print(card)
"""
2 Clubs
3 Clubs
...
10 Clubs
J Clubs
Q Clubs
K Clubs
A Clubs
2 Diamonds
...
A Diamonds
2 Hearts
...
A Hearts
2 Spades
...
A Spades
"""


# Task 05
"""
В коде представлена реализация класса FileReader, 
который должен при итерирации считывать построчно содержимое файла
Дописать метод __next__, чтобы он возвращал по порядку строки из файла, 
пока содержимое файла не закончится. 
Строку нужно очистить слева и справа от символов пробелов и переносов на новую строку
"""
# class FileReader:
#     def __init__(self, filename):
#         self.file = open(filename)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
#
# for line in FileReader('lorem.txt'):
#     print(line)

class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            s = self.file.readline()
            if s:
                return s.strip()
            self.file.close() # перед вызовом исключения файл правильнее будет закрыть.
            raise StopIteration

for line in FileReader('lorem.txt'):
    print(line)


# Task 06
"""
Создайте класс InfinityIterator, который реализует бесконечный итератор, 
который будет при каждой новой итерации или вызова функции next будет возвращать число, 
увеличенное на 10 от предыдущего значения. 
Начинать нужно с нуля.
"""
class InfinityIterator:
    def __init__(self):
        self.current = -10

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 10
        return self.current


a = iter(InfinityIterator())
next(a)


# Вариант (без метода __init__)
class InfinityIterator:

    def __iter__(self):
        self.current = -10
        return self

    def __next__(self):
        self.current += 10
        return self.current
