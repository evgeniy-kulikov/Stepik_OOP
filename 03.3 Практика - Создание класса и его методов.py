# 3.3 Практика. Создание класса и его методов
""""""

"""
Мы можем создать список экземпляров класса. 
Таким образом, каждый элемент в списке будет являться объектом нашего класса, 
имеющим свои атрибуты и методы. Обращаясь через индекс к списку, 
мы получаем экземпляр класса, а уже потом через точку можем обращаться к атрибутам и методам.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}," \
               f"and I am {self.age} years old."


# 1-й вариант
persons = []
persons.append(Person('Arcadi', 20))
persons.append(Person('Alex', 40))
persons.append(Person('Susan', 44))

print(persons[0].name)  # Arcadi
print(persons[1].age)  # 40
print(persons[2].greet())  # Hello, my name is Susan,and I am 44 years old.

# 2-й вариант
for el in persons:
    print(el.age, el.name) # Обращаемся к атрибутам
    print(el.greet()) # Обращаемся к методу



"""
При моделировании явлений реального мира в программах классы 
нередко дополняются все большим количеством подробностей. 
Списки атрибутов и методов растут, и через какое-то время файлы становятся длинными и громоздкими. 
В такой ситуации часть одного класса нередко можно записать в виде отдельного класса. 
Большой код разбивается на меньшие классы, которые работают во взаимодействии друг с другом.
"""
# Атибуты и методы в рамках одного класса
class ElectricCar:
    """
    Класс для создания электромобиля
    Атибуты и методы в рамках одного класса
    """
    def __init__(self, maker, model, year, battery_size=70):
        self.maker = maker
        self.model = model
        self.year = year
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def describe_car_info(self):
        print(f'{self.maker} {self.model} {self.year}'.title())

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_car_info()


# Разделили класс первый вариант класса ElectricCar на два связанных класса
# Battery и ElectricCar
class Battery:
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar:
    """Класс для создания электромобиля"""
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car_info(self):
        print(f'{self.maker} {self.model} {self.year}'.title())


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_car_info()
my_tesla.battery.describe_battery()
print(my_tesla.battery.battery_size)


# Другой пример реализации связанных классов
#  Игра «Камень-Ножницы-Бумага» при помощи двух классов.
class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        # !!!   \  - Перенос f строки   !!!
        self.choice = input(f"{self.name}, choose rock, "\
        f"paper or scissors: ").lower()

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    def get_winner(self):
        if self.player1.choice == self.player2.choice:
            return None
        elif self.rules[self.player1.choice] == self.player2.choice:
            return self.player1
        else:
            return self.player2

    def play(self):
        self.player1.choose()
        self.player2.choose()
        winner = self.get_winner()
        if winner:
            print(f"{winner.name} победил!")
        else:
            print("У нас ничья.")


# Пример использования
player1 = Player("Игрок 1")
player2 = Player("Игрок 2")
game = Game(player1, player2)
game.play()



#  Игра «Камень-Ножницы-Бумага» при помощи трех классов.
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.choice: str | None = None

    def __str__(self) -> str:
        return f'Игрок: {self.name}'

    def get_choice(self) -> None:
        while True:
            player_input: str = input(f'{self.name}, выбери одно из действий: '
                                      f'камень, ножницы, бумага: ').lower()

            if self._is_correct_choice(player_input):
                self.choice = player_input
                break

            print(f'{player_input} — такого действия нет\n')

    @staticmethod
    def _is_correct_choice(player_input: str) -> bool:
        return player_input in GameRules.rules


class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.rules: dict[str, str] = GameRules.rules

    def _get_winner(self) -> Player | None:
        if self.player1.choice == self.player2.choice:
            return None
        elif self.rules.get(self.player1.choice) == self.player2.choice:
            return self.player1
        return self.player2

    def start(self) -> None:
        for player in (self.player1, self.player2):
            player.get_choice()

        winning_player = self._get_winner()

        print(f'\nПобедил(а): {winning_player.name}!' if winning_player else '\nНичья...')


if __name__ == '__main__':
    andrew = Player('Андрей')
    mila = Player('Мила')

    game = Game(andrew, mila)
    game.start()


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создайте класс Dog, у которого есть методы:
 __init__, принимающий имя и возраст собаки и сохраняющий их в аргументы name и age
 description, который возвращает строку в виде «{name} is {age} years old»
 speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}»
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        self.sound = sound
        return f'{self.name} says {self.sound}'


# Task 02
"""
Создайте класс Rectangle, который имеет следующие методы:
 __init__, который устанавливает значения атрибутов width и height
 area, который возвращает площадь прямоугольника
 perimeter , который возвращает периметр прямоугольника
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


