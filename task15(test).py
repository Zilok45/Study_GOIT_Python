result = None
operand = None
operator = None
wait_for_number = True
while True:
    user_input = input("Введіть число, оператор (+, -, *, /), або = для завершення: ")
    if user_input == "=":
        break
    if result is None:
        try:
            result = float(user_input)
        except ValueError:
            print("Невірний формат числа. Спробуйте ще раз.")
    else:
        if user_input in ("+", "-", "*", "/"):
            operator = user_input
        else:
            try:
                operand = float(user_input)
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    if operand == 0:
                        print("Ділення на нуль недопустиме. Спробуйте ще раз.")
                        continue
                    result /= operand
                operator = None  # Скидаємо оператор після обчислення
            except ValueError:
                print("Невірний формат числа або оператора. Спробуйте ще раз.")
if result is not None:
    print(f"Результат: {result}")