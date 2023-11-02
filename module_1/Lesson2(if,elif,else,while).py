                                    # Керуючі конструкції. Винятки
name = input("What is your name? ")
print(f"Hello {name}")
# За замовчуванням у Python інструкції виконуються одна за одною зверху вниз. У прикладі дві інструкції — спочатку виконується name = input("What is your name? "), потім print(f"Hello {name}").
    
    #У Python існує три способи управління потоком виконання:
    
        # 1. умовне виконання — виконання блоку інструкцій тільки при настанні деякої умови;
        # 2. цикли — повторення виконання блоку інструкцій, доки виконується деяка умова;
        # 3. винятки — виконання блоку інструкцій у разі помилки.

                            # Умовне виконання:

age = input("How old are you? ")

if int(age) >= 18:
    print("You are adult already.")
else:
    print("You are infant yet.")
    
    # У Python реалізований оператор контролю виконання (умовний оператор) if ... elif ... else.
    # Оператор контролю виконання дозволяє виконувати блоки інструкцій не завжди, а тільки тоді, коли буде виконана умова.

    # Синтаксис умовного оператора:
        # 1. починається з ключового слова if, за яким йде умова;
        # 2. після умови ставиться двокрапка і з нового рядка з відступом йде блок інструкцій, які будуть виконані, якщо умова виконується;
        # 3. після блоку if може бути нуль або більше блоків elif, інтерпретатор послідовно перевірятиме усі умови elif зверху вниз, доки не знайде той, який виконується;
        # 4. потім може бути один блок else, який виконується, якщо всі попередні умови не виконуються.
                # Умовне виконання
a = input("enter number")
a = int(a)
if a > 0:
    print("Number add")
elif a < 0:
    print("number has minus variable")
else:
    print("your number is zero")
                    #Умови у Python

# Умовний оператор if ... elif ... else у Python у якості умов може приймати змінні типу bool або будь-який вираз, який він виконає і результат перетворить в bool.

                    # Логічні вирази
    # у Python є механізм неявного приведення будь-якого типу до типу bool. Правила приведення до bool — інтуїтивні:
    
    # 1. число 0 приводиться до False (ціле, дробове або комплексне);
money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts") 
    # 2. None приводиться до False;
result = None
if result:
    print(result)
else:
    print("Result is None, do something")  
    # 3. порожній контейнер (порожній рядок тощо) приводиться до False     
user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!") 
    # 4. все інше приводиться до True
                            # Булева алгебра
name = "Taras"
age = 22
has_driver_licence = True

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")
    # У Python оператори булевої алгебри — це оператори not, and, or.
        #  and (І) вираз виконується, якщо обидві умови виконуються
a = True and False  # False  
        # or (АБО) вираз виконується, якщо хоча б одна з умов виконується
a = True or False  # True
        # not (НІ) заперечення, вираз виконується, якщо операнд — неправда
a = not 2 < 0  # True  

                            # Тернарні операції
    # Тернарні оператори — це ті самі умовні вирази, але в скороченій формі. Ці оператори повертають щось, залежно від того, чи є умова істиною або брехнею.
is_nice = True
state = "nice" if is_nice else "not nice" # У цьому прикладі у state буде рядок 'nice'
    # У Python також існує коротший варіант тернарного оператора.
some_data = None
msg = some_data or "Не було повернено даних"
#У цьому прикладі msg містить рядок 'Не було повернено даних', це зручно, коли потрібно швидко перевірити значення та показати повідомлення, якщо значення None.
                            # Блоки інструкцій
x = int(input("X: "))
y = int(input("Y: "))

if x == 0:     # У Python рекомендується для виділення одного рівня вкладеності для блоку інструкцій використовувати 4 пробіли.
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x

# В цьому прикладі тричі повторюється перевірка на нерівність x нулю, і на кожну перевірку блок інструкцій виділяється додатковими 4-ма пробілами.
x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

    if x == 0:
        print("X can`t be equal to zero")
        x = int(input("X: "))

        if x == 0:
            print("X can`t be equal to zero")
            x = int(input("X: "))

result = y / x
# Приклад вкладеності для визначення чвертей для координатної площини.
if x >= 0:
    if y >= 0:               # x > 0, y > 0
        print("Перша чверть")
    else:                    # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:               # x < 0, y > 0
        print("Друга чверть")
    else:                    # x < 0, y < 0
        print("Третя чверть")

