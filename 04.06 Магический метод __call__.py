# 4.6 Магический метод __call__
""""""

"""
В python оператор вызова () как правило используется для вызова функций и методов, 
но может так же быть применен к объектам, которые поддерживает вызов. 
Когда мы создаем свой собственный класс, мы можем вызывать его 
и результатом вызова будет новый экземпляр класса.
Чтобы объект мог поддерживать вызов, нужно определить в нем магический метод __call__
"""


class Counter:
    def __init__(self):
        self.counter = 0
        self.summ = 0
        self.length = 0
        print(f'init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summ += sum(args)
        self.length += len(args)
        print(f'Наш экземпляр вызывался {self.counter} раз')

    def get_average(self):
        return self.summ / self.length


counter = Counter()

counter(1, 2, 3)  # Наш экземпляр вызывался 1 раз
counter(4, 5, 6)  # Наш экземпляр вызывался 2 раз
print(f"Общее количество вызовов: {counter.counter}")  # Общее количество вызовов: 2
print(f"Сумма переданных аргументов: {counter.summ}")  # Сумма переданных аргументов: 21
print(f"Общая длина переданных аргументов: {counter.length}")  # Общая длина переданных аргументов: 6
print(counter.get_average())  # 3.5


"""
Реализация метода __call__ нужна, когда мы хотим, чтобы экземпляры класса вели себя как функции.
Одна из реальных ситуаций — это создание утилиты ведения журнала, 
которую можно легко настроить и вызывать из любых частей вашей программы.
"""
class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def __call__(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

from datetime import datetime
# создать экземпляр логгера и использовать его для регистрации сообщений из любой части сторонней программы
logger = Logger('my_log_file.txt')
def get_information():
    logger(f'Start work in get_information: {datetime.now()}')
    # do some work
    logger(f'Finished work in get_information: : {datetime.now()}')


def delete_files():
    logger(f'Start work in {delete_files.__name__}: {datetime.now()}')
    # do some work
    logger(f'Finished work in {delete_files.__name__}: : {datetime.now()}')



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""

"""
class QuadraticFunction:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


# Код для проверки
f = QuadraticFunction(2, 5, 7)
assert f(1) == 14
assert f(-3) == 10
assert f(2) == 25
assert f(5) == 82
f_2 = QuadraticFunction(-1, 2, 4)
assert f_2(5) == -11
assert f_2(2) == 4
assert f_2(-3) == -11
assert f_2(1) == 5
print('Good')



# Task 02
"""
Создайте класс Addition, у которого необходимо:
определить метод __call__. 
Он должен принимать произвольное количество аргументов 
и среди этих аргументов находить числа и их суммировать. 
Все остальные типы данных необходимо пропускать. 
В результате метод __call__ должен вернуть строку в следующем в виде:
Сумма переданных значений = {сумма}
"""
class Addition:

    def __call__(self, *args, **kwargs):
        # res = sum([el for el in (*args, *kwargs.values()) if isinstance(el, (int, float))])
        res = sum([el for el in args if isinstance(el, (int,float))])  # только для *args
        return f"Сумма переданных значений = {res}"


# Код для проверки
add = Addition()
assert add(10, 20) == "Сумма переданных значений = 30"
assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"
add2 = Addition()
assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
assert add2() == "Сумма переданных значений = 0"
assert add2('hello') == "Сумма переданных значений = 0"
print(add(1, 2, 3, val=10, num=4))
print('Good')



# Task 03
"""
Реализуйте свой собственный класс-декоратор Timer
"""

import time

class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        self.fn(*args, **kwargs)
        finish = time.time()
        print(f'Время работы функции {finish - start}')

@Timer
def calculate():
    for i in range(10000000):
         2 ** 100

calculate()
