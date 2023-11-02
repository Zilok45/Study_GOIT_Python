''''
num = int(input("Enter the integer (0 to 100): "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i += 1
print(sum)
'''
'''
Рядок — це об'єкт, що ітерується, а, значить, ми можемо використовувати його в циклі for
Підрахуйте в заданому рядку message кількість входжень символу зі змінної search
Результат помістіть у змінну result.
'''
'''''
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for i in message:
    if i == search:
        result = result + 1
print(result)

'''
'''''
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
if first and second < 0:
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))
gcd = 0
if first > second:
    gcd = second
else:
    gcd = first
while first % gcd !=0 or second % gcd !=0:
    gcd -=1
print(first)
print(second)
'''
'''''
Напишіть два цикли, вкладені один в один. У першому циклі while ми постійно запитуємо ціле число,
а у другому з допомогою циклу for складаємо суму чисел від 0 до введеного числа включно і додаємо до змінної sum. 
Змінна sum накопичує суми, що утворюються при кожному введенні числа. 
Вихід з першого циклу здійснюємо, якщо ми ввели число 0.

Тести використовують дві тестові послідовності чисел:

10, 13, 73, 0 і чекають на суму 2847
1, 2, 3, 4, 0 і чекають на суму 20
'''
num = int(input("Enter integer (0 for output): "))
sum = 0
while num >= 0:
    for i in range(num):
        sum += i
        i += 1
    num = int(input("Enter integer (0 for output): "))
print(sum)