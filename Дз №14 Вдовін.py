import math

# print("Завдання 1")
#
# class Rectangle:
#
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     def square_rectangle(self):
#         square = self.height * self.width
#         return square
#
#     def __gt__(self, other):
#         return self.square_rectangle() > other.square_rectangle()
#
#     def __add__(self, other):
#         new_rect = self.square_rectangle() + other.square_rectangle()
#         return new_rect
#
#     def __mul__(self, other):
#         return self.square_rectangle() * other
#
#     def __str__(self):
#         return f"Висота прямокутника: {self.height}, ширина прямокутника: {self.width}"
#
#
# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(3, 4)
# print(rect1)
# print(rect2)
# print("Площа 1-го прямокутника: ", rect1.square_rectangle())
# print("Площа 2-го прямокутника: ", rect2.square_rectangle())
# print("Порівняння:", rect1 > rect2)
# print("Складання двох площин прямокутників:", rect1 + rect2)
# print("Множення площі прямокутника на задане число:", rect1 * 3)

print("Завдання 2")

class ProperFraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __add__(self, other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator + other.numerator
            if new_numerator > self.denominator and new_numerator % self.denominator:
                real_num = new_numerator // self.denominator
                return f"  {new_numerator % self.denominator}\n{real_num} ---\n   {self.denominator}"
            elif new_numerator > self.denominator and not new_numerator % self.denominator:
                real_num = new_numerator // self.denominator
                return f"  {real_num}"
            else:
                return f"{new_numerator}\n---\n {self.denominator}"
        else:
            new_denominator = (self.denominator * other.denominator) // (math.gcd(self.denominator, other.denominator))
            if self.denominator != new_denominator and other.denominator != new_denominator:
                self.numerator = self.numerator * other.denominator
                other.numerator = other.numerator * self.denominator
                self.denominator = self.denominator * (new_denominator // self.denominator)
                other.denominator = other.denominator * (new_denominator // other.denominator)
                new_numerator = self.numerator + other.numerator
                if new_numerator > self.denominator and new_numerator % self.denominator:
                    real_num = new_numerator // self.denominator
                    return f"  {new_numerator % self.denominator}\n{real_num} ---\n   {self.denominator}"
                elif new_numerator > self.denominator and not new_numerator % self.denominator:
                    real_num = new_numerator // self.denominator
                    return f"  {real_num}"
                else:
                    return f"{new_numerator}\n---\n {self.denominator}"


    def __sub__(self, other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator - other.numerator
            if new_numerator > self.denominator and new_numerator % self.denominator:
                real_num = new_numerator // self.denominator
                return f"  {new_numerator % self.denominator}\n{real_num} ---\n   {self.denominator}"
            elif new_numerator >= self.denominator and not new_numerator % self.denominator:
                real_num = new_numerator // self.denominator
                return f"  {real_num}"
            else:
                return f"{new_numerator}\n---\n {self.denominator}"
        else:
            new_denominator = (self.denominator * other.denominator) // (math.gcd(self.denominator, other.denominator))
            if self.denominator != new_denominator and other.denominator != new_denominator:
                self.numerator = self.numerator * (new_denominator // self.denominator)
                other.numerator = other.numerator * (new_denominator // other.denominator)
                new_numerator = self.numerator + other.numerator
                if new_numerator > self.denominator and new_numerator % self.denominator:
                    real_num = new_numerator // self.denominator
                    return f"  {new_numerator % self.denominator}\n{real_num} ---\n   {self.denominator}"
                elif new_numerator >= self.denominator and not new_numerator % self.denominator:
                    real_num = new_numerator // self.denominator
                    return f"  {real_num}"
                else:
                    return f"{new_numerator}\n---\n {self.denominator}"

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        if new_numerator > new_denominator and new_numerator % new_denominator:
            real_num = new_numerator // new_denominator
            return f"  {new_numerator % new_denominator}\n{real_num} ---\n   {new_denominator}"
        elif new_numerator >= new_denominator and not new_numerator % new_denominator:
            real_num = new_numerator // new_denominator
            return f"  {real_num}"
        else:
            return f"{new_numerator}\n---\n {new_denominator}"


    def __str__(self):
        if self.numerator > self.denominator:
            real_num = self.numerator // self.denominator
            return f"  {self.numerator}\n{real_num} ---\n   {self.denominator}"
        elif self.numerator == self.denominator:
            real_num = self.numerator // self.denominator
            return f"  {real_num}"
        else:
            return f"{self.numerator}\n---\n {self.denominator}"




drob1 = ProperFraction(5, 3)
drob2 = ProperFraction(2, 3)
print("Перший дріб:\n", drob1)
print("Другий дріб:\n", drob2)
print("Сума:\n", drob1 + drob2, "\n")
print("Різниця:\n", drob1 - drob2, "\n")
print("Добуток:\n", drob1 * drob2, "\n")
