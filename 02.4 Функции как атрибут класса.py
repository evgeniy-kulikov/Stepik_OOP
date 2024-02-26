# 2.4 Функции как атрибут класса
""""""

class Car:
  model = "BMW"
  engine = 1.6

  def drive():  # нет аргумента self
    print("Let's go")

Car.drive()  # Let's go
getattr(Car, 'drive')()  # Let's go

auto = Car()
auto.drive()  # TypeError !!!


class NewCar:
  model = "BMW"
  engine = 1.6

  @staticmethod  # Декоратор @staticmethod позволяет вызывать функцию как от класса, так и от ЭК
  def drive():  # нет аргумента self
    print("Let's go again!")

auto = NewCar()
auto.drive()  # Let's go again!
