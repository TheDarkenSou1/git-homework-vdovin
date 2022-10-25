print("Завдання 1\n")


class Frog1Descriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("Field can only be read")

    def __delete__(self, instance):
        raise AttributeError("Field can only be read")


class Frog1:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Frog name: {self.name}\nFrog age: {self.age}"

    color = Frog1Descriptor("Light green")


frog1 = Frog1("Grisha", 2)
print(frog1, "\n")
# frog1.color = "Dark green"
# print(frog1, "\n")

print("Завдання 2\n")


class Frog2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        if key == "age":
            if isinstance(value, int):
                self.__dict__[key] = value
            else:
                raise AttributeError("Attribute must be int type")
        self.__dict__[key] = value

    def __str__(self):
        return f"Frog name: {self.name}\nFrog age: {self.age}"


frog2 = Frog2("Sharik", 2)
print(frog2)
frog2.age = 5
print(frog2, "\n")
# frog2.age = "komar"
# print(frog2, "\n")

print("Завдання 3\n")
import datetime

class Frog3:

    def __init__(self, name, age, __color):
        self._name = name
        self.age = age
        self.__color = __color

    def get_color(self):
        return f"Frog's new color: {self.__color}"

    def set_color(self, value):
        time = datetime.datetime.now()
        text = f"Time: {time}\nText: {value}"
        file = open("Frogs_colors.txt", "w+")
        file.write(text)
        file.close()
        self.__color = value

    color = property(get_color, set_color)

    def __str__(self):
        return f"Frog name: {self._name}\nFrog age: {self.age}\nFrog color: {self.__color}"


frog3 = Frog3("Шуша", 3, "green")
print(frog3)
frog3.color = "black"
print(frog3.color)