# Task 03
"""
Реализуйте класс Numbers, который предназначен для хранения произвольного количества чисел. 
Данный класс должен содержать методы:
__init__, принимающий произвольное количество чисел и сохраняющих их внутри экземпляра
add_number, которой принимает числовое значение и добавляет его в конец коллекции экземпляра
get_positive, который возвращает список всех положительных чисел из коллекции экземпляра
get_negative, который возвращает список всех отрицательных чисел из коллекции экземпляра
get_zeroes,  который возвращает список всех нулевых значений из коллекции экземпляра
"""
class Numbers:
    def __init__(self, *args):
        self.numbers = list(args)  # args - это имя кортежа

    def add_number(self, num):
        return self.numbers.append(num)

    def get_positive(self):
        return [el for el in self.numbers if el > 0]
        # return list(filter(lambda x: x > 0, self.numbers))

    def get_negative(self):
        return [el for el in self.numbers if el < 0]
        # return list(filter(lambda x: x < 0, self.numbers))

    def get_zeroes(self):
        return [el for el in self.numbers if el == 0]
        # return list(filter(lambda x: x == 0, self.numbers))


# Task 04
"""
реализовать класс Stack, у которого есть методы:

 __init__создаёт новый пустой стек. Параметры данный метод не принимает. 
 Создает атрибут экземпляра values, где будут в дальнейшем храниться элементы стека в виде списка (list), 
 изначально при инициализации задайте значение атрибуту values, равное пустому списку;

 push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает;

 pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. 
 Стек изменяется. Если пытаемся удалить элемент из пустого списка, 
 необходимо вывести сообщение "Empty Stack";

 peek() возвращает верхний элемент стека, но не удаляет его. 
 Параметры не требуются, стек не модифицируется. Если элементов в стеке нет, 
 распечатайте сообщение "Empty Stack", верните None после этого;

 is_empty() проверяет стек на пустоту. Параметры не требуются, 
 возвращает булево значение.

 size() возвращает количество элементов в стеке. Параметры не требуются, 
 тип результата — целое число.
"""
class Stack:
    def __init__(self):
        self.values = list()

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.values:
            return self.values.pop()
        return print("Empty Stack")

    def peek(self):
        if self.values:
            return self.values[-1]
        print("Empty Stack")
        return None

    def is_empty(self):
        return not bool(self.values)

    def size(self):
        return len(self.values)


# Task 05
"""
реализовать класс Worker, у которого есть методы:

 __init__, принимающий 4 аргумента: имя, зарплата, пол и паспорт. 
    Необходимо сохранить их в следующих атрибутах: name, salary, gender и passport.

 get_info, который распечатает информацию о сотруднике в следующем виде: 
    «Worker {name}; passport-{passport}»
"""
class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')


persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

worker_objects = [Worker(*el) for el in persons]
[el.get_info() for el in worker_objects]


