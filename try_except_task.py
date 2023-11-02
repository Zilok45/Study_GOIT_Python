pool = 1000
while True:
    
    try:
        
        quantity = int(input("Enter the number of mailings: "))
        chunk = pool // quantity
        print(f"Вам потрібно зробити {chunk} розсилок")
        break
    
    except ValueError:
        print("Ви ввели текст замість числа")
        
    except ZeroDivisionError:
        print('Divide by zero completed!')
        
    finally:
        print("-" * 30)