print("Завдання 1")
num1 = int(input("Введіть 1 число: "))
num2 = int(input("Введіть 2 число: "))
num3 = int(input("Введіть 3 число: "))
num4 = int(input("Введіть 4 число: "))
if num1 > num2 and num1 > num3 and num1 > num4:
    print("Найбільше число:", num1, "\n")
elif num2 > num3 and num2 > num4:
    print("Найбільше число:", num2, "\n")
elif num3 > num4:
    print("Найбільше число:", num3, "\n")
else:
    print("Найбільше число:", num4, "\n")

print("Завдання 2")
num_ap = int(input("Введіть номер квартири: "))
if num_ap > 36:
    print("Квартири з номером", num_ap, "немає у цьому домі.")
else:
    level = (num_ap - 1) // 4 + 1
    pod = (num_ap - 1) % 4 + 1
    print("Ваша квартира знаходиться у", pod, "під'їзді на", level, "поверсі.\n")

print("Завдання 3")
year = int(input("Введіть рік: "))
if not year % 4 and year % 100 or not year % 400:
    print(year, "- високосний рік!\n")
else:
    print(year, "- невисокосний рік.\n")

print("Завдання 4")
a = int(input("Введіть 1 сторону трикутника: "))
b = int(input("Введіть 1 сторону трикутника: "))
c = int(input("Введіть 1 сторону трикутника: "))
if a + b < c or a + c < b or c + b < a:
    print("Такого трикутника не існує!")
else:
    print("Такий трикутник існує!")
