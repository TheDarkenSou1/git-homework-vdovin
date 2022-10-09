print("Завдання 1\n")

class LimitGroupError(Exception):

    def __init__(self, value=None, msg=None):
        super().__init__()
        self.value = value
        self.msg = msg

    def __str__(self):
        return f'Current Limit in Group = {self.value}\n{self.msg}'

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
    def __init__(self, surname : str, name : str, birthday_data):
        super().__init__(surname, name)
        self.birthday_data = birthday_data

    def __str__(self):
        return f"{self.surname} {self.name}, {self.birthday_data}"

class GroupIterator:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

class Group:
    """
    creation the group of students
    """
    count = 0
    def __init__(self, title, max_students):
        self.max_students = max_students
        self.title = title
        self.students = []

    def add_students(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError('Smth wrong with data type')

        if len(self.students) >= self.max_students:
            raise LimitGroupError(self.max_students, "Max limit error")

        if student in self.students:
            raise ValueError('Student already registered')

        self.students.append(student)

    def search_students(self, surname : str):
        res = []
        for student in self.students:
            if surname.strip().lower() == student.surname.lower():
                res.append(student)
        return res

    def remove_students(self, student):
        if isinstance(student, Student):
            if student in self.students:
                self.students.remove(student)
        else:
            raise TypeError('Smth wrong with data type')

    def __iter__(self):
        return GroupIterator(self.students)

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return f"{self.title}\n" + "\n".join(map(str, self.students))

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

gr1 = Group("Python PRO", max_students=10)

try:
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
except Exception as error:
    print(error)


count = len(gr1.students)

for person in range(count):
    print(gr1.students[person], f": {person + 1} у групі.")

print("\nЗавдання 2\n")


class PriceError1(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_message(self):
        return self.message


class PriceError2(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_message(self):
        return self.message


class Customer:
    """
    gives a brief description of the product: price, description, size
    """

    def __init__(self, surname, name, patronymic, phone_number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        return f"Прізвище: {self.surname}\nИм'я: {self.name}\nПо-батькові: {self.patronymic}\nНомер телефону: {self.phone_number}\n"


class Products:
    """
    name and price of a product
    """

    def __init__(self, title: str, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} : {self.price}"

class OrderIterator:
    def __init__(self, order):
        self.order = order
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.order):
            self.index += 1
            return self.order[self.index - 1]
        else:
            raise StopIteration


class Order:
    """
    order cost
    """

    def __init__(self, customer: Customer):
        self.customer = customer
        self.cart = {}
        self.list_cart = []

    def add_product(self, good, quantity):
        self.good = good
        self.quantity = quantity
        self.cart[good] = self.quantity
        self.list_cart.append((good, ": ", str(self.cart.get(good))))

    def total(self):
        summa = 0
        for item in self.cart:
            summa += self.cart.get(item) * item.price
        return summa

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.list_cart[item]
        if isinstance(item, slice):
            start = 0 if item.start is None else item.start
            stop = len(self.list_cart) if item.stop is None else item.stop
            step = 1 if item.step is None else item.step
            res = []
            for itm in range(start, stop, step):
                res.append(self.list_cart[itm])
            return res

    def __iter__(self):
        return OrderIterator(self.list_cart)

    def __str__(self):
        res = f"{self.customer}\n"
        for product, quantity in self.cart.items():
            res += f"{product} * {quantity} = {product.price * quantity} грн. "

        return res


pr1 = Products("Печиво", 16)
pr2 = Products("Цукерки", 30)
pr3 = Products("Зефір", 40)
client3 = Customer("Вдовін", "Андрій", "Максимович", "0994123299")

order1 = Order(client3)
order1.add_product(pr1, 3)
order1.add_product(pr2, 2)
order1.add_product(pr3, 1)
print(order1, "\n")

print(order1[0:2])

for i in order1.cart:
    print(i)
