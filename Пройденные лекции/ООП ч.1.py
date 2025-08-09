# Задача 1
# Создай пустой класс Car.
class Car:
    pass


My_car = Car()

# Задача 2
# Добавь в класс Car конструктор __init__, который:
# Принимает параметр model (модель машины),
# Сохраняет его в атрибут объекта self.model.
class Car:
    def __init__(self, model):
        self.model = model


my_car = Car("Mersedes")
print(my_car.model)

# Задача 3
# Добавь в класс Car метод start_engine(), который:
# Не принимает параметров (кроме self)
# Возвращает строку "Двигатель запущен"
class Car:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return ("Двигатель запущен")


my_car = Car("BMW")
print(my_car.start_engine())

# Задача 4
# Добавь в класс Car атрибут класса WHEELS = 4 (у всех машин по умолчанию 4 колеса).
class Car:
    WHEELS = 4


print(Car.WHEELS)

# Задача 5
# Добавь в класс Car метод get_model(), который:
# Не принимает аргументов (кроме обязательного self),
# Возвращает значение атрибута self.model.
class Car:
    def __init__(self, model):
        self.model = model

    def get_model(self):
        return self.model


my_car = Car("bmW")
print(my_car.get_model())

# Задача 6Создай:
# Класс Book с конструктором, принимающим title (название) и author (автор)
# Объект my_book класса Book с произвольными названием и автором
# Выведи оба атрибута объекта
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


my_book = Book("У лукоморья", "Пушкин")
print(my_book.title, my_book.author)

# Задача 7
# Добавь в класс Book метод get_info(), который возвращает строку в формате:
# "Название: {title}, Автор: {author}"
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Название: '{self.title}', Автор: '{self.author}'"


my_book = Book("У лукоморья", "Пушкин")
print(my_book.get_info())

# Задача 8
# Добавь в класс Book атрибут класса library_name = "Моя библиотека". Затем:
# Создай объект my_book,
# Выведи этот атрибут и через класс, и через объект.
class Book:
    library_name = "Моя библиотека"



my_book = Book()
print(Book.library_name)
print(my_book.library_name)
