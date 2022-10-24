print("Завдання 1")

class_list = []

def class_decor(cls):
    def add_to_list(*args, **kwargs):
        if cls not in class_list:
            class_list.append(cls(*args, **kwargs))
        return class_list
    return add_to_list


@class_decor
class Cat1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Кота звуть {self.name} і йому {self.age} років."


cat1 = Cat1("Вася", 5)
print(class_list)

print("Завдання 2")


def info_adder(txt):
    def class_getter(cls):
        def add_text(*args, **kwargs):
            res = txt + str(cls(*args, **kwargs))
            return res
        return add_text
    return class_getter


@info_adder("\nОпис котика:")
class Cat2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"\nКота звуть {self.name}.\nЙому {self.age} років."


cat2 = Cat2("Боня", 3)
print(cat2, "\n")

print("Завдання 3")

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = " + str(self.x)+", y = " + str(self.y) + ", z = " + str(self.z) + " ]"

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def volume_boxes():
        sum_vol = box1.volume() + box2.volume()
        return sum_vol

    @staticmethod
    def up():
        print("up")

    @classmethod
    def print_class_info(cls):
        print(str(cls))


box1 = Box(3, 4, 6)
box2 = Box(2, 5, 9)
print(box1)
print(box2)
print("Сумарний об'єм двох коробків:", Box.volume_boxes())