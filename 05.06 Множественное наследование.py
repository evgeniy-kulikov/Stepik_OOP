#  5.6 Множественное наследование
""""""

"""
Поиск имен в иерархии классов

Порядок определения(разрешения) имен определяется при помощи MRO Method Resolution Order 
- порядка разрешения методов. 
Можно взглянуть на MRO при помощи магического атрибута __mro__  у дочернего класса
"""
class Doctor:
    pass

class Builder:
    pass

class Person(Builder, Doctor):
    pass


print(Person.__mro__)
# (<class '__main__.Person'>, <class '__main__.Builder'>, <class '__main__.Doctor'>, <class 'object'>)


"""
Делегирование при множественном наследовании
Через super() можно вызывать метод родителя. 
Но при множественном наследовании мы имеем несколько родителей. 
Так метод какого именно родителя будет вызван, 
если воспользоваться функцией super()? Тут опять все решает MRO
"""
class Doctor:
    def graduate(self):
        print('Ура, я отучился на доктора')


class Builder:
    def graduate(self):
        print('Ура, я отучился на строителя')


class Person(Builder, Doctor):
    def graduate(self):
        print('Посмотрим кем я стал')
        super().graduate()


print(Person.__mro__)
# (<class '__main__.Person'>, <class '__main__.Builder'>, <class '__main__.Doctor'>, <class 'object'>)
s = Person()
s.graduate()
# Посмотрим кем я стал
# Ура, я отучился на строителя


# чтобы отработал .graduate() у всех родителей,
# то необходимо для второго родителя напрямую прописать вызова метода .graduate()
class Person(Builder, Doctor):
    def graduate(self):
        print('Посмотрим кем я стал')
        super().graduate()
        Doctor.graduate(self)  # рямой вызов



# *  *  *  *  *   Task   *  *  *  *  *



# Task 01
"""
имеется три класса Mother, Father и Child.
Перепишите метод __init__ класса Child так,
чтобы он делегировал создание атрибутов mother_name и father_name родительским классам
"""
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name


class Father:
    def __init__(self, father_name):
        self.father_name = father_name


class Child(Mother, Father):
    def __init__(self, child_name, mother_name, father_name):
        super().__init__(mother_name)
        # self.mother_name = mother_name
        Father.__init__(self, father_name)
        # self.father_name = father_name
        self.child_name = child_name

    def introduce(self):
        return f"Меня зовут {self.child_name}. Моя мама - {self.mother_name}, мой папа - {self.father_name}"


child = Child("Анна", "Мария", "Иван")
print(child.introduce())
# Меня зовут Анна. Моя мама - Мария, мой папа - Иван




# Task 02 (don't answer)
"""
создать класс User, который принимает имя пользователя и пароль при инициализации, 
и имеет метод get_info(), который возвращает строку в виде 
Имя пользователя: {self.username}

Создайте класс Authentication, состоящий из одного метода authenticate(). 
Данный метод принимает имя пользователя и пароль, и возвращает True, 
если пользователь аутентифицирован успешно, и False, если аутентификация не удалась.

Создайте класс AuthenticatedUser, который наследуется от классов Authentication и User. 
Он не имеет своих методов и все поведение наследуют от родителей
"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_info(self):
        return f"Имя пользователя: {self.username}"

class Authentication:
    def authenticate(self, username, password):
        return 1

class AuthenticatedUser(Authentication, User):
    pass


# Код для проверки
assert issubclass(AuthenticatedUser, User) is True
assert issubclass(AuthenticatedUser, Authentication) is True
user1 = AuthenticatedUser('user1', 'password1')
assert user1.get_info() == 'Имя пользователя: user1'
assert user1.authenticate('user1', 'password2') is False
assert user1.authenticate('user1', 'password1') is True
ted = AuthenticatedUser('ted_lawyer', 'alligator3')
print(ted.get_info())
print('Good')

