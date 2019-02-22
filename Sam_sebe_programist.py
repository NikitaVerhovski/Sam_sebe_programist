import os
import csv
import statistics
from Dz import cuded

# Глава 4 функции

# 1
#
# def my_sqar(x):
#     """Функция прнимает значение и возводит вл 2ую степень"""
#     x =  x**2
#     return x
#
# print(my_sqar(3))
#
# # 2
#
# def string(str):
#     """функция примает значение строки и выводит строку"""
#     return print(str)
#
# string("Sosiska")
#
# # 3
#
# def five_parametr(z, x, q, a=5, b=10):
#     """функция принимает 3 обязательных элемента и 2 необязательных
#     складывает 3 обязательных с 2умя необязательными которые умножаются между собой"""
#     suma = z + x + q + (a * b)
#     return suma
#
# print(five_parametr(10, 20, 20))
#
# # 4
#
# def my_int(int):
#     """принимает целое число после чего делит его на 2 без остатка"""
#     int = int // 2
#     return int
#
# def my_int2(my_int):
#     """функция принимает целое число и умножает на 4"""
#     my_int = my_int * 4
#     return my_int
#
# print(my_int2(my_int(20)))
#
# # 5
#
# def str_in_float(x = float(input("Введите число"))):
#
#     try:
#         x = x / 4
#     except ZeroDivisionError:
#         print("Нельзя делить на 0")
#     else:
#         print("Исключений нет", "\n     x = ", x)


# str_in_float()

# Глава 5 Контейнеры

# 1. Создайте список своих любимых исполнителей
# 1ый вариант
my_favorit_musik = ["metallica", "RATM", "SOAD", "pantera", "bob marley", "black sabbat"]
print(my_favorit_musik)
# 2ой вариант
my_music = list()
my_music.append("metallica")
my_music.append("Korn")
my_music.append("AC/DC")
my_music.append("Pantera")
print(my_music)

# 2. Создайте список кортежей
geolacation = []
spb_geolacation = (56.34570, 18.95208)
sosnovo_geolacation = (60.559952, 30.247084)
print("spb", spb_geolacation, "sosnovo", sosnovo_geolacation)

# 3. Создайте словарь

me = dict()
me["r"] = 183
me["v"] = 52
me["m"] = ("Metallica", "Pantera", "Korn")
print(me)

# 4. Создайте програму которая запрашиивает ответы из 3его задания

# growt = input("Напишите ваш рост ")
# weight = input("Напишите ваш вес ")
# music = input("Напиишиите вваш любимый жанр в музыке ")
#
# if growt in me:
#     print("Ваш рост действительно", me["r"], "см")
# else:
#     print("Вы указали неправильный рост")
#
# if weight in me:
#     print("Вы хорошо себя знаете , ваш вес", me["v"], "кг")
# else:
#     print("У вас совсем другой вес ")
#
# if music in me:
#     print("Ты шаришь в музыке :", me["m"])
# else:
#     print("Ты чего?! Не помнишь")

# 5 Создайте словарь связывающий музыкантов со списком их песен
music_and_songs = {}
favorit_music = {"Metallica": ("Fade to black", "All Nightmare Long"),
                 "Pantera": ("Domination", "Cemetery Gates"),
                 "Korn": ("Kiss", "Y'all Want A Single")}

print(favorit_music)

# Глава 6 Операции со строками

# 1. Вывведите каждый список в строке Чехов

five_one = "Чехов"
print(five_one[0],
      five_one[1],
      five_one[2],
      five_one[3],
      five_one[4],
      )
print("\n")
# 2. Напишите программу которая принимает от пользователя 2 строки,
# вставляет их в строку , и выводит новую

# five_two1 = input("Куда вчера ходил? :")
# five_two2 = input("Что покупал в магазине :")
#
# print(f"Вчера я ходил  {five_two1}.\nВчера в магазине я купил {five_two2}")

# 3. Используйте метод чтобы исправить грамматическую ошибку в строке
# "олдос Хаксли родился в 1894 году"

suggestion = "олдос Хаксли родился в 1894 году"
print(suggestion.capitalize())
print("\n")
# 4 Вызовите метод который превращает строку "Где это? Кто это? Когда это? в список
stroka = "Где это? Кто это? Когда это?"
my_list = [stroka[:8], stroka[9:17], stroka[18:]]

print(my_list)
print("\n")
# 5. Превратиить спиисок ["Рыжая", "лиса", "перепрыгула", "через", "низкий",
# "забор", "."] в граматически праввильное предложение.Каждое слово должно отделятся
# пробелом, но между словом "забор" и следующей за ним точкой пробела быть не должно.

