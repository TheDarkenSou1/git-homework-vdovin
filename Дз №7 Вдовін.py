print("Завдання 1")
week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
num = int(input("Введіть номер дня тижня: "))
print(num, "-", week.get(num, "Нема такого номера дня тижня"))
print()

print("Завдання 2")
cat_description = {"name": "Tom", "age": 2, "color": "grey",
                   "breed": "british shorthair cat",
                   "cat character": "not as friendly as we expected"}
for desc in cat_description:
    print(desc, ":", cat_description.get(desc))

text = input("Введіть рядок: ")
text_list = list(text.replace(" ", ""))
slovar = {}
for letter in text_list:
    if not slovar.get(letter):
        slovar[letter] = text .count(letter)
        print(letter, '-', slovar[letter])
print()

print("~ ДОДАТКОВе ДЗ ~")
print("Завдання1")
from num2words import num2words
money = input("How much money do you have? \n")
money = money.split(",")
print("You have:", num2words(money[0]), "dollars and", num2words(money[1]), "cents.")
print()

print("Завдання 2")
def conversion(n):
    n2 = n
    result = ''
    for arabic_num, roman_num in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1), 'M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I'.split(", ")):
        result += n // arabic_num * roman_num
        n %= arabic_num
    print(n2, "-->", result)
    return result
arab_num = int(input("Введіть ціле число: "))
conversion(arab_num)