# Task 06
"""
Реализовать класс CustomLabel, у которого есть методы:
    __init__, принимающий один обязательный аргумент — текст виджета, 
 который необходимо сохранить в атрибут text. 
 Также в метод  может поступать произвольное количество именованных аргументов. 
 Их необходимо сохранять в атрибуты экземпляра под тем же названием.

    метод config, который принимает произвольное количество именованных атрибутов. 
 Он должен создать атрибут с указанным именем или, 
 если этот атрибут уже присутствовал в экземпляре, изменить его на новое значение
"""
class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        # self.__dict__.update(kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        # self.__dict__.update(kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)


# Task 07
"""
1. Создайть базовый класс Person, у которого есть:
метод __init__, принимающий имя и возраст человека. 
    Их необходимо сохранить в атрибуты экземпляра nameи age соответственно.
метод display_person_info , который печатает информацию в следующем виде:
    Person: {name}, {age}

2. Создайте класс Company , у которого есть:
метод __init__, принимающий название компании и город ее основания. 
    Их необходимо сохранить в атрибуты экземпляра company_name  и location соответственно.
метод display_company_info , который печатает информацию в следующем виде:
    Company: {company_name}, {location}

3. Создайте класс Employee , который:
имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания. 
    Необходимо создать атрибут personal_data и сохранить в него экземпляр класса Person. 
И также создать атрибут work  и сохранить в него экземпляр класса Company.
После этого через атрибуты personal_data и work 
вы можете обращаться к методам соответствующих классов Personи Company
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')

class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')

class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)


# Task 08
"""
Создать приложение для учета задач, которое будет использовать классы Task, TaskList и TaskManager.

Класс Task будет хранить информацию о задаче (название, описание, статус выполнения), состоит из: 
метода __init__, принимающий  и сохраняет в атрибуты экземпляра name , description и status. 
По умолчанию status равен False.
метод display , который печатает информацию в следующем виде:
{название задачи} (Сделана/Не сделана)
В зависимости от статуса задачи выводится Сделана или Не сделана 

Класс TaskList будет содержать список задач и методы для добавления/удаления задач.
В нем должно быть реализованы методы:
 __init__, который должен создать пустой список задач в атрибуте tasks
 add_task, который принимает задачу и добавляет ее в конец списка задач
 remove_task, который принимает задачу и удаляет ее из списка задач

Класс TaskManager будет содержать методы для отображения списка задач и изменения статуса выполнения задач. 
В нем должно быть реализованы методы:
 __init__, который должен принимать экземпляр TaskList  и сохранять его в атрибуте  task_list
  mark_done, который принимает задачу (экземпляр Task)  и устанавливает ей истинный статус выполнения
  mark_undone, который принимает задачу (экземпляр Task)  и устанавливает ей ложный статус выполнения
  show_tasks, который для каждой хранящейся задачи в списке вызывает метод display
"""
class Task:
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print(f"{self.name} ({'Сделана' if self.status else 'Не сделана'})")


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:
    def __init__(self, task_list):
        self.task_list = task_list

    def mark_done(self, task):
        task.status = True

    def mark_undone(self, task):
        task.status = False

    def show_tasks(self):
        for instance in self.task_list.tasks:
            instance.display()


# Task 09
"""
Создайте класс Triangle, в котором реализованы следующие методы
 __init__, принимающий три стороны треугольника.
 is_exists, который отвечает на вопрос существует ли треугольник с текущими сторонами.
* Треугольник существует, если каждая сторона треугольника меньше суммы двух других сторон.
 is_equilateral, который проверяет является ли треугольник равносторонним.
* называется равносторонним, если у него все стороны равны.
 is_isosceles, который проверяет является ли треугольник равнобедренным и существующим. 
* Треугольник называется равнобедренным, если у него две стороны равны.
"""
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self):
        return all([self.a < self.b + self.c, self.b < self.a + self.c, self.c < self.b + self.a])

    def is_equilateral(self):
        if self.is_exists():
            return self.a == self.b == self.c
        return False

    def is_isosceles(self):
        if self.is_exists():
            return any([self.a == self.b, self.c == self.b, self.a == self.c])
        return False


triangle = Triangle(1, -1, 0)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")
