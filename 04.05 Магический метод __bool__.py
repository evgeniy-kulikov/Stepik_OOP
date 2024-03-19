# 4.5 Магический метод __bool__
""""""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс City, у которого есть:

конструктор __init__, принимающий единственный аргумент - название города. 
Вам необходимо сохранить его в качестве атрибута экземпляра name, 
причем вам нужно преобразовать переданное имя города таким образом, 
чтобы первая буква каждого слова была заглавной, 
а остальные оказались строчными (пример "new york" - > "New York")
 
магический метод __str__ таким образом, чтобы он возвращал имя города
 
магический метод __bool__ так, чтобы он возвращал False,
если название города заканчивается на любую гласную букву латинского алфавита (a, e, i, o, u), 
в противном случае - True
"""
class City:

    def __init__(self, name: str):
        self.name = name.title()
        # self.name = ' '.join([el.capitalize() for el in name.split()])

    def __bool__(self):
        return self.name[-1] not in 'aeiou'

    def __str__(self):
        return f"{self.name}"



# Код для проверки
p1 = City('new york')
assert p1.name == "New York"
assert p1.__str__() == "New York"
assert isinstance(p1, City)
print(p1)
assert bool(p1)

p2 = City('SaN frANCISco')
assert isinstance(p2, City)
assert p2.name == "San Francisco"
print(p2)
assert not bool(p2)

p3 = City('NIZHNY NoVGORod')
assert p3.name == "Nizhny Novgorod"
print(p3)
assert bool(p3)
assert isinstance(p3, City)
print('Good')


# Task 02
"""
создать класс Quadrilateral(четырехугольник), в котором есть:

метод __init__. Он должен сохранять в экземпляр класса два атрибута: width и height. 
При этом в сам метод __init__ может передаваться один аргумент
(тогда в width и height присваивать это одно одинаковое значение, тем самым делать квадрат), 
либо два аргумента( первый идет в атрибут width, второй - в height)
 
метод __str__ , который работает следующим образом: 
если width и height одинаковые, возвращать строку «Квадрат размером <width>х<height>»
в противном случае, возвращать строку «Прямоугольник размером <width>х<height>»
переопределить метод __bool__ так, чтобы он возвращал True, если объект является квадратом, 
и False в противном случае
"""
class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = width
        if height == None:
            self.height = width
        else:
            self.height = height

    def __bool__(self):
        return self.width == self.height

    def __str__(self):
        if self.width == self.height:
            return f"Квадрат размером {self.width}х{self.height}"
        return f"Прямоугольник размером {self.width}х{self.height}"


# Код для проверки
q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)
print('Good')