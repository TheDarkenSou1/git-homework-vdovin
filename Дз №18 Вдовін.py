print("Завдання №1")
class Counter:

    count = 0

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.count


@Counter
def decor_func(a):
    return a * a


n = decor_func(2)
m = decor_func(3)
print(decor_func.count, "\n")

print("Завдання №2")

list_func = []

def function_adder(f):
    def add_func(*arg):
        if f not in list_func:
            list_func.append(f)
        return list_func
    return add_func


@function_adder
def sort_list(list_numbers):
    list_numbers.sort()
    return list_numbers


@function_adder
def square(list_numbers):
    res2 = [el ** 2 for el in list_numbers]
    return res2


@function_adder
def cube(list_numbers):
    res3 = [el ** 3 for el in list_numbers]
    return res3


list_nums = [4, 2, 7, 0, 1, 5, 10, -3]
sort_list(list_nums)
square(list_nums)
cube(list_nums)
print(list_func)
for func in range(len(list_func)):
    print(list_func[func](list_nums))
print()

print("Завдання 3")

def adder_to_file(f):
    def add_string(s):
        name_class = s.__class__.__name__
        file = open(f"{name_class}.txt", "w+")
        file.write(f(s))
        file.close()
        return f(s)
    return add_string


class Text:

    def __init__(self, stroka: str):
        self.stroka = stroka

    @adder_to_file
    def __str__(self):
        return f"{self.stroka}"


text = Text("Hello world!")
print(text, "\n")
#
print("Завдання 4")
import time


def time_tracker(count, file_name):
    def dec_function(f):
        def func_list(num):
            for el in range(count):
                start = time.time()
                f(num)
                end = time.time()
                file = open(f"{file_name}.txt", "a")
                file.write(f"{el + 1} time: {end - start}\n")
                file.close()
            return
        return func_list
    return dec_function


@time_tracker(50, "test_time")
def cube_and_sum(num):
    return sum(i**3 for i in range(num))

print(cube_and_sum(30000))

