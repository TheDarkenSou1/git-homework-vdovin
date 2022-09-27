print("Завдання 1, 2 і 3\n")

class Person:
    """
    surname and name of person
    """
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f"{self.surname} {self.name}"

class Student(Person):
    """
    info student
    """
    def __init__(self, surname, name, birthday_data):
        super().__init__(surname, name)
        self.birthday_data = birthday_data

    def __str__(self):
        return f"{self.surname} {self.name}, {self.birthday_data}"

class Group:
    """
    creation the group of students
    """
    count = 0
    def __init__(self, title, max_students = 10):
        self.max_students = max_students
        self.title = title
        self.__students = []

    def add_students(self, student: Student):
        if not isinstance(student, Student):
            return -1
        if len(self.__students) < self.max_students and student not in self.__students:
            self.__students.append(student)
            return None
        return -1

    def search_students(self, surname : str):
        res = []
        for student in self.__students:
            if surname.strip().lower() == student.surname.lower():
                res.append(student)
        return res

    def remove_students(self, student):
        if isinstance(student, Student):
            if student in self.__students:
                self.__students.remove(student)

    def __str__(self):
        return f"{self.title}\n" + "\n".join(map(str, self.__students))

st1 = Student("Вдовін", "Андрій", "26.07.2003")
st2 = Student("Пиріжок", "Максим", "01.03.2001")
st3 = Student("Арбуз", "Віктор", "14.04.2004")
st4 = Student("Кавун", "Роман", "16.05.2002")
st5 = Student("Персик", "Олександр", "10.06.2003")
st6 = Student("Слива", "Григорій", "09.08.2002")
st7 = Student("Абрикос", "Марія", "22.09.2002")
st8 = Student("Вишня", "Дарья", "23.10.2001")
st9 = Student("Полуниця", "Люба", "29.11.2001")
st10 = Student("Батьківна", "Олена", "27.12.2000")

gr1 = Group("Python PRO")
gr1.add_students(st1)
gr1.add_students(st2)
gr1.add_students(st3)
gr1.add_students(st4)
gr1.add_students(st5)
gr1.add_students(st6)
gr1.add_students(st7)
gr1.add_students(st8)
gr1.add_students(st9)
gr1.add_students(st10)
print(gr1, "\n")

gr1.remove_students(st10)
gr1.remove_students(st9)
print(gr1, "\n")

print(gr1.search_students("Вдовін"))



