# 5.10 Slots: свойства(property) и наследования
""""""

"""
Все атрибуты, которые вы укажите в __slots__ дочернего класса, 
будут добавлены к именам из родительского  __slots__ . 
В нашем случае мы прописали пустую коллекцию (пустой кортеж). 
Значит в экземплярах Square можно использовать имена атрибутов, указанные в родители: 
'__width' и 'height'
"""
class Rectangle:
    __slots__ = '__width', 'height'

class Square(Rectangle):
    __slots__ = tuple()


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""

"""
class Device:
    __slots__ = ['_name', '_location', '_status']

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._status = 'ON'

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, val):
        self._location = val

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        self._status = val

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

class Light(Device):
    __slots__ = ['_brightness', '_color']

    def __init__(self, name, location, brightness, color):
        super().__init__(name, location)
        self._brightness = brightness
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, val):
        self._brightness = val

class Thermostat(Device):
    __slots__ = ['_current_temperature', '_target_temperature']

    def __init__(self, name, location, current_temperature, target_temperature):
        super().__init__(name, location)
        self._current_temperature = current_temperature
        self._target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, val):
        self._current_temperature = val

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, val):
        self._target_temperature = val


class SmartTV(Device):
    __slots__ = '_channel'

    def __init__(self, name, location, channel):
        super().__init__(name, location)
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, val):
        self._channel = val

# Код для проверки
device1 = Device('Устройство 1', 'Гостиная')
assert device1.name == 'Устройство 1'
assert device1._name == 'Устройство 1'
assert device1.location == 'Гостиная'
assert device1._location == 'Гостиная'
assert device1.status == 'ON'
assert device1._status == 'ON'

device1.turn_off()
assert device1.status == 'OFF'
device1.location = 'Кухня'
assert device1.location == 'Кухня'
assert device1._location == 'Кухня'
device1.turn_on()
assert device1.status == 'ON'

light1 = Light('Лампа', 'Гостиная', 50, 'белый')
light1.name == 'Лампа'
light1.location == 'Гостиная'
light1.status == 'ON'
light1.brightness == '50'
light1.color == 'белый'

light1.turn_off()
light1.status == 'OFF'

thermostat_1 = Thermostat('Термометр', 'Балкон', 10, 15)
thermostat_1.name == 'Термометр'
thermostat_1.location == 'Балкон'
thermostat_1.status == 'ON'
thermostat_1.current_temperature == 10
thermostat_1.target_temperature == 15

tv = SmartTV('Samsung', 'Спальня', 20)
tv.name == 'Термометр'
tv.location == 'Балкон'
tv.status == 'ON'
tv.channel == 20
print('GOOD')
