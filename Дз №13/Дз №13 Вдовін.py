from class_student import Student
from class_group import Group
from class_limitgrouperror import LimitGroupError

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

try:
    gr1 = Group("Python PRO", max_students=10)
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

except LimitGroupError as error:
    print(error.__str__())
else:
    print(gr1, "\n")