# print("Завдання 1")
# list1 = [1, -5, 20, 100, -60]
# def func(n):
#     return max(n)
#
# print("Максимальне число у списку:", func(list1))
#
# print("Завдання 2")
# def func2(x1, x2, x_str):
#     res = x_str + str(x1 + x2)
#     return res
#
# x1 = int(input("Введіть 1 число: "))
# x2 = int(input("Введіть 2 число: "))
# x_str = input("Введіть рядок: ")
# print("Конкатенація рядка та суми 2 чисел:", func2(x1, x2, x_str))
#
# print("Завдання 3")
# def rectangle(h, w):
#     for i in range(1, h + 1):
#         for m in range(1, w + 1):
#             if i == 1 or i == h:
#                 print("*", end=" ")
#             elif m == 1 or m == w:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
#     print()
# h = int(input("Введіть висоту прямокутника: "))
# w = int(input("Введіть ширину прямокутника: "))
# rectangle(h, w)
#
# print("Завдання 4")
# def linear_search(list_el, number):
#     for i in range(len(list_el)):
#         if list_el[i] == number:
#             print("Індекс елементу у списку:", i, "\n")
#             return i
#     return print(-1)
#
# num = int(input("Скільки буде елементів у списку? "))
# list_el = []
# for i in range(num):
#     el = int(input("Введіть елемент списку: "))
#     list_el.append(el)
# number = int(input("Яке число будемо шукати? "))
#
# linear_search(list_el, number)
#
# print("Завдання 5")
# def func3(string1):
#     string2 = string1.split()
#     return print("Кількість слів у рядку:", len(string2))
#
# string1 = input("Введіть рядок: ")
# func3(string1)

print("~ ДОДАТКОВЕ ДЗ ~")
print("Завдання 1")
import math
def arifm_seq(seq):
    d = seq[1] - seq[0]
    if seq[0] + d == seq[1] and seq[1] + d == seq[2]:
        seq.append(seq[len(seq) - 1] + d)
        return seq

def geom_seq(seq):
    div = seq[1] // seq[0]
    if seq[0] * div == seq[1] and seq[1] * div == seq[2]:
        seq.append(seq[len(seq) - 1] * div)
        return seq

def degree_sq_seq(seq):
    if (pow(seq[0], 1 / 2) + 1) ** 2 == seq[1] and (pow(seq[1], 1 / 2) + 1) ** 2 == seq[2]:
        seq.append((len(seq) + 1) ** 2)
        return seq

def degree_cube_seq(seq):
    if (pow(seq[0], 1 / 3) + 1) ** 3 == seq[1] and (pow(seq[1], 1 / 3) + 1) ** 3 == seq[2]:
        seq.append((len(seq) + 1) ** 3)
        return seq

num_seq = input("Введіть всі елементи послідовності через пробіл: ")
seq = (num_seq.split())
seq = list(map(int, seq))

if arifm_seq(seq):
    print("Наступний елемент послідовності:", seq[len(seq) - 1])
elif geom_seq(seq):
    print("Наступний елемент послідовності:", seq[len(seq) - 1])
elif degree_sq_seq(seq):
    print("Наступний елемент послідовності:", seq[len(seq) - 1])
elif degree_cube_seq(seq):
    print("Наступний елемент послідовності:", seq[len(seq) - 1])
else:
    print("Помилка! Неможливо визначити послідовність.")
