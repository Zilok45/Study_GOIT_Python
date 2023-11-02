message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ord("a") <= ord(ch) <= ord("z"):
        pos_small = ord(ch) - ord("a")
        pos_small = (pos_small + offset) % 26
        new_ch = chr(pos_small + ord("a"))
    elif ord("A") <= ord(ch) <= ord("Z"):
        pos_big = ord(ch) - ord("A")
        pos_big = (pos_big + offset) % 26
        new_ch = chr(pos_big + ord("A"))         
    else:
        pos_sym_or_num = ord(ch)
        new_ch = chr(pos_sym_or_num)

    encoded_message += new_ch
print(f"Your encoded message is: {encoded_message}")
    
    
   #різниця між бажаними шифрами:
    
# pos = ord('v') - ord('a')  # 21

    #додаємо зсув і ділимо на ціло на к-сть букв в алфавіті
    
# pos = (pos + 33) % 26  # 2

    #додаємо новий символ
    
# new_char = chr(pos + ord("a"))  # 'c'