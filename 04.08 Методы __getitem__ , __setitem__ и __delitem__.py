#  4.8 Методы __getitem__ , __setitem__ и __delitem__
""""""

"""
Магический метод __getitem__
позволяет добавить возможность обращения к экземплярам вашего класса по индексу или ключу
У данного метода следующий синтаксис:

def __getitem__(self, item):
Параметр item принимает значение индекса, которое используется при индексировании. 


Магический метод __setitem__
возможность установить новое значение. 
Определение метода __setitem__ должно быть следующем

def __setitem__(self, key, value):
Здесь параметр key принимает значение индекса или ключа,  
которое было указано в квадрантных скобках, а в параметр value поступает значение, 
которое стоит слева от знака присваивания. 


Магический метод __delitem__
позволяет удалять значения. 
синтаксис:

def __delitem__(self, key):
Параметр key принимает значение индекса или ключа, которое необходимо удалить
"""


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
В классе Building должно быть реализовано:
метод __init__, который принимает количество этажей в здании
метод __setitem__, который закрепляет за определенным этажом компанию. 
Если этаж был занят другой компанией, нужно заменить название другой компанией
метод __getitem__, который возвращает название компании с этого этажа. 
В случае, если этаж пустует, следует вернуть None
метод __delitem__, который высвобождает этаж
"""
class Building:

    def __init__(self, level):
        self.house = [None] * level
        # self.house = [None for _ in range(level)]

    def __getitem__(self, key):
        if 0 <= key <= len(self.house):
            return self.house[key]
        else:
            raise IndexError("Индекс за пределами списка")

    def __setitem__(self, key, val):
        if 0 <= key <= len(self.house):
            self.house[key] = val


    def __delitem__(self, key):
        if 0 <= key <= len(self.house):
            self.house[key] = None
        else:
            raise IndexError("Индекс за пределами списка")

# Короче.
class Building:

    def __init__(self, level):
        self.level = level
        self.house = [None] * level

    def __getitem__(self, key):
        if 0 <= key < self.level:
            return self.house[key]

    def __setitem__(self, key, val):
        if 0 <= key < self.level:
            self.house[key] = val

    def __delitem__(self, key):
        if 0 <= key < self.level:
            self.house[key] = None

# Код для проверки
iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])


# Task 02
"""
создадим аналог плейлиста, для этого понадобиться реализовать два класса Song и Playlist

Класс Song должен содержать:
метод __init__, который сохраняет в экземпляре два атрибута title и artist: название песни и исполнитель

Класс Playlist должен содержать:
метод __init__. , который создает в экземпляре атрибут songs. Изначально должен быть пустым списком;
метод __getitem__ , который возвращает песню из атрибута songs по индексу
метод __setitem__ , который добавляет песню в атрибут songs в указанный индекс. 
 При этом нужно сдвинуть уже имеющиеся песни вправо, у которых индекс был до момента вставки равен или больше переданного
метод add_song, который добавляет песню в конец плейлиста
"""
class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:

    def __init__(self):
        self.songs = list()

    def __getitem__(self, key):
        if isinstance(key, int):
            if 0 <= key < len(self.songs):
                return self.songs[key]

    def __setitem__(self, key, value):
        if isinstance(key, int) and isinstance(value, Song):
            if 0 <= key < len(self.songs):
                self.songs.insert(key, value)

    def add_song(self, value):
        if isinstance(value, Song):
            self.songs.append(value)


# Код для проверки
playlist = Playlist()
assert len(playlist.songs) == 0
assert isinstance(playlist, Playlist)
playlist.add_song(Song("Paradise", "Coldplay"))
assert playlist[0].title == 'Paradise'
assert playlist[0].artist == 'Coldplay'
assert len(playlist.songs) == 1

playlist[0] = Song("Resistance", "Muse")
assert playlist[0].title == 'Resistance'
assert playlist[0].artist == 'Muse'
assert playlist[1].title == 'Paradise'
assert playlist[1].artist == 'Coldplay'

playlist[1] = Song("Helena", "My Chemical Romance")
assert playlist[1].title == 'Helena'
assert playlist[1].artist == 'My Chemical Romance'

assert playlist[2].title == 'Paradise'
assert playlist[2].artist == 'Coldplay'
print('Good')



# Task 03
"""
реализовать класс ShoppingCart. В нем должно содержаться следующее:

метод __init__. , который создает в экземпляре атрибут items. 
Изначально должен быть пустым словарем, в нем будут содержаться покупки;
 
метод __getitem__ , который возвращает по названию товара его текущее количество или 0, 
если товар отсутствует в корзине 
 
метод __setitem__ , который проставляет по названию товара его количество в корзине. Е
сли товар отсутствовал, его необходимо добавить, если присутствовал - нужно проставить ему новое количество
 
метод __delitem__ , который удаляет товар из корзины
 
метод add_item, который добавляет товар к текущим. 
Это значит, что если товар уже присутствовал в корзине, то необходимо увеличить его количество. 
Если товар отсутствовал, нужно его добавить. 
Данный метод принимает обязательно название товара и необязательно его количество 
(по умолчанию количество равно 1).
 
метод remove_item, который удаляет некоторое количество товара из корзины. 
Если хотят удалить из корзины столько же товара, чем там имеется или больше, 
необходимо удалить его из корзины.  
В остальных случаях уменьшаем количество товара на переденное количество. 
Данный метод принимает обязательно название товара и необязательно его количество 
(по умолчанию количество равно 1). Предусмотрите ситуацию, когда удаляемый товар отсутствует в корзине
"""
from collections import defaultdict
class ShoppingCart:

    def __init__(self):
        self.items = defaultdict(int)
        # self.items = dict()  # без defaultdict

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]

    def add_item(self, key, value=1):
        # self.items.setdefault(key, 0)  # без defaultdict
        self.items[key] += value

    def remove_item(self, key, value=1):
        if key in self.items:
            if self.items[key] > value:
                self.items[key] -= value
            else:
                del self.items[key]




# Код для проверки
# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")
print('Good')


