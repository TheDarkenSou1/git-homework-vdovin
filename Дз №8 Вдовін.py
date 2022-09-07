print("Завдання 1")
str1 = input("Введіть перший рядок: ")
str2 = input("Введіть другий рядок: ")
str1_1, str2_2 = set(str1), set(str2)
print("Букви, які є в обох словах:", str1_1 & str2_2, "\n")

print("Завдання 2")
def func(n):
    i_list = []
    for i in range(0, 51, n):
        if not (i % n):
            i_list.append(i)
            if len(i_list) == 11:
                break
    return i_list
list1 = func(3)
list2 = func(5)
list3 = set(list1) & set(list2)
print("Числа, які є в обох списках:", list3)