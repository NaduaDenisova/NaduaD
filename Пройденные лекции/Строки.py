#Задача 1 (Доступ к символам):Дана строка:
text = "Python"
#Напиши код, который выводит третий символ этой строки.
result = text [ 2 ]
print(result)

#Задача 2 (Срезы):Дана строка:
text = "автоматизация"
#Напиши код, который выводит подстроку с 3-го по 7-й символ включительно (индексы: с 2 по 6).
result = text [2: 7:]
print (result)

#Задача 3 (F-строки):Даны переменные:
language = "Python"
version = 3.12
#Напиши код, который выводит строку в формате:"Я изучаю Python версии 3.12", используя f-строку.
result = f"Я изучаю {language} версии {version}"
print (result)

#Задача 4 (Базовые методы строк):Дана строка:
text = "   роботы это будущее!   "
#Напиши код, который:Удаляет пробелы в начале и конце строки
#Переводит первый символ в верхний регистр
#Выводит результат Пример вывода:
"Роботы это будущее!"
result = text.strip()
result1 = result [0].upper() + result[1::]
print (result1)

#Задача 5 (Конкатенация строк):Даны переменные:
word1 = "Авто"
word2 = "матизация"
#Напиши код, который соединяет их в одну строку без пробела и выводит результат.
#Пример вывода:"Автоматизация"Условие: Реши без f-строк, только конкатенация (+).
result = (word1 + word2)
print (result)

#Задача 6 (Получение длины строки):
text = "Пайтон"
#Напиши код, который выводит количество символов в этой строке.
print (len (text) )

#Задача 7 (Создание строки):Напиши код, который:
#Создаёт строку "Программирование" в переменной word.Выводит её на экран.
word = "Программирование"
print (word)

#Задача 9 (Срезы с шагом):Дана строка:
text = "автоматизировать"
#Напиши код, который выводит каждый второй символ строки, начиная с первого (индекс 0).
result = text [0: :2]
print (result)