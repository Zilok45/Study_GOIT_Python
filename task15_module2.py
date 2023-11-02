print("Вас Вітає калькулятор Python")
while True:
    try:
        operand = int(input("Введіть число для обчислення: "))
        break
    except ValueError:
        print("Ви ввели не число, спробуйте ще раз")
        continue     
result = operand
operator = None
wait_for_number = True

while True:
    while wait_for_number:
        user_operator = input("Введіть символ (+, -, *, /  - для обчислення або = для Відповіді):  ")
        if user_operator not in ("+", "-", "*", "/", "="):
            print("Неправильний оператор, спробуйте ще раз")
            continue
        operator = user_operator
        break
    if operator == "=":
        print(f"Ваш результат обчислень: {result}")
        break
    while wait_for_number:
        try:
            user_input = float(input("Введіть число для обчислення: "))
            operand = user_input
        except ValueError:
            print("Ви ввели не число, спробуйте ще раз")
        else:
            break
    if operator == "+":
            result = result + operand
    elif operator == "-":
            result = result - operand
    elif operator == "*":
            result = result * operand
    elif operator == "/":
        if operand == 0:
            print("Помилка: Ділення на нуль!")
            continue
        else:
            result = result / operand
    