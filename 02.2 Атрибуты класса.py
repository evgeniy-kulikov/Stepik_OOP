# 2.2 Атрибуты класса
""""""

"""
Обращение к атрибутам класса производится по следующей схеме:

class_name.attribute_name
class_name — имя класса
attribute_name — имя атрибута

Обращаться через точку можно только к существующим атрибутам. 
Если попытаться обратиться к имени атрибута, который отсутствует в классе, будет исключение
"""
class Person:
  name = 'Jared'
  age = 30

print(Person.name)  # Jared
print(Person.age)  # 30

"""
Функция getattr
Также доступ к атрибутам класса Person можно получить, используя функцию getattr

Функция getattr() возвращает значение именованного атрибута объекта. 
Если атрибут не найден, функция getattr не падает с ошибкой AttributeError, 
а возвращает значение по умолчанию.

def getattr(object, name, default=None): # known special case of getattr
"""
class Person:
  name = 'Jared'
  age = 30

print(getattr(Person, 'name'))  # Jared
print(getattr(Person, 'age'))  # 30

# пример со значением по умолчанию:
print(getattr(Person, 'salary', 'Нет такого атрибута'))  # Нет такого атрибута


# Для получения всех атрибутов, содержащихся в классе или в экземпляре класса,
# применяется магический атрибут __dict__
class Person:
  """Класс Person"""
  name = 'Bob'
  age = 35


print(Person.__dict__)
# '__module__': '__main__', '__doc__': 'Класс Person', 'name': 'Bob', 'age': 35,
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>}

"""
Чтобы проверить наличие конкретного атрибута в классе, нужно воспользоваться функцией hasattr:

hasattr(obj, name)
object — это объект, который будет подвержен проверке;
attribute_name — это название искомого атрибута в виде строки.
"""
class Person:
  name = 'Jared'
  age = 30

print(hasattr(Person, 'name'))  # True
print(hasattr(Person, 'money'))  # False


"""
Изменение атрибута класса
Для изменения значения существующего атрибута класса следует применять следующую конструкцию:

class_name.attribute_name = value
class_name — имя класса,
attribute_name — имя атрибута
value — новое значение атрибута
"""
class Person:
  name = 'Jared'
  age = 30

print(Person.name)  # Jared
Person.name = 'Michail'
print(Person.name)  # Michail


"""
для создания нового атрибута или изменения существующего применяется функция setattr:

setattr(obj, name, value)
Функция setattr принимает следующие параметры:
obj: объект, который следует дополнить атрибутом
name: строка с именем атрибута. Можно указывать как имя нового, так и существующего атрибута.
value: произвольное значение атрибута.
"""


class Person:
  name = 'Ivan'
  age = 30

print(Person.name)  # Ivan
setattr(Person, 'name', 'Vasya')
print(Person.name)  # Vasya

"""
Удаление атрибутов класса
Для удаления атрибута следует применять оператор del или функцию delattr:

Функция delattr
delattr(obj, name)
удаляет из объекта obj атрибут name. 

При попытке удалить несуществующий атрибут получите исключение AttributeError
"""


class Person:
  name = 'Ivan'
  age = 30
  money = 200

del Person.money  # удаление успешно
delattr(Person, 'age') # первое удаление успешно
delattr(Person, 'age') # второе - нет, так как атрибута age уже нет
del(Person, name)

"""
Проверка наличия атрибута
В python существует функция, которая позволяет проверить наличие атрибута в объекте. Она называется hasattr
 
Функция hasattr() возвращает значение True, если объект имеет заданный именованный атрибут, 
и значение False, если нет.
"""


class Person:
  name = 'Jared'
  age = 30


print(hasattr(Person, 'name'))  # True
print(hasattr(Person, 'salary'))  # False

if hasattr(Person, 'age'):
    print('Атрибут age присутствует')

if not hasattr(Person, 'city'):
    print('Атрибут city отсутствует')



# *  *  *  *  *   Task   *  *  *  *  *

# Tasks  01 - 05
class Book:
  name = '1984'
  writer = 'Джордж Оруэлл'
  pages = 213


# вывести на разных строках сначала атрибут класса writer, а затем атрибут name
print(Book.writer)
print(Book.name)

# получить доступ к атрибутам writer и pages при помощи функции getattr
print(getattr(Book, 'writer'))
print(getattr(Book, 'pages'))

# изменить значения атрибутов name и pages
setattr(Book, 'name', 'Скотный двор')
setattr(Book, 'pages', 115)

# добавить в класс Book два новых атрибута (один атрибут - через функцию setattr, второй - через присвоение)
setattr(Book, 'rating', 8.7)
Book.genre = 'dystopian'

# Из класса Book удалить три атрибута: pages, writer, rating
# Удаление выполните с помощью оператора del и функции delattr
delattr(Book, 'pages')
del Book.writer
del Book.rating


# Task 06
"""
создать класс Cat и внутри него два атрибута класса:
атрибут name со значением 'Матроскин'
атрибут color со значением 'black'
После этого создайте экземпляр класса и сохраните его в переменную my_cat
"""
class Cat:
    name = 'Матроскин'
    color = 'black'


my_cat = Cat()

# Task 07
"""
взять каждый первый элемент кортежа и создать на его основе название атрибута в классе Empty , 
а в качестве значения присвоить второй элемент кортежа.
"""
class Empty:
    pass


my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]

for el in my_list:
    setattr(Empty, el[0], el[1])

# print(Empty.__dict__)


# Task 08
"""
Реализуйте функцию is_obj_has_attr, 
которая принимает любой объект в качестве первого аргумента 
и название атрибута в качестве второго

Функция is_obj_has_attr должна возвращать True, 
если в объекте имеется атрибут с указанным названием, 
либо вернуть False
"""
class Duck:
    weight = 5
    height = 10


def is_obj_has_attr(obj, atr):
    return hasattr(obj, atr)

# print(is_obj_has_attr(Duck, 'weight'))
# print(is_obj_has_attr(Duck, 'name'))
# print(is_obj_has_attr(Duck, 'height'))


# Task 09
"""
Программа будет принимать на вход произвольное количество слов в одну строку, 
разделенных пробелом. Проверить, является ли каждое из введенных слов названием атрибута. 
Регистр слов значения не имеет.

Нужно вывести в каждой отдельной строке введенные слова по порядку 
и напротив через дефис указать, нашлось свойство с таким именем или нет 
(вывести YES или NO)
"""
class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


for el in map(str, input().split()):
    if hasattr(Person, el.lower()):
        print(f'{el}-YES')
    else:
        print(f'{el}-NO')
