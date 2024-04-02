#  10.2 Паттерн Singleton
""""""

"""
Синглтон (Singleton) — это паттерн проектирования, который гарантирует, 
что класс имеет только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру. 
Этот экземпляр обычно предоставляет доступ к определенным ресурсам или службам, 
таким как база данных, файловая система, или любая другая общая ресурсоемкая операция.

Идея синглтона заключается в ограничении количества экземпляров, 
которые может иметь данный класс, только одним значением.

Основные черты синглтона:

Одиночный экземпляр: синглтон гарантирует, что у класса есть только один экземпляр, 
и предоставляет глобальную точку доступа к этому экземпляру.

Глобальный доступ: экземпляр синглтона обычно предоставляет 
статический метод или свойство для доступа из любой точки программы.

Ленивая инициализация: экземпляр синглтона часто создается только при первом вызове, 
что позволяет отложить его создание до момента реальной необходимости. 
Созданный экземпляр сохраняется внутри класса и будет возвращаться при повторных вызовах.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

instance_1 = Singleton()
instance_2 = Singleton()

print(id(instance_1))  # 140510704405232
print(id(instance_2))  # 140510704405232
print(instance_1 is instance_2)  # True


# Альтернатива. Паттерн (шаблон) мотостояние
# Создаются разные экземпляры класса Monostate, но с одинаковыми атрибутами/методами
class Monostate:
    _shared_state = {}
    def __init__(self):
        if not self._shared_state:
            self.my_attr = 'my_value'


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
создать класс Logger, который предоставляет глобальный доступ к одному экземпляру логгера в приложении. 
Класс Logger имеет атрибут log_level, который хранит текущий уровень логирования, 
по умолчанию нужно проставить значением INFO

Класс Logger также должен иметь:

метод класса set_level, который принимает новый уровень логирования и записывает его в атрибут log_level. 
При этом обязательно проверьте был ли создан экземпляр. 
В случае отсутствия экземпляра необходимо необходимо возбуждать исключение  ValueError('The instance has not created')

статический метод get_logger, который возвращает экземпляр синглтона. 
Если экземпляр еще не существует, его необходимо создать 
"""
class Logger:
    _instance = None
    log_level = "INFO"

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    @classmethod
    def set_level(cls, val):
        if not cls._instance:
            raise ValueError('The instance has not created')
        cls.log_level = val

    @staticmethod
    def get_logger():
        if not Logger._instance:
            Logger.__new__(Logger)
        return Logger._instance


# Код для проверки
try:
    logger_1 = Logger.set_level("DEBUG")
except ValueError as ex:
    print(ex)

logger_1 = Logger.get_logger()
print(logger_1.log_level)  # "INFO"
Logger.set_level("DEBUG")
print(logger_1.log_level)  # "DEBUG"

logger_2 = Logger.get_logger()
print(logger_2.log_level)  # "DEBUG"
print(logger_2 is logger_1)  # True


# Task 02
"""
Имеется несколько пустых классов и на каждым вещается декоратор singleton, который нужно реализовать
Функция-декоратор singleton должна сохранять в себе 
для каждого класса один созданный экземпляр при первом вызове. 
При последующих вызовах возвращать ранее созданный экземпляр для данного класса
"""
# Функция декоратор
# def decorator(func):
#     def inner():
#         func()
#     return inner


def singleton(cls):
    class Singleton:
        _instance = None

        def __new__(cls):
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance

    return Singleton


@singleton
class Logger:
    pass

@singleton
class AppConfig:
    pass

@singleton
class SMTPServerConfig:
    pass


# Код для проверки
log = Logger()
app_conf = AppConfig()
app_conf_2 = AppConfig()
smtp_conf = SMTPServerConfig()
assert log is Logger()
assert app_conf is app_conf_2
assert smtp_conf is SMTPServerConfig()
assert log is not app_conf
assert log is not smtp_conf
assert app_conf is not smtp_conf
print('Good')
