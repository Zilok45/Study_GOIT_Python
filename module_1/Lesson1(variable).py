                    # Змінні
                    
# Змінна — це елемент пам'яті, у якого є ім'я і в якому можуть зберігатися данні.

age = 20        # age - назва змінної, 20 -значення
user1_age = 30
user2_age = 30
ADULT_THR = 18
# 67788 = 18 # так називати змінні не можна
# _do_not_use_this = 0 # так називати змінні не можна

# Стосовно іменування змінних у Python є три суворих правила:
    # 1. ім'я змінної у Python може складатися лише з цифр, літер та знаків підкреслення _;
    # 2. ім'я змінної не може починатися з цифри, але може зі знака нижнього підкреслення;
    # 3. використання зарезервованих слів у якості імені змінної буде призводити до помилки.
    
#Перелік зарезервованих слів: False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield  

                                        # Інструкція
                                        
  # Інструкція (statement) — це пов'язаний набір слів і символів з синтаксису мови, які об'єднуються, щоб виразити одну ідею, одну інструкцію для машини. 
  
x = 2
y = x + 10   

                                        #  Вирази Python
                                        
a = 1           #   це вираз
b = 2           #   це вираз
c = a + b + 10  # це вираз

# Виразом називається сукупність змінних, операцій, імен функцій, дужок, який може бути обчислений відповідно до синтаксису Python.

                                        # Оператори та операнди
    
# Оператори та операнди — це частини виразу. Оператори — визначають дію, операнди — те, з чим ця дія буде вчинена.

 # Оператори: + (Додавання), - (Віднімання), * (множення), / (Ділення), % (залишок від ділення), // (Ділення без остачі), ** (піднесення до степеня).
 # Операндами для арифметичних операторів є числа.
 
                                        # Порядок виконання операцій у виразі

# Python виконує операції у виразі у тому ж порядку, в якому виконуються математичні операції. Спочатку виконується вираз у дужках, потім піднесення до степеня, потім множення, потім додавання та віднімання.

x = 8**3 + 4*(2 + 2)

                    # Типи даних
    # Змінні можуть бути різного типу (зберігати інформацію у різноманітних форматах):
    # 1. None — порожнє значення і "жодний" тип даних. - None
    # 2. Числа (Numeric Type) -  int, float, complex
    # 3. Boolean — бульовий (логічний) тип. Є підтипом цілих чисел. - boll
    # 4. Рядки (Text Sequence Type) - str
    
    # Приклади

a = None # Значення None

int_number = 3 # значення int - ціле число (3)
float_number = 3.3 # значення float - з плаваючою крапкою (3.3)
complex_number = 3.3 + 2j # значення сomplex - з комплексним числом (3.3 + 2j)

hello_string = "Hello"  #   Значення рядкове з " "
world_string = 'World!' #   Значення рядкове з ' '

    # Операції над рядками:

s1 = "Hello,"
s2 = " World!"
joined_string = s1 + s2 # Основна операція, яка реалізована для рядків, — це об'єднання рядків (конкатенація) = "Hello World"

# f-рядок — це такий шаблон, який дозволяє зручним чином генерувати рядок, підставляючи результат виконання виразів в потрібне місце у шаблоні.

name = "Oleg"
hello_string = f"Hello, {name}!" # виведе на консоль : "Hello, Oleg!" працює тільки з рядками
    
        # Створення змінних типу bool
    # Є 2 прості способи створити змінну з типом bool:
# 1. Присвоїти змінній значення True або False
a = True
b = False
# 2. Присвоїти змінній результат виконання логічного виразу, наприклад порівняння:
age = 18
adult1 = age >= 18    # True

age = 15
adult2 = age >= 18    # False
    #Вирази порівняння
# Для порівняння у Python є оператори < (менше), <= (менше або дорівнює), > (більше), >= (більше або дорівнює), == (дорівнює), != (не дорівнює).
a = 3
b = 5
c = a < b   # True
d = a > b   # False
a == b      # False
a != b      # True

                # Вбудовані функції
                
print("Hello World!!!") # - виведе на консоль Hello World!!!
# Функція print() приймає довільну кількість аргументів і все намагається перетворити в рядок і вивести в консоль
# print() зручно використовувати, щоб дізнатися вміст тієї або іншої змінної у міру виконання інструкцій.
  
                #Введення даних

# Для введення даних з консолі використовується функція input Значення аргументу функції (рядок) буде виводитися в консоль, а далі — буде активовано спеціальний курсор, який означає, що програма чекає введення даних.
a = input("Рядок запрошення: ") # Змінна a отримає те значення, яке ввів користувач.
# На екрані ви побачите: Рядок запрошення: 
#  Інтерпретатор буде чекати до тих пір, доки не зустріне символ нового рядка (Enter). Після цього весь введений з клавіатури текст буде повернений як результат роботи функції input.

            # Приведення типів
            
# Oдна й та сама змінна може змінювати свій тип у міру виконання нових інструкцій, але автоматично інтерпретатор не змінюватиме тип даних.
            
age = input("How old are you? ") # Функція input повертає str — рядок, та порівняти значення age з числом 18 — не можна, бо незрозуміло, яким чином повинно відбуватися таке порівняння.

# можна перетворити тип змінної age у int за допомогою вбудованої функції int (функція називається так само, як і тип):
age = input("How old are you? ")
age = int(age)
#Для перетворення рядків в числа з дробовою частиною можна використати функцію float:
pi = float('3.14')
#Також можна перетворити практично будь-який Python об'єкт в рядок функцією str:
pi_str = str(3.14)
age_str = str(29)