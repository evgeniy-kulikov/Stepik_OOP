#  5.8 Миксины
""""""

"""
Одно из главных преимуществ миксинов заключается в том, что они позволяют создавать код, 
который можно использовать повторно. Миксины можно использовать в любом классе, 
который может наследовать их методы и свойства, что позволяет сократить объем кода. 
Например, если вы хотите добавить функциональность к нескольким классам, 
вы можете создать миксин, который содержит эту функциональность, 
и затем наследовать этот миксин в каждом классе.

Миксины не предназначены для создания самостоятельных экземпляров классов, 
а скорее для того, чтобы добавлять функциональность к другим классам.

Принято в названии миксин класса добавлять в конце слово Mixin, 
чтобы подчеркнуть для себя и других разработчиков, что здесь вы имеете дело с «примесью»
"""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
По примеру из лекции создайте класс CountryPizza:
название «Деревенская пицца»
в составе должны быть помимо сыра еще ветчина, перец, оливки, пепперони, грибы и курица
Из перечисленных топпингов отсутствуют в коде ниже
ветчина(ham, стоимость 7)
перец (pepper, стоимость 3)
курица (chicken, стоимость 5)
Миксины для данных топпингов необходимо создать
"""
class BasePizza:
    BASE_PIZZA_PRICE = 15

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f"{self.name} with {self.toppings}, ${self.price:.2f}"


class PepperoniMixin:
    def add_pepperoni(self):
        print("Adding pepperoni!")
        self.price += 5
        self.toppings += ['pepperoni']


class MushroomMixin:
    def add_mushrooms(self):
        print("Adding mushrooms!")
        self.price += 3
        self.toppings += ['mushrooms']


class OnionMixin:
    def add_onion(self):
        print("Adding onion!")
        self.price += 2
        self.toppings += ['onion']


class BaconMixin:
    def add_bacon(self):
        print("Adding bacon!")
        self.price += 6
        self.toppings += ['bacon']


class OlivesMixin:
    def add_olives(self):
        print("Adding olives!")
        self.price += 1
        self.toppings += ['olives']


class HamMixin:
    def add_ham(self):
        print("Adding ham!")
        self.price += 7
        self.toppings += ['ham']


class PepperMixin:
    def add_pepper(self):
        print("Adding pepper!")
        self.price += 3
        self.toppings += ['pepper']


class ChickenMixin:
    def add_chicken(self):
        print("Adding chicken!")
        self.price += 5
        self.toppings += ['chicken']


class OlivesPizza(BasePizza, OlivesMixin):
    def __init__(self):
        super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
        self.add_olives()


class PepperoniPizza(BasePizza, PepperoniMixin):
    def __init__(self):
        super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
        self.add_pepperoni()


class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):
    def __init__(self):
        super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_onion()
        self.add_bacon()


class CountryPizza(BasePizza, HamMixin, PepperMixin, OlivesMixin, PepperoniMixin, MushroomMixin, ChickenMixin):
    def __init__(self):
        super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
        self.add_ham()
        self.add_pepper()
        self.add_olives()
        self.add_pepperoni()
        self.add_mushrooms()
        self.add_chicken()


# Код для проверки
pizza = CountryPizza()
assert pizza.name == 'Деревенская пицца'
assert pizza.price == 39
assert pizza.toppings == ['cheese', 'ham', 'pepper', 'olives', 'pepperoni', 'mushrooms', 'chicken']
print(pizza)
print('Good')

# Task 02
"""
создайте класс PermissionMixin, который будет иметь следующие методы:
__init__(self): метод инициализации, который создает множество permissions для хранения разрешений. 
В него мы будем сохранять действия, которые будут доступны пользователям, 
например Чтение, Запись, Выполнение и т.д.

grant_permission(self, permission): метод для назначения разрешения. 
Добавляет переданное разрешение в множество permissions

revoke_permission(self, permission): метод для отмены разрешения. 
Удаляет переданное разрешение из множества permissions

has_permission(self, permission): метод для проверки наличия разрешения. 
Возвращает True, если переданное разрешение присутствует в множестве permissions, и False в противном случае.

Создайте класс User, который будет наследоваться от PermissionMixin и иметь следующие атрибуты:
name: имя пользователя.
email: email пользователя.
"""
class PermissionMixin:
    def __init__(self):
        self.permissions = set()

    def grant_permission(self, permission):
        self.permissions.add(permission)

    def revoke_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User(PermissionMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email


# Код для проверки
user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')
assert user1.email == 'alice@example.com'
assert user1.name == 'Alice'
assert user1.permissions == set()
assert user2.email == 'bob@example.com'
assert user2.name == 'Bob'
assert user2.permissions == set()
user1.grant_permission('read')
user1.grant_permission('write')
user2.grant_permission('read')
assert user1.permissions == {'read', 'write'}
assert user2.permissions == {'read'}
assert user1.has_permission('read') is True
assert user1.has_permission('write') is True
assert user1.has_permission('execute') is False
assert user2.has_permission('read') is True
assert user2.has_permission('write') is False
assert user2.has_permission('execute') is False
user1.revoke_permission('write')
user1.revoke_permission('execute')
assert user1.has_permission('read') is True
assert user1.has_permission('write') is False
assert user1.has_permission('execute') is False
print('Good')


# Task 03
"""
Ваша задача научить классы конвертиться к json-строке 
при помощи миксина под названием JsonSerializableMixin, 
который добавляет метод to_json() в любой класс, использующий этот миксин. 
Метод to_json() конвертирует словарь атрибутов экземпляра в строку JSON, 
используя стандартную библиотеку json в Python.
"""
import json

class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class Car(JsonSerializableMixin):
    def __init__(self, make: str, color: str):
        self.make = make
        self.color = color

class Book(JsonSerializableMixin):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Person(JsonSerializableMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Код для проверки
car = Car("Toyota", "red")
assert car.to_json() == '{"make": "Toyota", "color": "red"}'
book = Book("The Catcher in the Rye", "J.D. Salinger")
assert book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger"}'
book.ratings = [5, 4, 5, 4, 5]
book.is_bestseller = True
book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", "ratings": [5, 4, 5, 4, 5], "is_bestseller": true}'
person = Person("John", 30)
assert person.to_json() == '{"name": "John", "age": 30}'
print('Good')




# Task 04
"""
Класс DictMixin представляет собой миксин, который добавляет в класс, наследующий его, метод to_dict(). 
Этот метод позволяет преобразовать объект в словарь.

