#  7.4 Продолжение про итераторы
""""""

"""
Итераторы реализуют метод __iter__, который обычно возвращает self, и метод __next__, 
который возвращает по одному элементу при каждом вызове.

Все итераторы являются итерируемыми, поскольку они соответствуют итерируемому протоколу. 
Однако не все итерируемые объекты являются итераторами — только те, 
которые реализуют метод __next__
Если у итерируемых объектов не реализован метод __next__, 
значит их нельзя использовать в качестве аргументов функции next()
"""
numbers = [1, 4, 5, 7]
print(next(numbers))  # TypeError: 'list' object is not an iterator


class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration


obj = Counter(3, 5)
iter_1 = iter(obj)
iter_2 = iter(obj)
print(iter_1, id(iter_1))  # одинаковые ячейки памяти
# <__main__.Counter object at 0x7ff43097a620> 140686763992608
print(iter_2, id(iter_2))  # одинаковые ячейки памяти
# <__main__.Counter object at 0x7ff43097a620> 140686763992608

"""
 Итерируемые объекты обычно содержат в себе сами данные. 
 Напротив, итераторы не хранят данные, а предоставляют их по одному элементу за раз
"""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
создать итератор SequenceIterator, который принимает контейнер данных в виде списка 
в момент инициализации и сохраняет его в атрибуте ЭК
При итерации объект SequenceIterator должен сперва выдать все элементы, 
находящиеся на четных индексах (0, 2, 4 и т.д), 
а затем элементы, имеющие нечетные индексы (1, 3, 5 и т.д.)
"""
class SequenceIterator:
    def __init__(self, value: list):
        self.value = value

    def __iter__(self):
        self.even = 0
        self.odd = 1
        return self

    def __next__(self):
        if self.even < len(self.value):
            self.even += 2
            return self.value[self.even - 2]
        if self.odd < len(self.value):
            self.odd += 2
            return self.value[self.odd - 2]
        else:
            self.even = 0
            self.odd = 1
            raise StopIteration

# Оригинальное решение (список вместо __next__)
class SequenceIterator:
    def __init__(self, value: list):
        self.value = value

    def __iter__(self):
        return iter(self.value[::2] + self.value[1:][::2])


# Больше кода
class SequenceIterator:
    def __init__(self, value: list):
        self.value = value

    def __iter__(self):
        self.index = 0
        self.even = True
        return self

    def __next__(self):
        if self.even:
            if self.index >= len(self.value):
                self.index = 1
                self.even = False
            else:
                self.index += 2
                return self.value[self.index - 2]

        if not self.even:
            if self.index >= len(self.value):
                self.index = 0
                self.even = True
                raise StopIteration
            else:
                self.index += 2
                return self.value[self.index - 2]

# Код для проверки
container = SequenceIterator([0, 1, 2, 3, 4, 5])
for i in container:
    print(i, end=' ')  # 0 2 4 1 3 5


# Task 02
"""
класс Stack логику перебора элементов делегирует классу StackIterator. 
Реализовать итератор в классе StackIterator, который обходит элементы стека сверху вниз
"""
class StackIterator():
    def __init__(self, obj: object):
        self.stack = obj
        self.index = 0

    def __next__(self):
        if self.index >= len(self.stack.items):
            self.index = 0
            raise StopIteration
        else:
            self.index += 1
            return self.stack.items[::-1][self.index - 1]


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return StackIterator(self)


# Код для проверки
stack = Stack()
stack.push(100)
stack.push(True)
stack.push('hello')
stack.push('world')
# Используем итератор для обхода стека
for item in stack:
    print(item, end=' ')  # world hello True 100



# Task 03
"""
Создайте объект итератор FibonacciIterator, 
который умеет выдавать последовательность Фибоначчи из n чисел. 
Число n поступает при инициализации класса FibonacciIterator.

Будем считать, что последовательность Фибиначчи следующая: 0, 1, 1, 2, 3, 5, 8, 13, 21 и т.д. 
Каждое следующее число получается суммой двух предыдущих.
"""
class FibonacciIterator:
    class FibonacciIterator:
        def __init__(self, num):
            self.num = num
            self.idx = 0
            self.prev, self.current = 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.idx >= self.num:
                self.idx = 0
                raise StopIteration
            if self.idx == 0:
                self.idx += 1
                return self.prev
            if self.idx == 1:
                self.idx += 1
                return self.current
            self.prev, self.current = self.current, self.prev + self.current
            self.idx += 1
            return self.current

# Код для проверки
fibonacci_iter = FibonacciIterator(7)

for number in fibonacci_iter:
    print(number, end=' ')  # 0, 1, 1, 2, 3, 5, 8


# Task 04
"""

"""

class Book:
    def __init__(self, title: str, pages: list):
        self.title = title
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return LibraryIterator(self.books) # тут определите, что будете передавать итератору

class LibraryIterator:
    def __init__(self, obj: object):
        self.books = obj
        self.idx = 0

    def __next__(self):
        ls = []
        for el in range(len(self.books)):
            ls.extend(self.books[el].pages)

        if self.idx >= len(ls):
            self.idx = 0
            raise StopIteration
        else:
            self.idx += 1
            return ls[self.idx - 1]

# Код для проверки
book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for page in library:
    print(page)
# Page 1
# Page 2
# Page 3
# Page 4
# Page A
# Page B
# Page C
# Chapter 1
# Chapter 2


# Task 05
"""
Создайте класс InfinityIterator, который реализует бесконечный итератор. 
Он должен возвращать элементы арифметической прогрессии с шагом 10. 
Начальное значение арифметическое прогрессии по умолчанию равно 0, 
но может быть передано при инициализации класса InfinityIterator
"""
class InfinityIterator:
    def __init__(self, num=0):
        self.current = num - 10

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 10
        return self.current


# Код для проверки
a = iter(InfinityIterator(5))
print(next(a))  # 5
print(next(a))  # 15
print(next(a))  # 25

# for i in InfinityIterator(7):
#     print(i)
# 7
# 17
# 27
# 37
# 47
# ...
