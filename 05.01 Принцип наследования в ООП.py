# 5.1 Принцип наследования в ООП
""""""

"""
Функция issubclass
- помогает проверить, является ли один класс подклассом другого. Имеет следующий синтаксис:

issubclass(class, classinfo)
Параметры:
class — класс, который проверяем
 
classinfo — класс или кортеж с классами, на принадлежность кому проверяем.
Функция issubclass() возвращает True, 
если переданный class является подклассом значения, которое передано в classinfo. 
При этом неважно должно ли родство между ними быть прямым или косвенным(через несколько наследников). 
"""



# Task 01
"""
Класс Vehicle является базовым классом, от которого наследуются все остальные.
Класс RaceCar наследуются от Класса Car
"""
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass

class RaceCar(Car):
    pass

# Код для проверки
vehicle = Vehicle()
car = Car()
plane = Plane()
boat = Boat()
race_car = RaceCar()
assert isinstance(vehicle, Vehicle)
assert isinstance(car, Car)
assert isinstance(plane, Plane)
assert isinstance(boat, Boat)
assert isinstance(race_car, RaceCar)
assert vehicle.__dict__ == {}
assert car.__dict__ == {}
assert issubclass(Car, Vehicle), "Класс Car должен наследоваться от Venicle"
assert issubclass(Plane, Vehicle), "Класс Plane должен наследоваться от Venicle"
assert issubclass(Boat, Vehicle), "Класс Boat должен наследоваться от Venicle"
assert issubclass(RaceCar, Car), "Класс RaceCar должен наследоваться от Venicle"
assert issubclass(RaceCar, Vehicle), "Класс RaceCar должен наследоваться от Venicle"
print('Good')


# Task 02
"""
Создайте базовый класс Vehicle, у которого есть:

конструктор __init__, принимающий название транспортного средства, 
его максимальную скорость и пробег. 
Их необходимо сохранить в атрибуты экземпляра name, max_speed и mileage соответственно
 
метод display_info , который печатает информацию в следующем виде:
Vehicle Name: {name}, Speed: {max_speed}, Mileage: {mileage}

Затем создайте подкласс Bus , унаследованный от Vehicle. Оставьте его пустым
"""
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

class Bus(Vehicle):
    pass


# Код для проверки
assert issubclass(Bus, Vehicle)
bus_99 = Bus("Ikarus", 66, 124567)
assert bus_99.name == 'Ikarus'
assert bus_99.max_speed == 66
assert bus_99.mileage == 124567
bus_99.display_info()

modelX = Vehicle('modelX', 240, 18)
assert modelX.__dict__ == {'max_speed': 240, 'mileage': 18, 'name': 'modelX'}
modelX.display_info()

audi = Bus('audi', 123, 43)
assert audi.__dict__ == {'max_speed': 123, 'mileage': 43, 'name': 'audi'}, 'Видимо забыли создать какой-то атрибут'
audi.display_info()
print('Good')


# Task 02
"""
Создайте базовый класс  Person, у которого есть:

конструктор __init__, который должен принимать на вход имя и записывать его в атрибут name
 
метод get_name, который возвращает атрибут name
 
метод  is_employee, который возвращает  False
Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:

метод  is_employee, который возвращает  True
"""
class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @staticmethod
    def is_employee():
        return False


class Employee(Person):

    @staticmethod
    def is_employee():
        return True


# Код для проверки
assert issubclass(Employee, Person)
p = Person("just human")
assert p.name == 'just human'
assert p.get_name() == 'just human'
assert p.is_employee() is False
emp = Employee("Geek")
assert emp.name == 'Geek'
assert emp.get_name() == 'Geek'
assert emp.is_employee() is True
print('Good')


# Task 03
"""
"""
class Shape():
    pass

class Polygon(Shape):
    pass

class Ellipse(Shape):
    pass

class Triangle(Polygon):
    pass

class Circle(Ellipse):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

# Код для проверки
assert issubclass(Ellipse, Shape), "Класс Ellipse должен наследоваться от Shape"
assert issubclass(Polygon, Shape), "Класс Polygon должен наследоваться от Shape"
assert issubclass(Circle, Shape), "Класс Circle должен наследоваться от Shape"
assert issubclass(Circle, Ellipse), "Класс Circle должен наследоваться от Ellipse"
assert not issubclass(Circle, Polygon), "Класс Circle не должен наследоваться от Polygon"
assert issubclass(Triangle, Polygon), "Класс Triangle должен наследоваться от Polygon"
assert issubclass(Triangle, Shape), "Класс Triangle должен наследоваться от Shape"
assert not issubclass(Triangle, Ellipse), "Класс Triangle не должен наследоваться от Ellipse"
assert issubclass(Square, Rectangle), "Класс Square должен наследоваться от Rectangle"
assert issubclass(Square, Polygon), "Класс Square должен наследоваться от Polygon"
assert issubclass(Square, Shape), "Класс Square должен наследоваться от Shape"
assert not issubclass(Square, Ellipse), "Класс Square не должен наследоваться от Ellipse"
print('Good')


# Task 04
"""
вывести 3 числа в разных строках:
на первой строке количество кружочков
на второй строке количество фигур, являющихся прямоугольниками
на последней строке количество фигур, являющихся многоугольниками.
"""
class Shape():
    pass

class Polygon(Shape):
    pass

class Ellipse(Shape):
    pass

class Triangle(Polygon):
    pass

class Circle(Ellipse):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

shapes = [
    Polygon(), Triangle(), Ellipse(), Polygon(), Triangle(), Ellipse(), Polygon(), Square(), Polygon(), Circle(),
    Shape(), Polygon(), Triangle(), Circle(), Ellipse(), Shape(), Circle(), Rectangle(), Circle(), Circle(),
    Square(), Square(), Circle(), Rectangle(), Rectangle(), Polygon(), Polygon(), Polygon(), Square(), Square(),
    Rectangle(), Square(), Rectangle(), Polygon(), Circle(), Triangle(), Rectangle(), Shape(), Rectangle(),
    Polygon(), Polygon(), Ellipse(), Square(), Circle(), Shape(), Polygon(), Ellipse(), Triangle(), Square(),
    Polygon(), Triangle(), Circle(), Rectangle(), Rectangle(), Ellipse(), Triangle(), Rectangle(), Polygon(),
    Shape(), Circle(), Rectangle(), Polygon(), Triangle(), Circle(), Polygon(), Rectangle(), Polygon(), Square(),
    Triangle(), Circle(), Ellipse(), Circle(), Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
    Triangle(), Polygon(), Square(), Polygon(), Circle(), Ellipse(), Polygon(), Shape(), Triangle(), Rectangle(),
    Circle(), Square(), Triangle(), Triangle(), Ellipse(), Square(), Circle(), Rectangle(), Ellipse(), Shape(),
    Triangle(), Ellipse(), Circle(), Shape(), Polygon(), Polygon(), Ellipse(), Rectangle(), Square(), Shape(),
    Circle(), Triangle(), Circle(), Circle(), Circle(), Triangle(), Ellipse(), Polygon(), Circle(), Ellipse(),
    Rectangle(), Circle(), Shape(), Polygon(), Polygon(), Triangle(), Rectangle(), Polygon(), Shape(), Circle(),
    Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
]

print(sum(isinstance(el, Circle) for el in shapes))
# print(sum(issubclass(el.__class__, Circle) for el in shapes))
print(sum(issubclass(el.__class__, Rectangle) for el in shapes))
print(sum(issubclass(el.__class__, Polygon) for el in shapes))
