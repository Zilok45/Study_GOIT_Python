'''
a = 1
b = 2
c = 3
d = 10 #необов'язково використовувати

#  За допомогою арифметичних операцій та функцій перетворення типів
#  1. отримати значення 123
#  2. отримати значення 15
#  Використовувати a, b, c  обов'язково.
'''
a = 1
b = 2
c = 3
d = 10  # необов'язково
result = a * d**2 + b*d +c
print(result)

'''
#  У Харкові відкривають у бомбосховищі школу для молодших школярів.
# Треба  обладнати три кімнати партами. Парта  - на дві людини.
# Програмі подається на вхід три числа (трьома input)  - кількість учнів в кожному
# класі. Програма має порахувати необхідну кількість парт загалом.
'''
''''
schoolboy_room1 = int(input("введіть кількість учнів Класу 1: "))
schoolboy_room2 = int(input("введіть кількість учнів Класу 2: "))
schoolboy_room3 = int(input("введіть кількість учнів Класу 3: "))

table_for_room1 = schoolboy_room1 % 2 + schoolboy_room1 // 2
table_for_room2 = schoolboy_room2 % 1 + schoolboy_room2 // 2
table_for_room3 = schoolboy_room3 % 1 + schoolboy_room3 // 2

print(f"Потрібно для 1 Класу {table_for_room1} парт")
print(f"Потрібно для 2 Класу {table_for_room2} парт")
print(f"Потрібно для 3 Класу {table_for_room3} парт")
print(f"Всього потрібно парт {table_for_room1 + table_for_room2 + table_for_room3}")
'''
'''
З початку доби пройшло n хвилин. Програма приймає це число input-ом. 
Який час буде показувати електроне табло годинника ?
Програма має вивести два числа - години (від 0 до 23), та 
хвилини (від 0 до 59).
'''
'''
minutes_input = int(input("Введіть кількість хвилин від 0 до 59: "))
hour = minutes_input// 60 % 24
minutes = minutes_input % 60
print(hour, minutes, sep=':', end="!") 
'''
'''
Дано текст і потрібно знайти його перше слово.

Даний текст містить англійські букви та пробіли.
На початку та у кінці пробілів немає.
'''
''''
a = input("enter text ") + " "
s = a.find(" ")
print(a[:s])
'''
'''
Дано текст і потрібно знайти його перше слово.

Даний текст містить англійські букви та пробіли.
На початку та у кінці пробілів немає.

'''
'''
Твоя задача знайти, на яку кількість нулів закінчується передане число.
'''
'''
number = str (input ("Введіть число: "))
s = number[: : -1]
s = int(s)
x = len(str(s))
y = len(number)
print (y-x)
'''
''''
Вхідний рядок складається лише з цифр. Функція повинна повернути кількість нулів від початку рядка.
'''
a = input("Введіть число: ")
a_int = int(a)
c = len(str(a_int))
x = len(a)
print(x - c)


