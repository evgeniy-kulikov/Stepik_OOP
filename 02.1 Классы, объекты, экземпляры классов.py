# 2.1 Классы, объекты, экземпляры классов
""""""
class Car:
  model = "BMW"
  engine = 1.6

a = Car()
b = Car()

print(a.model)  # BMW
print(b.engine)  # 1.6

b.model = "VAZ"  # Изменяем значение атрибута model в ЭК
b.color = 'white'  # Добавляем новый атрибут в ЭК

# проверить принадлежность объекта к определенному классу
print(25, 'Это целое число?', isinstance(25, int))  # 25 Это целое число? True


class Animal:
  pass

lion = Animal()
print(isinstance(lion, Animal))  # True
