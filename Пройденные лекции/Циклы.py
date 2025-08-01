# Задача 1 (Цикл for)
# Напиши код, который выводит каждый элемент списка в отдельной строке
fruits = ["яблоко", "банан", "вишня"]
for fruit in fruits:
    print(fruit)

# Задача 2 (Функция range)
# Напиши код, который выводит все чётные числа от 2 до 10 (включительно), используя range и цикл for.
for result in range(2, 11, 2):
    print(result)

# Задача 3 (Цикл while)
# Напиши код, который выводит числа от 5 до 1 в обратном порядке, используя while. После числа 1 выведи слово "Старт!".

count = 5
while count > 0:
    print(count)
    count -= 1
print("Старт!")

# Задача 4 (Цикл while + break)
# Напиши код, который выводит числа от 10 до 1 в обратном порядке,
# но прерывает цикл, если встречает число 3. После прерывания выведи фразу "Цикл остановлен".
count = 10
while count > 0:
    print(count)
    if count == 3:
        print("Цикл остановлен")
        break
    count -= 1

# Задача 5 (Цикл while + break)
# Напиши код, который выводит чётные числа от 20 до 0 (включительно), но прерывает цикл, если встречает число,
# которое делится на 5 без остатка.
# После прерывания выведи "Найдено число X!" (где X — это то самое число).

count = 20
while count > 0:
    print(count)
    if count // 5:
        print("Найдено число X!")
        break
    count //= 2

# Задача 6 (Цикл for + пропуск элементов)
# Напиши код, который выводит только нечётные числа из списка
# numbers = [10, 21, 4, 7, 12, 33], используя цикл for и условие if.
numbers = [10, 21, 4, 7, 12, 33]
for number in numbers:
    if number % 2 != 0:
        print(number)

# Задача 7 (Цикл for + range)
# Напиши код, который выводит числа от 15 до 30 (включительно), кроме чисел, кратных 4 (например, 16, 20, 24...).
for result in range(15, 31):
    if result % 4 != 0:
        print(result)

# Задача 8 (Цикл while с условием)
# Напиши код, который выводит квадраты чисел от 1 до N (N вводит пользователь),
# но останавливается, если квадрат превышает 100.
N = int(input("Введите N: "))
i = 1
while i <= N:
    square = i ** 2
    if square > 100:
        print("Конец (превышен лимит 100)")
        break
    print(square)
    i += 1






