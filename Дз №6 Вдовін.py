print("Завдання 1")
text = input("Enter text: ")
print("Number of letters 'b':", text.count("b"))
print()

print("Завдання 2")
while True:
    name = input("Введіть ваше ім'я: ")
    if name.isalpha():
        print("Ваше ім'я:", name.title())
        break
    else:
        print("Ім'я введено некоректно.", end=" ")
print()

print("Завдання 3")
res = sum(map(ord, input("Введіть рядок: ")))
print("Сума всіх кодів символів у рядку:", res)

print("Завдання 4")
import math
n = 3
for m in range(10):
    print("Число Pi: {pi:.{l}}".format(pi = math.pi, l = n))
    n += 1
print()

print("Завдання 5")
string2 = input("Введіть рядок: ")
string3 = string2.split()
print("Найдовше слово у рядку:", max(string3, key=len), "-->", len(max(string3, key=len)), "букв.\n")

print("~ ДОДАТКОВЕ ДЗ ~")
print("Завдання 1")
string4 = input("Введіть рядок: ")
string5 = ""
for q in string4:
    if q not in string5:
        string5 += q
    else:
        print(string4, "- Вовочка писав слово - '{}'\n".format(string5))
        break

print("Завдання 2")
import re
HTML_code = '''\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Пример веб-страницы</title>
 </head>
 <body>
  <h1>Заголовок</h1>
  <!-- Комментарий -->
  <p>Первый абзац.</p>
  <p>Второй абзац.</p>
 </body>
</html>
'''
print(re.sub(r'<.*?>', '', HTML_code))