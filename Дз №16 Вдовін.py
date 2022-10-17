print("Завдання 1")

def geom_prog(n, q, count):
    degree = 0
    index = 1
    while index < count:
        yield (n * q ** (degree))
        degree += 1

count = int(input("Кількість елементів у послідовності? "))
prog = geom_prog(2, 4, count)

for el in prog:
    if el > 2100:
        prog.close()
    else:
        print(el, end=", ")
print()

print("Завдання 2")
generator = (x + 3 for x in range(20) if x % 2)
for el in generator:
    print(el, end=", ")
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
    print(el, end =", ")
print()

print("Завдання 4")

finish = int(input("До якого числа будемо йти? "))
list_cubes = []
list_el_adder = [list_cubes.append(el ** 3) for el in range(2, finish + 1)]
print(list_cubes)


