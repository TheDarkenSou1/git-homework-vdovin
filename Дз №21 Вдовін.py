class MetaFrog(type):

    def __new__(type_class, class_name, supers, class_dict):
        text = class_name + "\n"
        for el in class_dict:
            text += str(el) + " = " + str(class_dict[el]) + "\n"
        file = open("Info.txt", "w+")
        file.write(text)
        file.close()
        return type.__new__(type_class, class_name, supers, class_dict)


class Frog(metaclass=MetaFrog):

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__} [Frog's name: {self.name}. " \
               f"Frog's age: {self.age}. Frog's color: {self.color}]"


frog1 = Frog("Мурлок", 3, "green")
print(frog1)
