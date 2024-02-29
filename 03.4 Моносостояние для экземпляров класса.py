#  3.4 Моносостояние для экземпляров класса
""""""

"""
Моносостояние можно создать при помощи одного общего словаря __shared_attr
__shared_attr — общий словарь для всего пространства имён, 
к которому имеет доступ каждый создаваемый экземпляр класса и изменения которого отражаются во всех ЭК. 
При инициализации мы подменяем личный словарь атрибутов у ЭК на наш общий словарь __shared_attr
"""

class Cat:
    __shared_attr = {      # Формирование единого словаря атрибутов класса
        'breed': 'pers',   # При изменении значений - эти значения обновятся
        'color': 'black'   # во всех экземплярах класса
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr  # Передаём в инициализатор ссылку на
                                           # созданный моно-словарь


cat1 = Cat()
cat2 = Cat()
print(cat1.__dict__)  # {'breed': 'pers', 'color': 'black'}
print(cat2.__dict__)  # {'breed': 'pers', 'color': 'black'}
cat1.breed, cat1.color = 'pers', 'white'  # Меняем атрибуты у cat1
print('cat1:', cat1.__dict__)  # {'breed': 'pers', 'color': 'white'}
print('cat2:', cat2.__dict__)  # {'breed': 'pers', 'color': 'white'}
cat2.breed, cat2.color = 'siam', 'gray'  # Меняем атрибуты у cat2
print('cat1:', cat1.__dict__)  # {'breed': 'siam', 'color': 'gray'}
print('cat2:', cat2.__dict__)  # {'breed': 'siam', 'color': 'gray'}


# При этом, мы можем добавлять новые параметры через экземпляр класса,
# которые также будут отражены в других ЭК.

class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


cat1 = Cat()
cat2 = Cat()
cat1.weight = 5  # Добавляем параметр в ЭК
print('cat1:', cat1.__dict__)  # {'breed': 'pers', 'color': 'black', 'weight': 5}
print('cat2:', cat2.__dict__)  # {'breed': 'pers', 'color': 'black', 'weight': 5}


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Определить класс WeatherStation, у которого
имеются разделяемые атрибуты temperature, humidity и pressure. 
Вот их начальные состояния:
{"temperature": 0, "humidity": 0, "pressure": 0}
метод update_data, который изменяет состояние сразу трех показаний.
метод get_current_data, который возвращает кортеж показаний  temperature, humidity и pressure.
"""
class WeatherStation:
    __shared_attr = {"temperature": 0, "humidity": 0, "pressure": 0}

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr

    def update_data(self, temperature, humidity, pressure):
        # self.temperature = temperature
        # self.humidity = humidity
        # self.pressure = pressure
        self.__dict__.update({"temperature": temperature, "humidity": humidity, "pressure": pressure})

    def get_current_data(self):
        # return self.temperature, self.humidity, self.pressure
        return tuple(self.__dict__.values())
