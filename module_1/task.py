is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")
is_active = True
is_admin = True
is_permission = True

if is_admin == True:
    access = True
elif is_active == True and is_permission == True:
    access = True
else: 
    access = False