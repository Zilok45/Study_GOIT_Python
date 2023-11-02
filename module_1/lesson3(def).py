    # Створення та виклик функцій

def say_hello():
    print('Привіт, Світ!')   # блок, що належить функції
    # Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()

    # Аргументи функції
    
def print_max(a, b):    # a і b - параметри
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

        # Повернення результату
        
# Для повернення значення з функції необхідно вказати, що повернути після ключового слова 
# return. Наприклад, функція, що виконує операцію додавання.

def plus(a, b):
  c = a + b
  return c

res = plus(3, 4)
print(res)  # Виведе 7

# Або ще коротше:

def plus(a, b):
  return a + b

print(plus(3, 4))   # Виведе 7

        # Локальні змінні
        
x = 50

def func():
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('x як і раніше', x)   # x як і раніше 50

        # Global
        
x = 50

def func():
    global x
    print('x дорівнює', x) # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)   # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)   # Значення x складає 2

        # Ключові аргументи
        
def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

func(3, 7)          # a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(25, c=24)      # a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(c=50, a=100)   # a дорівнює 100, b дорівнює 5, а c дорівнює 50

def say(message, times=1):
    print(message * times)

say('Привіт')   # Привіт
say('Світ', 5)   # СвітСвітСвітСвітСвіт

        #       Змінна кількість параметрів
        
def total(a=5, *numbers, **phone_book):
    print('a', a)
    # прохід по всіх елементах кортежу
    for single_item in numbers:
        print('single_item', single_item)

    #прохід по всіх елементах словника
    for first_part, second_part in phone_book.items():
        print(first_part,second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

"""

В результаті в консолі ми побачимо:

a 10
single_item 1
single_item 2
single_item 3
Jack 1123
John 2231
Inge 1560
None

Коли ми оголошуємо параметр із зірочкою (наприклад, *numbers),
всі позиційні аргументи, починаючи з цієї позиції до кінця, будуть зібрані в кортеж під ім'ям numbers. 
Аналогічно, коли ми оголошуємо параметри із двома зірочками (**phone_book), 
всі ключові аргументи, починаючи з цієї позиції до кінця, будуть зібрані в словник під ім'ям phone_book.

"""  
            # Контейнери для зберігання аргументів функцій
        # Кортежі
'''
    Кортежі у Python — це впорядковані незмінні множини елементів.
    Елементом кортежу може бути будь-який тип даних.
    Кортежі не можна змінювати, не можна додавати/видаляти/переставляти елементи.
    
    Щоб створити порожній кортеж, існують два способи, хоча і не зовсім зрозуміло навіщо потрібний порожній кортеж :-)
'''
my_tuple = tuple()
another_tuple = ()

    # Створення ж непорожніх кортежів відбувається наступним чином:
not_empty = (1, 2, 3)
    # Доступ до елементів кортежу відбувається за індексом за допомогою синтаксису квадратних дужок:
not_empty = (2, 4, 6)
not_empty[0]    # 2
not_empty[1]    # 4
not_empty[2]    # 6
"""
    Індексом слугує суворо ціле число. Індексація починається з 0.
    Ще з кортежами вміє працювати цикл for та може одразу перебрати усі елементи кортежу, як в прикладі з total.
 """
        # Словники:
'''
    Словник — це контейнер, який зберігає пари ключ-значення.
    Ключем може бути будь-який незмінний тип даних Python (число, рядок, кортеж тощо).
    Значенням словника може бути будь-який тип даних Python, включаючи призначені для користувача типи.
'''
    
    # Порожній словник можна створити одним з двох способів:
empty_dict = {}
another_empty_dict = dict()
    # Створити непорожній словник можна наступним чином::
some_dict = {
    "key": "value",
    1: "one",
    }
# Запис пари ключ-значення у вже існуючий словник відбувається за допомогою квадратних дужок і оператора присвоєння = :
not_empty = {"key": "value"}
not_empty["new_key"] = "new value"
print(not_empty)    # {"key": "value", "new_key": "new value"}

                # Рекурсія
'''
Рекурсивна функція — це функція, що визначається в термінах самої себе і здатна викликати саму себе.
Це означає, що функція викликатиме себе і повторюватиме свою поведінку до тих пір,
доки не буде виконана деяка умова для повернення результату.
'''
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)    # 120