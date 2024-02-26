# 3.1 Методы экземпляра. Аргумент self
""""""

# *  *  *  *  *   Task   *  *  *  *  *

# 01
"""
Создайте класс Lion. 
В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
"""
class Lion():
    def roar(self):
        print('Rrrrrrr!!!')

# Ниже код для проверки класса Lion
s = Lion()
assert isinstance(s, Lion)
assert s.__dict__ == {}
s.roar()


# Task 02
"""
Создайте класс Robot, в котором реализованы:
Метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
Метод say_bye ,  печатающий на экран фразу «See u later alligator»

После определения класса создайте 2 экземпляра и сохраните их в переменные  c3po и r2d2
Затем вызовите у переменной  c3po  метод say_hello , а затем метод say_bye 
И то же самое сделайте с переменной r2d2:  вызовите метод say_hello , потом — метод say_bye 
"""
class Robot:
    def say_hello(self):
        print('Hello, human! My name is C-3PO')

    def say_bye(self):
        print('See u later alligator')


c3po = Robot()
r2d2 = Robot()

c3po.say_hello()
c3po.say_bye()

r2d2.say_hello()
r2d2.say_bye()


# Task 03
"""
Переопределяем класс Robot, в котором должны быть реализованы:
- Метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name 
- Метод say_hello . Метод должен проверить, есть ли у ЭК атрибут name . 
    Если атрибут name  присутствует, необходимо напечатать фразу «Hello, human! My name is <name>». 
    Если атрибут name  отсутствует у экземпляра, печатайте сообщение «У робота нет имени» 
- Метод say_bye ,  печатающий на экран фразу «See u later alligator»
"""
class Robot():
    def set_name(self, name=None):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')


# c3po = Robot()
r2d2 = Robot()

# c3po.say_hello()
# c3po.say_bye()

r2d2.say_hello()
r2d2.set_name('Tom')
r2d2.say_hello()
r2d2.say_bye()


# Task 04
"""
Создать класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
В классе Counter нужно определить:
- Метод start_from, который принимает один необязательный аргумент. 
    Значение, с которого начинается подсчет, по умолчанию равно 0.
- Метод increment, который увеличивает счетчик на 1.
- Метод display, который печатает фразу "Текущее значение счетчика = <value>".
- Метод reset,  который обнуляет накопившееся значение счетчика.
"""

class Counter():

    def start_from(self, cnt=0):
        self.cnt = cnt

    def increment(self):
        self.cnt += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.cnt}')

    def reset(self):
        self.cnt = 0

c1 = Counter()
c1.start_from(45)
c1.increment()
c1.display()  #  46
c1.reset()  # обнулили cnt
c1.display()  #  0


# Task 05
"""
Создайте класс Constructor, в котором реализованы:
- Метод add_atribute , принимающий на вход название атрибута в виде строки и его значение. 
    При помощи функции setattr необходимо создать или изменить атрибут для ЭК, у которого этот метод был вызван.
- Метод display ,  печатающий на экран словарь __dict__ у ЭК.
"""

class Constructor():

    def add_atribute(self, atrr='', value=None):  # Для случая если параметры в add_atribute() не передаются
    # def add_atribute(self, atrr, value):  # Параметры в add_atribute() обязятельны
        setattr(self, atrr, value)

    def display(self):
        print(self.__dict__)


obj3 = Constructor()
obj3.display()  # {}
obj3.add_atribute('a', 100)
obj3.display()  # {'a': 100}
obj3.add_atribute()
obj3.display()  # {'a': 100, '': None}



# Task 06
"""
Создайте класс Point. У этого класса должны быть:

Метод set_coordinates, который принимает координаты точки на плоскости 
и сохраняет их в экземпляр класса в атрибуты x и y 

Метод get_distance, который обязательно принимает экземпляр класса Point 
и возвращает расстояние между двумя точками по теореме Пифагора. 
В случае, если в данный метод передается не экземпляр класса Point, 
необходимо вывести сообщение "Передана не точка"
"""


class Point():

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, obj):
        if isinstance(obj, Point):
            return ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** 0.5
        return print('Передана не точка')


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)  # вернёт 5.0
p1.get_distance(10)  # Распечатает "Передана не точка"
