
#Задача 1 (Получение элементов списка):Дан список:
fruits = ["apple", "banana", "cherry", "orange"]
#Напиши код, который выводит третий элемент списка.
print (fruits [2])

#Задача 2 (Добавление элементов в список):Дан список:
numbers = [10, 20, 30]
#Допиши код, чтобы:Добавить число 40 в конец списка.Вывести обновлённый список.
numbers.append(40)
print (numbers)

#Задача 3 (Срезы списка):Дан список:
letters = ["a", "b", "c", "d", "e", "f"]
#Напиши код, который выводит срез списка со второго по четвёртый элемент (включительно).
result = letters [1:4:]
print (result)

#Задача 4 (Замена элементов в списке):Дан список:
colors = ["red", "blue", "green", "yellow"]
#Замени второй элемент списка на "purple" и выведи обновлённый список.
colors [1] = "purple"
print (colors)

#Задача 5 (Удаление элементов из списка):
animals = ["cat", "dog", "elephant", "giraffe", "tiger"]
#Удали третий элемент списка и выведи результат.
del animals [2]
print (animals)

#Задача 6 (Добавление элементов в конкретное место списка):
numbers = [1, 2, 4, 5]
#Вставь число 3 между 2 и 4 (т.е. на позицию с индексом 2) и выведи список.
numbers.insert(2,3)
print(numbers)

#Задача 7 (Слияние списков):
list1 = [1, 2, 3]
list2 = [4, 5, 6]
#Объедини их в один список и выведи результат.
print ( list1 + list2 )

#Задача 8 (Очистка списка):
items = ["book", "pen", "notebook", "pencil"]
#Очисти список полностью и выведи его.
items.clear()
print(items)


