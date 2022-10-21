print("Завдання №1")
def cubes(num):
    return num + num

def gen_items(start, number, func):
    i = 0
    while i < number:
        yield start
        start = func(start)
        i += 1

for i in gen_items(1, 10, cubes):
    print(i)

print("\nЗавдання №2\n")
import timeit

var_1 = """
def fibonachi1():
    first_num = 1
    second_num = 1

    def get_num():
        nonlocal first_num
        nonlocal second_num
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num
        return next_num
    return get_num

get_n1 = fibonachi1()
for i in range(5):
    print(get_n1(), end=" ")
print()
"""

print(timeit.timeit(var_1, number=3))

var_2 = """
def fibonachi2():
    buf = [2, 3]

    def get_num(num):
        if len(buf) > num:
            return buf[num]

        first_num, second_num = buf[-2], buf[-1]

        for i in range(len(buf) - 1, num):
            next_num = first_num + second_num
            buf.append(next_num)
            first_num = second_num
            second_num = next_num
        return buf[-1]
    return get_num

get_n2 = fibonachi2()

for i in range(5):
    print(get_n2(i), end=" ")
print()
"""
print(timeit.timeit(var_1, number=3))

print("\nЗавдання 3")

def func(list1):
    list2 = []
    for el in range(len(list1)):
        list2.append(list1[el] ** 2)
    def summa():
        res = sum(list2)
        return res
    return summa

list1 = [2, 5, 1, 7, -3, 6, 12]

f = func(list1)
print("Сума отриманого переліку чисел: ", f())
