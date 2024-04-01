#  10.3 Класс type
""""""



# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
""" 
Определить класс Dog через класс type

"""

# Определение класса Dog
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'


class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def description(self):
    return f'{self.name} is {self.age} years old'

def speak(self, sound):
    return f'{self.name} says {sound}'
"""

class_namespace = {}
exec(class_body, globals(), class_namespace)

class_name = 'Dog'
class_bases = tuple()
Dog = type(class_name, class_bases, class_namespace)


# Код для проверки
curt = Dog("Curt", 4)
print(curt.name)
print(curt.age)
print(curt.description())
print(curt.speak('Wo'))
print(curt.speak('Bow'))
print(isinstance(curt, Dog))