fb = ["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."]
pb = " ".join(fb)
print(pb.replace(" .", "."))
print("\n")
# 6. Заменить каждое  ввхождениие буквы "о" в строке " Ребенок - зеркало поступков
# родителей." цифрой 0.

ezji = "Ребенок - зеркало поступков родителей"
print(ezji.replace("о", "0"))
print("\n")
# 7. Используйте метод, чтобы опредилить индекс символа "м" в строке "Хемингуей"
hemenguei = "Хемингуей"
print("индекс символа м = ", hemenguei.index("м"))
print("\n")
# 8.Найдите в своей любиимой книге диалог (с кавычками) и превратите его в строку.

shantaram = "Спасибо тебе, Хасан", \
            "Не за что", \
            "Теперь мы в расчете"

shantaram = ". ".join(shantaram) + "."
print(shantaram)
print("\n")
# 9. Создайте строкккку "тритритри" , используя конкатенацию,а затем сделайте то же самое,
# только с помощью умножения

print("три" + "три" + "три")
print("три" * 3)
print("\n")

# 10. Исвлеките срез стороки так , что бы она содержала только символы до восклицательного знака.

predlojenie = "И зачем так орать!Я и в перввый раз прекрасно слышал."
print(predlojenie[:17])
print("\n")

# Глава 7. Циклы
# 1. Выведите каждый элемент из списка

list1 = ["Ходячие мертвецы",
         "Красавцы",
         "Клан сопрано",
         "Дневниики вампира"]

for i in list1:
    print(i)
print("\n")
# 2. Выведите все числа от 25 до 50

for i in range(25, 51):
    print(i)

# 3. Выведите каждый элемент из спискка первого задания вместе с индексами.

for i, show in enumerate(list1):
    new = list1[i]
    list1[i] = new

print(list1)

# 4. Напишите программу с бесконечным циклом (с возможностью ввести букву Х,чтобы выйти)и списком чисел.
# При каждом переборе цикла предлагайтепользователю отгадать число из списка и сообщайте,правильно ли он отгадал

# numbers = [10, 12, 54, 65, 76, 34, 89]
#
# while input("Go?/X") != "X":
#     x = int(input("Угадай число от 0 до 100"))
#     if x in numbers:
#         print("Ты угодал ,поздравляю")
#     else:
#         print("К сожалению ты не угодал")

# 5. Умножьте все числа в списке [8, 19, 148, 4] на все числа в списке [9, 1, 33, 83] и поместите результат в 3ий список

new_list1 = [8, 19, 148, 4]
new_list2 = [9, 1, 33, 83]
added = []

for i in new_list1:
    for j in new_list2:
        added.append(i * j)

print(added)
print("\n")

# ГЛАВА 8. Модули

# 1.Вызовите какую - нибудь функцию из модуля statistic
data = [20, 30, 40, 50, 60, 70, 80, 90]
print(statistics.median_low(data))
print(statistics.median(data))  # среднее значение медианы
print(statistics.median_high(data))
print("\n")

# 2. Создайте модуль cuded, содержащий функцию, которая принимает в качестве параметра число, возводит это число в куб
# и возращает его.Импортируйте и вызовите функцию из другого модуля

cuded.cud(3)
print("\n")

# Глава 9. ФАЙЛЫ

# 1. Найдите у себя на компьютере файл и выведите его содержимое с помощью Python

os.path.join("C", "Project", "test.txt")

with open("test.txt", "w") as f:
    f.write("Hey, i am a man\nMy name is Nikita Verhovsky\nI like is hard metal and trash metal")

with open("test.txt", "r") as test:
    print(test.read())

# 2. Напишите программу которая задает пользователю вопрос и сохраняет ответ в файл


question = []
with open("question.txt", "w") as ques:
    ques.write(input("Что полезного ты сделал сегодня?"))
    question.append(ques)

# 3. Примите элементы в списке списков и запишите их в CSV-файлы.Данные каждого списка должны быть строчкой в файле,
# при этом каждый элемент списка должен быть отделен запятой

with open("new_test.csv", "w") as new_test:
    w = csv.writer(new_test, delimiter=",")
    w.writerow(["Звездные войны", "Терминатор", "Искуственный интелект"])
    w.writerow(["Дурак", "Матильда", "Левифан"])
    w.writerow(["Люди в черном", "Я - робот", "Эволюция"])

with open("new_test.csv", "r") as test_read:
    test = csv.reader(test_read, delimiter=",")
    for row in test_read:
        print("".join(row))
