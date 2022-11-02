import re

print("Завдання №1\n")
text = input("Введіть текст: ")
pattern1 = r'Rb+r'
match1 = re.findall(pattern1, text)


def poisk(match1):
    if match1:
        print("Такий паттерн знайшовся", match1, "\n")
    else:
        print("Такого немає\n")


poisk(match1)

print("\nЗавдання №2\n")
card_num = input("Введіть номер картки: ")
pattern2 = r'^\d{4}(-|\s)\d{4}(-|\s)\d{4}(-|\s)\d{4}$'
match2 = re.fullmatch(pattern2, card_num)


def validatsia(match2):
    if match2:
        print("Номер карти введено коректно:", match2, "\n")
    else:
        print("Помилка. Неправильно введено номер картки!\n")


validatsia(match2)


print("\nЗавдання №3\n")

mail = input("Введіть вашу пошту: ")
pattern3 = r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'
match3 = re.compile(pattern3)


def check_mail(match3, mail):
    if match3.findall(mail):
        print("Пошта введена коректно", "\n")
    else:
        print("Помилка\n")


check_mail(match3, mail)

print("\nЗавдання №4\n")

login = input("Введіть логін: ")
pattern4 = r'(^\w{2,10}$)'
match4 = re.fullmatch(pattern4, login)


def check_login(match4):
    if match4:
        print("Логін записано правильно.")
    else:
        print("Логін некоректний!")


check_login(match4)
