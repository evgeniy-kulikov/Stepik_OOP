# 7.2 Протокол
""""""

"""
В Python 3.8. появилась новая примечательная возможность — протоколы (PEP-544). 
Протоколы — это альтернатива абстрактным базовым классам. 
Они позволяют определить свой набор методов, который другие классы должны реализовать, 
чтобы соответствовать данному протоколу, но без наследования и иерархии. 
Протоколы осуществляют проверку совместимости классов исключительно на основе анализа их атрибутов и методов
"""

from typing import Protocol

class Animal(Protocol):
    def walk(self) -> None:
        ...  # ...  равнозначно pass

    def speak(self) -> None:
        ...

#  чтобы соответствовать протоколу Animal другой класс должен иметь в реализации методы walk и speak.
class Dog:
    def walk(self) -> None:
        print("This is a dog walking")

    def speak(self) -> None:
        print("Woof!")


def make_animal_speak(animal: Animal) -> None:
    animal.speak()


dog = Dog()
make_animal_speak(dog)
