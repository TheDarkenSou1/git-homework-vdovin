from class_limitgrouperror import LimitGroupError
from class_student import Student
class Group:
    """
    creation the group of students
    """
    count = 0
    def __init__(self, title, max_students):
        self.max_students = max_students
        self.title = title
        self.__students = []

    def add_students(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError('Smth wrong with data type')

        if len(self.__students) >= self.max_students:
            raise LimitGroupError(self.max_students, 'Max limit exceed')

        if student in self.__students:
            raise ValueError('Student already registered')

        self.__students.append(student)

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
        else:
            raise TypeError('Smth wrong with data type')

    def __str__(self):
        return f"{self.title}\n" + "\n".join(map(str, self.__students))