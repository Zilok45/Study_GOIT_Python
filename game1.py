from random import randint

SIZE_WIDTH = int(input("Введіть довжину поля: "))
SIZE_HEIGHT = int(input("Введіть ширину поля: "))

char_x = randint(1, SIZE_WIDTH - 1)
char_y = randint(1, SIZE_HEIGHT - 1)

exit_x = randint(0, SIZE_WIDTH - 1)
exit_y = randint(0, SIZE_HEIGHT - 1)

while True:
    
    game_map = ""
    
    for j in range(SIZE_HEIGHT):
        
        row = " |"
        
        for i in range(SIZE_WIDTH):
            
            if char_x == i and char_y == j:
            
                row += "X|"
            
            elif exit_x == i and exit_y == j:
                
                row += "О|"
            
            else:
                
                row += " |"
            
        game_map += f"{row}\n"
        
    print(game_map)
    
    if char_x == exit_x and char_y == exit_y:
        
        print("level complited, You Won!!!")
        break
    
    direction = input("Enter direction (w(up) / s(down) / a(left) /d(right)) : ")
    
    if direction == "w" and char_y > 0:
        
        char_y -= 1
    
    elif direction == "s" and char_y < SIZE_HEIGHT - 1:
        
        char_y += 1
    
    elif direction == "a" and char_x > 0:
        
        char_x -= 1
    
    elif direction == "d" and char_x < SIZE_WIDTH - 1:
        
        char_x += 1
        
