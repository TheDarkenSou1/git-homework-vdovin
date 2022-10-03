from class_person import Person

class Student(Person):
    """
    info student
    """
    def __init__(self, surname : str, name : str, birthday_data):
        super().__init__(surname, name)
        self.birthday_data = birthday_data

    def __str__(self):
        return f"{self.surname} {self.name}, {self.birthday_data}"