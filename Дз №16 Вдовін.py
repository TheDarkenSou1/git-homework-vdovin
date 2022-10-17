print("Завдання 1")

def geom_prog(n, q, count):
    degree = 0
    index = 0
    while index < count:
        yield (n * q ** (degree))
        degree += 1
        index += 1

count = int(input("Кількість елементів у послідовності? "))
prog = geom_prog(2, 4, count)

for el in prog:
    if el > 2100:
        prog.close()
    print(el, end=" ")
print("\n")

print("Завдання 2")
def _range(*args):
    start, stop, step = 0, None, 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError()

    if step > 0 and (step < start):
        raise ValueError()
    if step < 0 and (stop > start):
        raise ValueError()
    if step == 0:
        raise ValueError()

    while abs(start) < abs(stop):
        yield (start + 3)
        start += step

print(*_range(1, 20))
print()

print("Завдання 3")

def prime_generator(x):
    n = 2
    for i in range(n, x):
        for j in range(n, i):
            if not i % j:
                break
        else:
            yield i

a = prime_generator(20)
for el in a:
    print(el, end =" ")
print("\n")

print("Завдання 4")

finish = int(input("До якого числа будемо йти? "))
list_cubes = []
list_el_adder = [list_cubes.append(el ** 3) for el in range(2, finish + 1)]
print(list_cubes)


