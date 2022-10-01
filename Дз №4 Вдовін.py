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
M1 = list(number)
M2 = list(number)[::-1]
if M1 == M2:
    print("Число - паліндром")
else:
    print("Число - не паліндром")
print("Завдання 3")
X = int(input("Введіть координати X: "))
Y = int(input("Введіть координати Y: "))
r = 4
r_XY = math.sqrt(X ** 2 + Y ** 2)
if r_XY <= r:
    print("Точка належить колу.")
else:
    print("Точка не належить колу.")
