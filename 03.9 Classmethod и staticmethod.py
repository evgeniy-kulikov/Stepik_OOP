# 3.9 Classmethod и staticmethod
""""""

"""
Метод класса
Метод класса позволяет привязать функцию именно к классу, а не к экземпляру. 
Для реализации метода класса нужно использовать декоратор @classmethod. 
Шаблон создания метода класса следующий:

class className:

    @classmethod
    def class_method_name(cls, params):
        pass
"""

"""
В примере ниже мы добавили новый метод класса class_hello, 
обязательно повесив на него декоратор @classmethod. 
Теперь не важно, как мы будем его вызывать: 
от класса или от экземпляра, 
все равно данный метод будет принимать в атрибут cls значение класса.
"""
class Example:

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')

Example.class_hello() # class_hello <class '__main__.Example'>
instance = Example()
instance.class_hello() # class_hello <class '__main__.Example'>


"""
Статические методы
Если вы хотите, чтобы метод вообще не был привязан ни к классу, ни к его экземплярам, 
нужно создавать его статическим. 
Для этого используется  специальный декоратор @staticmethod по следующему шаблону:

class className:

    @staticmethod
    def static_method_name(params):
        pass
"""

class Example:

    @staticmethod
    def static_hello():
        print(f'instance_hello')

Example.static_hello()  # instance_hello
instance = Example()
instance.static_hello()  # instance_hello



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Создать класс, содержащий набор функций которые конвертируют температуру 
из градусов по Цельсию в градусы по Кельвину и по Фаренгейту.
"""
class TemperatureConverter():

    @staticmethod
    def celsius_to_fahrenheit(value):
        return value * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(value):
        return (value - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(value):
        return value + 273.15

    @staticmethod
    def kelvin_to_celsius(value):
        return value - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(value):
        return round((value - 32) * 5 / 9 + 273.15, 2)

    @staticmethod
    def kelvin_to_fahrenheit(value):
        return round((value - 273.15) * 9 / 5 + 32, 2)

    @staticmethod
    def format(val, el):
        ls = ['F', 'C', 'K']
        if el in ls:
            return f"{val}°{el}"


# Код для проверки
assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0
assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
assert TemperatureConverter.fahrenheit_to_celsius(32) == 0

converter = TemperatureConverter()
assert converter.celsius_to_kelvin(100) == 373.15
assert converter.kelvin_to_celsius(273.15) == 0
assert converter.fahrenheit_to_kelvin(50) == 283.15
assert converter.kelvin_to_fahrenheit(54.0) == -362.47
assert converter.format(1653.0, 'K') == '1653.0°K'
assert converter.format(45, 'F') == '45°F'
assert converter.format(36.6, 'C') == '36.6°C'
print('Good')


# Task 02
"""
Сделать код корректным: для это нужно заменить знак _ на один из декораторов 
@staticmethod, @classmethod и @property или же просто удалить знак
"""
class RobotVacuumCleaner:
    name = 'Henry'
    charge = 25

    @classmethod
    def update_charge(cls, new_value):
        cls.charge = new_value

    @staticmethod
    def hello(name):
        return f'Привет, {name}'

    @property
    def data(self):
        return {
            'name': self.name,
            'charge': self.charge
        }

    # _
    def make_clean(self):
        if self.charge < 30:
            return 'Кожаный, заряди меня! Я слаб'
        return 'Я вычищу твою берлогу!!!'


# Код для проверки
print(RobotVacuumCleaner.hello('Господин'))  # Привет, Господин
RobotVacuumCleaner.update_charge(50)

robot = RobotVacuumCleaner()
print(robot.make_clean())  # Я вычищу твою берлогу!!!
print(robot.data)  # {'name': 'Henry', 'charge': 50}

RobotVacuumCleaner.update_charge(False)
print(robot.make_clean())  # Кожаный, заряди меня! Я слаб




# Task 03
"""
Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:
* класс-метод from_diameter, принимающий диаметр круга. Метод from_diameter должен возвращать 
  новый экземпляр класса Circle(учитывайте, что экземпляры круга создаются по радиусу);
* статик-метод is_positive, принимающий одно число. 
  Метод is_positive должен возвращать ответ, является ли переданное число положительным;
* статик-метод area, который принимает радиус и возвращает площадь круга. 
  Для этого воспользуйтесь формулой 2 pi ∗ r^2 и в качестве значения pi возьмите 3.14
"""
class Circle:
    def __init__(self, radius):
        if not self.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)  # создание нового экземпляра класса

    @staticmethod
    def is_positive(value):
        return value > 0

    @staticmethod
    def area(value):
        return 3.14 * (value ** 2)


# Код для проверки
circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 3.14
assert Circle.area(2) == 12.56
print('Good')



# Task 04
"""
Необходимо реализовать класс AppConfig, который предоставляет методы для загрузки конфигурации из JSON-файла 
и получения значений конкретных параметров.
В классе AppConfig должно быть реализовано следующее: 
* метод load_config, который загружает конфигурацию из указанного JSON-файла
* метод get_config, который принимает ключ и возвращает соответствующее значение из загруженной конфигурации. 
  Если ключ не найден, метод должен возвращать None. 
  Также необходимо предоставить возможность обращаться к вложенным параметрам через точку.

Вам будет предоставлен файл 'app_config.json', который имеет следующее содержимое:
{
  "database": {
    "host": "127.0.0.1",
    "port": 5432,
    "database_name": "postgres_db",
    "user": "owner",
    "password": "ya_vorona_ya_vorona"
  },
  "api_key": "hUFHu834837248jhoiHF89",
  "log_level": "debug",
  "max_connections": 10
}
Необходимо реализовать возможность вызова перечисленных методов как через класс, так и через экземпляр. 
Также необходимо обеспечить распространение значений параметров на все экземпляры класса AppConfig. 
Это значит, что все экземпляры AppConfig должны иметь одинаковые значение конфигурации приложения.
"""
import json

class AppConfig():

    @classmethod
    def load_config(cls, filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            cls.data = json.load(file)


    @classmethod
    def get_config(cls, key: str):
        dic = cls.data
        ls_key = key.split('.')

        # Решение на любой уровень вложенности
        for key in ls_key:
            dic = dic.get(key)  # Новый словарь или значение по ключу
            if dic is None:
                return None
        return dic

        # Ограниченное решение о глубине словаря (2 уровня вложения)
        # if len(ls_key) == 1:
        #     return dic.get(key)
        # if len(ls_key) == 2:
        #     try:
        #         if dic[ls_key[0]][ls_key[1]]:
        #             return dic[ls_key[0]][ls_key[1]]
        #     except:
        #         return None


# Код для проверки
# Загрузка конфигурации при запуске приложения
AppConfig.load_config('app_config.json')

# Получение значения конфигурации
assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None
#
config = AppConfig()
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None
#
conf = AppConfig()
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None
print('Good')
