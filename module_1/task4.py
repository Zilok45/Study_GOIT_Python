# банкомат - чи правильно введений пін-код

# з циклом While:

correct_pincode = "3373"
n = 0
max_tries = 3

while n < 3:
    
    user_pincode = input("Введіть свій пін-код: ")
    
    if len(user_pincode) == 4 or len(user_pincode) == 6:
        
        if correct_pincode == user_pincode:
            
            print ("Пін - код вірний")
            user_cash = int(input("Скільки готівки бажаєте зняти?: "))
            
            if user_cash > 0:
                
                print(f"Візміть свої {user_cash} Гривень.")
                break
            
            else:
                
                print(f"ви не можете {user_cash} гривень")
                       
        else:
            
            print("Пін-код не вірний")
            print(f"У вас залишилось {max_tries - n - 1} спроби")
            n += 1
            
    else:
        
        print("Пін-код має скаладатися із 4 цифр або 6 цифр")
        
print("До зустрічі!!!")

'''
# З циклом for:

correct_pincode = "3373"
for i in range(3):
    user_pincode = input("Введіть свій пін-код: ")
    if len(user_pincode) == 4 or len(user_pincode) == 6:
        if correct_pincode == user_pincode:
            print ("Пін - код вірний")
            break
        else:
            print("Пін-код не вірний")
    else:
        print("Пін-код має скаладатися із 4 цифр або 6 цифр")
print("До зустрічі!!!")
 '''   