Внутри класса DictMixin вы можете создавать сколько угодно служебных методов и атрибутов, 
которые помогут вам справиться с задачей. 
Главное, это реализовать метод to_dict(), 
он являться точкой входа для взаимодействия с вашим миксином 
и он должен вернуть представление вашего объекта в виде словаря. 
Обратите внимание на вложенность атрибутов.  
"""
# import json
# class DictMixin:
#     def to_dict(self):
#         return json.loads(json.dumps(self, default=vars))

# class DictMixin:
#     def to_dict(self):
#         d_dict = json.dumps(self, default=lambda x: x.__dict__)
#         return json.loads(d_dict)


# class DictMixin:
#     def __repr__(self):
#         return str(self.__dict__)
#
#     def to_dict(self):
#         return eval(self.__repr__())


class DictMixin:
    def to_dict(self):
        result_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, list):
                result_dict[k] = [el.to_dict() for el in v]
            elif isinstance(v, DictMixin):
                result_dict[k] = v.to_dict()
            else:
                result_dict[k] = v
        return result_dict

class Phone(DictMixin):
    def __init__(self, number):
        self.number = number

class Person(DictMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address

# Код для проверки
address = Address("123 Main St", "Anytown", "CA", "12345")
john_doe = Person("John Doe", 30, address)

john_doe_dict = john_doe.to_dict()

assert john_doe_dict == {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345'
    }
}

address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_dict() == {
    'street': '123 Main St',
    'city': 'Albuquerque',
    'state': 'NM',
    'zip_code': '987654'
}
walter = Person("Walter White", 30, address)
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White'}

walter_phone = Phone("555-1234")
walter.phone = walter_phone
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White',
                            'phone': {'number': '555-1234'}}

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
company = Company("SCHOOL", company_address)

assert company.to_dict() == {'address': {'city': 'Albuquerque',
                                         'state': 'NM',
                                         'street': '3828 Piermont Dr',
                                         'zip_code': '12345'},
                             'name': 'SCHOOL'}

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_dict() == {'address': {'city': 'Albuquerque',
                                       'state': 'NM',
                                       'street': 'Los Pollos Hermanos',
                                       'zip_code': '12345'},
                           'age': 55,
                           'friends': [{'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '123 Main St',
                                                    'zip_code': '987654'},
                                        'age': 30,
                                        'name': 'Walter White',
                                        'phone': {'number': '555-1234'}},
                                       {'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '456 Oak St',
                                                    'zip_code': '12345'},
                                        'age': 27,
                                        'name': 'Jesse Bruce Pinkman',
                                        'phone': {'number': '555-5678'}}],
                           'name': 'Gustavo Fring'}

print('Good')


# Task 05
"""
выполнить сериализацию объектов, атрибутами которых могут быть другие объекты. 
Для этого переделайте миксин JsonSerializableMixin, так чтобы он мог сериализовать такие объекты. 

Внутри миксина JsonSerializableMixin обязательно должен быть метод to_json(), 
который возвращает итоговую строку сериализации объекта. 
Все остальное вы можете создавать по своему усмотрению
"""
import json

# class JsonSerializableMixin:
    # def to_dict(self):
    #     return json.loads(json.dumps(self, default=vars))
    #
    # def to_json(self):
    #     return json.dumps(self.to_dict())

# class JsonSerializableMixin:
#     def __repr__(self):
#         return str(self.__dict__)
#
#     def to_json(self):
#         return json.dumps(eval(self.__repr__()))

class JsonSerializableMixin :
    def to_json(self):
        return json.dumps(self, default = lambda x: x.__dict__)


# Ниже код для проверки миксина JsonSerializableMixin
class Person(JsonSerializableMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(JsonSerializableMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(JsonSerializableMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address



# Код для проверки
address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_json() == '{"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}'

walter = Person("Walter White", 30, address)
walter.hobby = ['Chemistry', 'Cooking']
walter.is_danger = True

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
walter.company = Company("SCHOOL", company_address)
assert walter.to_json() == '{"name": "Walter White", "age": 30, "address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, "company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}}'

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
walter.is_lucky = False

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_json() == '{"name": "Gustavo Fring", "age": 55, "address": {"street": "Los Pollos Hermanos", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}, "friends": [{"name": "Walter White", "age": 30, "address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, "company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}, "is_lucky": false}, {"name": "Jesse Bruce Pinkman", "age": 27, "address": {"street": "456 Oak St", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}]}'
print('Good')




