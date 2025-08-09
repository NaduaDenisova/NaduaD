# Напиши декоратор @repeat_call(n), который вызывает декорируемую функцию n раз и возвращает список результатов.
# @repeat_call(3)
# def get_number():
#     return 42
#
# print(get_number())

def repeat_call(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(times):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return decorator

@repeat_call(3)
def get_number():
    return 42
print(get_number())

# Задача 1 (Создание и вызов функций)
# Напиши функцию print_hello(), которая выводит (не возвращает) строку "Hello!". Затем вызови эту функцию.

def print_hello():
    print("Hello!")


print_hello()

# Задача 2
# Напиши функцию multiply(a, b), которая:
# Принимает два числа a и b,
# Возвращает их произведение (не выводит!).
def multiply(a, b):
    return a*b


print(multiply(9, 5))

# Задача 3
# Напиши функцию greet(name="Гость"), которая:
# Принимает один аргумент name (со значением по умолчанию "Гость"),
# Возвращает строку "Привет, {name}!".
def greet(name="Гость"):
    return f"Привет, {name}!"


print(greet())

# Задача 4
# Напиши функцию is_positive(number), которая:
# Принимает число,
# Возвращает True, если число положительное, и False — если нет.
def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(10))
print(is_positive(-5))
print(is_positive(0))

# Следующая задача (из раздела "Декораторы"):
# Задача 5
# Напиши декоратор @uppercase, который преобразует результат функции в верхний регистр.

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase
def say_hello():
    return "hello world"

print(say_hello())

# Следующая задача (из раздела "Аргументы функций"):Задача 6
# Напиши функцию power(base, exponent), которая:
# Принимает два числа: base (основание) и exponent (степень),
# Возвращает результат возведения в степень (используй оператор **).
def power(base, exponent):
    return base ** exponent


print(power(5, 7))


# Следующая задача (из раздела "Декораторы"):Задача 7
# Напиши декоратор @bold, который оборачивает результат функции в HTML-тег <b>:

def bold(func):
    def wrapper():
        result = func()
        return f"<b> {result} </b>"
    return wrapper


@bold
def get_text():
    return "Hello World"

print(get_text())


















