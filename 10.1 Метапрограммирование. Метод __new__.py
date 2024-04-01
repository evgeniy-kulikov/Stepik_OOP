#  10.1 Метапрограммирование. Введение. Метод __new__
""""""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Переписать класс Circle таким образом, чтобы все атрибуты и методы определялись только в методе __new__
"""
# class Circle:
#     PI = 3.14
#
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = 2 * radius
#
#     def get_radius(self):
#         return self._radius
#
#     def get_diameter(self):
#         return self._diameter
#
#     def get_area(self):
#         return self.PI * self._radius ** 2
#
#     def get_perimeter(self):
#         return 2 * self.PI * self._radius

class Circle:
    PI = 3.14

    def __new__(cls, radius):
        instance = super().__new__(cls)
        # Создаем атрибуты
        instance._radius = radius
        instance._diameter = 2 * radius
        # Создаем методы
        cls.get_radius = lambda self: self._radius
        cls.get_diameter = lambda self: self._diameter
        cls.get_area = lambda self: self.PI * self._radius ** 2
        cls.get_perimeter = lambda self: 2 * self.PI * self._radius

        return instance

# Код для проверки
circle_instance = Circle(3.5)
print(f"Radius: {circle_instance.get_radius()}")  # Radius: 3.5
print(f"Diameter: {circle_instance.get_diameter()}")  # Diameter: 7.0
print(f"Area: {circle_instance.get_area()}")  # Area: 38.465
print(f"Perimeter: {circle_instance.get_perimeter()}")  # Perimeter: 21.98



# Task 02
"""
"""
# class BaseConfig:
#     def __new__(cls, *args, **kwargs):
#         instance = super(BaseConfig, cls).__new__(cls)
#         instance.debug = False
#         instance.log_level = "INFO"
#         return instance

class BaseConfig:
    def __new__(cls, *args, **kwargs):
        instance = super(BaseConfig, cls).__new__(cls)
        instance.debug = False
        instance.log_level = "INFO"
        return instance

class EmailConfig(BaseConfig):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.smtp_server = 'smtp.gmail.com'
        instance.smtp_port = 587
        instance.username = 'boss_of_gym@gmail.com'
        instance.password = ''
        return instance

class DatabaseConfig(BaseConfig):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.db_host = '127.0.0.1'
        instance.db_port = 5432
        instance.db_name = 'cookies'
        instance.db_user = 'admin'
        instance.db_password = 'admin'
        return instance

# Код для проверки
database_config = DatabaseConfig()
print("Database Configuration:")
print(f"Host: {database_config.db_host}")
print(f"Port: {database_config.db_port}")
print(f"Database name: {database_config.db_name}")
print(f"User: {database_config.db_user}")
print(f"Password: {database_config.db_password}")
print(f"Debug: {database_config.debug}")
print(f"Logger: {database_config.log_level}")

# email_config = EmailConfig()
# print("SMTP server Configuration:")
# print(f"Server: {email_config.smtp_server}")
# print(f"Port: {email_config.smtp_port}")
# print(f"User: {email_config.username}")
# print(f"Password: {email_config.password}")
# print(f"Debug: {email_config.debug}")
# print(f"Logger: {email_config.log_level}")

# base_config = BaseConfig()
# print("Base Configuration:")
# print(f"Debug: {base_config.debug}")
# print(f"Logger: {base_config.log_level}")

# email_config = EmailConfig()
# print("SMTP server Configuration:")
# print(f"Server: {email_config.smtp_server}")
# print(f"Port: {email_config.smtp_port}")
# print(f"User: {email_config.username}")
# print(f"Password: {email_config.password}")
# print(f"Debug: {email_config.debug}")
# print(f"Logger: {email_config.log_level}")


