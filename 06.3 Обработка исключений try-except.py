#  6.3 Обработка исключений try-except
""""""

"""
оператор try-except.

try:
    # код, в которым вы хотите отловить исключения
except <ExceptionType>:
    # код, который выполняется, когда произошло исключение ExceptionType
"""
try:
    print("int('hello')")
    int('hello')
    print("1 / 0")
    1 / 0
    print("a + b")
    a + b
except ValueError:
    print('error ValueError')

# int('hello')
# error ValueError

"""
Несколько блоков except
Блоков except может быть несколько: каждый except будет обрабатывать свой тип ошибок. 

try:
    # код, в которым вы хотите отловить исключения
except <ExceptionType_1>:
    # код, который выполняется, когда произошло исключение ExceptionType_1
except <ExceptionType_2>:
    # код, который выполняется, когда произошло исключение ExceptionType_2
"""
try:
    1 / 0
    int('hello')
    a + b
except ValueError:
    print('error ValueError')
except ZeroDivisionError:
    print('error ZeroDivisionError')
# error ZeroDivisionError


try:
    4 + 'dfgd'
except Exception as ex:
    print(f'error: {ex.__class__.__name__}')  # error: TypeError
finally:  # этот блок всегда отработает
    print('end')  # end


try:
    1/0
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('ZeroDivisionError')  # ZeroDivisionError
else:  # этот блок отработает если была поймана ошибка
    print('Good')
finally:
    print('end')  #  end


try:
    1/1
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('ZeroDivisionError')  # ZeroDivisionError
else:
    print('Good')  #  Good
finally:
    print('end')  #  end


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Отловить исключения типа ValueError и ZeroDivisionError.
"""
# a = int(input())
# b = int(input())
# print(f"Результат деления a на b: {a/b}")

try:
    a = int(input())
    b = int(input())
    a / b
except(ValueError, ZeroDivisionError):
    print("Введите корректные значения")
else:
    print(f"Результат деления a на b: {a/b}")

# вариант
try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except (ValueError, ZeroDivisionError):
    print('Введите корректные значения')


# Task 02
"""
Отловить каждое исключения  отдельным блоком
"""
try:
    a = int(input())
    b = int(input())
    a / b
except(ValueError):
    print("Введите целое число")
except(ZeroDivisionError):
    print("Делитель не должен быть равен нулю")
else:
    print(f"Результат деления a на b: {a/b}")


# Task 03
"""
"""
# file = open('pentagon_secrets.txt', 'r')
# print(file.read())

try:
    file = open('pentagon_secrets.txt', 'r')
except FileNotFoundError:
    print("Эх, не судьба тайны пентагона узнать")
else:
    print(file.read())

# Вариант
try:
    file = open('pentagon_secrets.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('Эх, не судьба тайны пентагона узнать')


# Task 04
"""
"""
def func(phrase):
    func(phrase)

# func('Это рекурсия, детка!')
try:
    func('Это рекурсия, детка!')
except RecursionError:
    print('Кто-то должен остановить это безумие')



# Task 05
"""
создать класс CustomButton, у которого есть:

метод __init__, принимающий один обязательный аргумент текст кнопки, его необходимо сохранить в атрибут text. 
И также в метод  может поступать произвольное количество именованных аргументов. 
Их необходимо сохранять в атрибуты экземпляра под тем же названием
метод config, который принимает произвольное количество именованных атрибутов. 
Он должен создать атрибут с указанным именем или, если этот атрибут уже присутствовал в экземпляре, 
изменить его на новое значение

метод click, который должен выполнить следующую строчку
self.command()
Здесь command является не методом, а атрибутом, который вызывают. 
В момент выполнения этой строчки может произойти две неприятные ситуации:
атрибут command может отсутствовать у экземпляра и тогда возникнет исключение AttributeError
атрибут command может не поддерживать оператор вызова и тогда возникнет исключение TypeError
Эти ситуации вам необходимо обработать в блоке try-except.
При первом варианте нужно вывести сообщение «Кнопка не настроена», 
при втором - «Кнопка сломалась»
"""
class CustomButton:
    def __init__(self, text, **kwargs):
        self.texy = text
        # self.kwargs = kwargs
        for key, value in kwargs.items():
            # setattr(self, key, value)
            self.key = value

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print("Кнопка не настроена")
        except TypeError:
            print("Кнопка сломалась")


# Код для проверки
def func():
    print('Оно живое')

btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click()  # Кнопка не настроена
btn.config(command=func)
btn.click()  # Оно живое

