# Задача 1 (Создание словаря)
# Создай словарь book со следующими ключами и значениями:Затем выведи весь словарь на экран.
book = {
    "title": "Гарри Поттер",
    "author": "Дж. Роулинг",
    "year": 1997
}
print(book)

# Задача 2 (Доступ к элементам словаря)
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}
# Выведи значение ключа "model" в формате:"Модель: Corolla"
# Дополнительное задание (если хочешь сложнее):
# Проверь, есть ли в словаре ключ "color". Если нет — выведи "Ключ 'color' отсутствует".
print("Модель: " + car["model"])
print(f"Модель: {car['model']}")
if "color" in car:
    print("Ключ")
else:
    print("Ключ 'color' отсутствует")

# Задача 3 (Добавление и обновление элементов словаря)
laptop = {"brand": "Lenovo", "ram": 16, "storage": 256}
# Добавь новый ключ "storage" со значением 256
# Обнови значение ключа "ram" на 16
# Выведи изменённый словарь
print(laptop)
if "processor" not in laptop:
    laptop["processor"] = "Intel Core i5"
    print(laptop)

# Задача 4 (Удаление элементов словаря)
student = {
    "name": "Анна",
    "age": 20,
    "course": "Информатика",
    "grade": "A"
}
# Удали ключ "grade" с помощью метода pop()
# Удали любой элемент с помощью popitem() (без указания ключа)
# Выведи оставшийся словарь и отдельно выведи:
# Значение удалённого через pop()
# Пару ключ-значение, удалённую через popitem()
result = student.pop("grade")
result2 = student.popitem()
print(student)
print(result)
print(result2)

# Задача 5 (Получение элементов, ключей и значений словаря)
country = {
    "name": "Япония",
    "capital": "Токио",
    "population": 125_800_000,
    "language": "японский"
}
# Выведи все ключи словаря через пробел (используй метод словаря)
# Выведи все значения словаря через запятую с пробелом
# Выведи все пары ключ-значение построчно (каждая пара с новой строки)
result = country.keys()
print(result)
result2 = country.values()
print(result2)
result3 =country.items()
print(result3)

# Задача 6 (Проверка на наличие ключей и значений)
smartphone = {
    "brand": "Xiaomi",
    "model": "Redmi Note 10",
    "year": 2021,
    "OS": "Android"
}
# Проверь, есть ли в словаре ключ "price". Если нет — выведи "Ключ 'price' отсутствует"
# Проверь, есть ли среди значений "iOS". Если нет — выведи "Значение 'iOS' не найдено"
# Дополнительно: Выведи список всех ключей, у которых значения являются строками
if"price"in smartphone:
    print("key in dict")
else:
    print("Ключ 'price' отсутствует")
if"iOS"in smartphone:
    print("Значение присутствует")
else:
    print("Значение 'iOS' не найдено")








