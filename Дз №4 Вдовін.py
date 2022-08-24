import math
print("Завдання 1")
num = input("Введіть номер квитка: ")
while True:
    N = list(map(int, num))
    if len(N) % 2:
        print("Номер квитка має містити однакову\n"
              "кількість цифр з кожної сторони!\n")
        num = input("Введіть номер квитка ще раз: ")
    else:
        i = int(len(N) / 2)
        N1 = N[0:i]
        N2 = N[-i:]
        if sum(N1) == sum(N2):
            print("Ваш квиток щасливий!\n")
        else:
            print("Ваш квиток нещасливий. Пощастить наступного разу!\n")
        break
print("Завдання 2")
number = input("Введіть число: ")
M = list(map(int, number))
a = 0
b = -1
is_palindrome = True
for i in M:
    if M[a] == M[b]:
        a += 1
        b -= 1
        continue
    else:
        is_palindrome = False
if is_palindrome == True:
    print("Ваше число - паліндром.\n")
else:
    print("Ваше число - не паліндромом.\n")
print("Завдання 3")
X = int(input("Введіть координати X: "))
Y = int(input("Введіть координати Y: "))
r = 4
r_XY = math.sqrt(X ** 2 + Y ** 2)
if r_XY <= r:
    print("Точка належить колу.")
else:
    print("Точка не належить колу.")