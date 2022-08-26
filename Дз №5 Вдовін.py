print("Завдання 1")
[print(i, end = " ") for i in range(1, 101) if not i % 7]
print()

print("Завдання 2")
n = int(input("Введіть число n (4 < n < 16): "))
i = n
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("Факторіал числа", i, "=", factorial)
print()

print("Завдання 3")
m = 5
print("Таблиця множення на 5:")
for i in range(1, 11):
    print(i, "*", m, "=", m * i)
print()

print("Завдання 4")
h = int(input("Введіть висоту прямокутника: "))
w = int(input("Введіть ширину прямокутника: "))
for i in range(1, h + 1):
    for m in range(1, w + 1):
        if i == 1 or i == h:
            print("*", end=" ")
        elif m == 1 or m == w:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

print("Завдання 5")
list = [0, 5, 2, 4, 7, 1, 3, 19]
count = 0
for el in list:
    if el % 2:
        count += 1
print("Кількість непарних чисел у списку:", count)
print()

print("Завдання 6")
from random import randint
list1 = [randint(1, 20) for i in range(4)]
list2 = list1[:]
for i in list1:
    list2.append(i * 2)
print("Перший список:", list1)
print("Другий список:", list2, "\n")

print("Завдання 7")
salary = [randint(7500, 15000) for i in range(12)]
print("Середня зарплатня робітника: ", round(sum(salary)/len(salary), 2), "\n")

print("Завдання 8")
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Матриця 4х4:")
summ = 0
for el in matrix:
    for i in el:
        summ += i
        if i < 10:
            print(i, end="  ")
        else:
            print(i, end=" ")
    print()
print("Сума елементів матриці:", summ)

print("~ ДОДАТКОВЕ ДЗ ~")
print("Завдання 1")
prime_list = []
n = 2
for i in range(2, 101):
    for j in range(2, i):
        if not i % j:
            break
    else:
        prime_list.append(i)
print(prime_list, "\n")

print("Завдання 2")
a = int(input("Введіть ширину пісочного годинника (число непарне): "))
for i in range(a, 0, -1):
    if i % 2:
        n = (a - i) // 2
        print(" " * n, end="")
        for m in range(i):
            print("*", end="")
    else:
        continue
    print()
for i in range(1, a + 1):
    if i % 2 and i != 1:
        n = (a - i) // 2
        print(" " * n, end="")
        for m in range(i):
            print("*", end="")
    else:
        continue
    print()
print()

print("Завдання 3")
initial_list = [1, 2, 3, 7, 111]
print("Початкова версія списку:", initial_list)
initial_list.reverse()
print("Реверс початкового списку:",initial_list)
