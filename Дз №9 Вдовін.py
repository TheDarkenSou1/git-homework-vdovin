print("Завдання 1")
list1 = [1, -5, 20, 100, -60]

def func(n):
    print("Максимальне число у списку:", max(n), "\n")

func(list1)

print("Завдання 2")
def func2():
    x1 = int(input("Введіть 1 число: "))
    x2 = int(input("Введіть 2 число: "))
    x_str = input("Введіть рядок: ")
    res = x_str + str(x1 + x2)
    return res

print("Конкатенація рядка та суми 2 чисел:", func2())

print("Завдання 3")
def rectangle():
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
rectangle()

print("Завдання 4")
def linear_search(list_el, number):
    for i in range(len(list_el)):
        if list_el[i] == number:
            print("Індекс елементу у списку:", i, "\n")
            return i
    return print(-1)

num = int(input("Скільки буде елементів у списку? "))
list_el = []
for i in range(num):
    el = int(input("Введіть елемент списку: "))
    list_el.append(el)
number = int(input("Яке число будемо шукати? "))

linear_search(list_el, number)

print("Завдання 5")
def func3():
    string1 = input("Введіть рядок: ")
    string2 = string1.split()
    return print("Кількість слів у рядку:", len(string2))
func3()

