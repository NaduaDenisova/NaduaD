# Задача 1 (Базовое наследование)
# Создай:
# Класс Animal с методом eat() (выводит "Ест"),
# Класс Dog, который:
# Наследует Animal,
# Добавляет метод bark() (выводит "Гав").
class Animal:

    def eat(self):
        return "Ест"


class Dog(Animal):

    def bark(self):
        return "Гав"


dog = Dog()
print(dog.eat())
print(dog.bark())

# Задача 2Создай:
# Класс Bird с методом move() (возвращает "Летит"),
# Класс Penguin, который:
# Наследует Bird,
# Переопределяет move() (возвращает "Плывет").
class Bird:

    def move(self):
        return "Летит"


class Penguin(Bird):

    def move(self):
        return "Плывет"


berd = Penguin()
print(berd.move())

# Задача 3Создай:
# Класс Vehicle с методом start() (возвращает "Двигатель запущен"),
# Класс Car, который:
# Наследует Vehicle,
# Добавляет метод drive(), где:
# Сначала вызывается start(),
# Затем возвращается "Едет".
class Vehicle:

    def start(self):
        return "Двигатель запущен"


class Car(Vehicle):

    def drive(self):
        return f"{super().start()}\nЕдет" #super метод вызова родительского метода, новое!!!! запомнить


car = Car()
print(car.drive())

# Задача 4
# Создай иерархию классов:
# Базовый класс Electronics с методом power_on() (возвращает "Питание включено"),
# Класс Phone, который:
# Наследует Electronics,
# Добавляет метод call() (возвращает "Звонок..."),
# Класс SmartPhone, который:
# Наследует Phone,
# Добавляет метод play_game() (возвращает "Запуск игры").
class Electronics:

    def power_on(self):
        return "Питание включено"


class Phone(Electronics):
    def call(self):
        return "Звонок..."


class SmartPhone(Phone):
    def play_game(self):
        return "Запуск игры"


phone = SmartPhone()
print(phone.power_on())
print(phone.call())
print(phone.play_game())






















