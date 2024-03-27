#  6.5 Пользовательские исключения в Python
""""""

class MyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('__str__ called')
        if self.message:
            return f'My exception: {self.message}'
        else:
            return 'My exception is empty'

try:
    raise MyException('hello', 42)  # в скобках передаются аргументы в __init__
except MyException as e:
    print(e)  # My exception: hello

try:
    raise MyException('hello', 42)
except MyException:
    print('done')  # done

raise MyException('hello', 42)  # ошибка MyException: My exception: hello
print("Good")  #  этот код (и все что ниже) не отрабатывает


print(" - " * 10)
# Необходимо верно указывать класс исключения
# в данном примере LookupError и ArithmeticError - разные ветки исключений
class MyException(LookupError):
    pass

try:
    raise MyException('hello', 42)
except ArithmeticError:
    print('done')  # код не отрабатывает


# *  *  *  *  *   Task   *  *  *  *  *


# Task 01
"""
Дописать функцию get_user: 
она должна принимать логин пользователя и возвращать имя пользователя из словаря users. 
Если логин отсутствует, необходимо возбуждать исключение UserNotFoundError 
с текстом User not found

Реализовать класс-исключение UserNotFoundError
"""
class UserNotFoundError(KeyError):
    def __str__(self):
        return "User not found"

users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}

def get_user(username):
    if username not in users:
        raise UserNotFoundError()
    return users[username]['name']


try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)


# Task 02
"""
Создайте класс BankAccount, который представляет банковский счет, у которого есть:

метод __init__, принимающий баланс(атрибут balance)
 
метод deposit для пополнения баланса. Если пользователь пытается внести отрицательную сумму на счет, 
должно возникать исключение NegativeDepositError("Нельзя пополнить счет отрицательным значением"):
 
метод withdraw для вывода денег. Если пользователь пытается снять больше денег, чем есть на счете, 
должно возникать исключение InsufficientFundsError("Недостаточно средств для снятия")

Также необходимо создать исключения NegativeDepositError и InsufficientFundsError
"""
class NegativeDepositError(Exception):
    def __str__(self):
        return "Нельзя пополнить счет отрицательным значением"

class InsufficientFundsError(Exception):
    def __str__(self):
        return "Недостаточно средств для снятия"


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value < 0:
            raise NegativeDepositError
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            raise InsufficientFundsError
        self.balance -= value


# Код для проверки
try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')

try:
    raise NegativeDepositError("Внесено отрицательное значение")
except Exception as e:
    if not isinstance(e, NegativeDepositError):
        raise ValueError('Реализуйте исключение NegativeDepositError')

account = BankAccount(100)
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(75)
assert account.balance == 75

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(e)  # "Недостаточно средств для снятия"

assert account.balance == 75

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)  # "Нельзя пополнить счет отрицательным значением"
print("Good")


# Task 03
"""
реализовать базовым класс исключения PasswordInvalidError, 
который наследуется от стандартного класса исключений Exception. 
Этот класс можно использовать для обработки любых общих ошибок, связанных с неверными паролями.
От него нужно унаследовать следующие классы:
PasswordLengthError представляет ошибку, связанную с недостаточной длиной пароля;
PasswordContainUpperError представляет ошибку, связанную с отсутствием заглавных букв в пароле;
PasswordContainDigitError представляет ошибку, связанную с отсутствием цифр в пароле.
 
Создайте класс User с атрибутами username и password(пароль по умолчанию None). 
Класс должен иметь метод set_password, который принимает пароль и устанавливает его как значение атрибута password. 
Метод set_password должен также проверять, соответствует ли пароль заданным требованиям безопасности:

Длина пароля должна быть не менее 8 символов 
(наче генерируется исключение PasswordLengthError с текстом Пароль должен быть не менее 8 символов)
 
Пароль должен содержать хотя бы одну заглавную букву 
(наче генерируется исключение PasswordContainUpperError с текстом Пароль должен содержать хотя бы одну заглавную букву)
 
Пароль должен содержать хотя бы одну цифру 
(наче генерируется исключение PasswordContainDigitError с текстом Пароль должен содержать хотя бы одну цифру)
"""
class PasswordInvalidError(Exception):
    pass

class PasswordLengthError(PasswordInvalidError):
    def __str__(self):
        return "Пароль должен быть не менее 8 символов"

class PasswordContainUpperError(PasswordInvalidError):
    def __str__(self):
        return "Пароль должен содержать хотя бы одну заглавную букву"

class PasswordContainDigitError(PasswordInvalidError):
    def __str__(self):
        return "Пароль должен содержать хотя бы одну цифру"


class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, value: str):
        if len(value) < 8:
            raise PasswordLengthError
        if not any(el.isupper() for el in value):
            raise PasswordContainUpperError
        if not any(el.isdigit() for el in value):
            raise PasswordContainDigitError
        self.password = value


# Код для проверки
assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'
print("Good")
