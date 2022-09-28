print("Завдання 1")


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

class Order:
    """
    order cost
    """
    def __init__(self, customer: Customer):
        self.customer = customer
        self.cart = {}

    def add_product(self, value: Products, quan=1):

        if isinstance(value, Products):
            if self.cart.get(value):
                self.cart[value] += quan
            else:
                self.cart[value] = quan


    def total(self):
        summa = 0
        for item, quantity in self.cart.items():
            summa += item.price * quantity
        return summa

    def __str__(self):
        res = f"{self.customer}\n"
        for product, quantity in self.cart.items():
            res += f"{product} * {quantity} = {product.price * quantity} грн."

        return res

pr1 = Products("Печенье", "дадада")
pr2 = Products("Конфеты", 30)
pr3 = Products("Зефир", 40)
list_pr = [pr1, pr2, pr3]
client3 = Customer("Вдовін", "Андрій", "Максимович", "0994123299")

try:
    order1 = Order(client3)
    order1.add_product(pr1, 3)
    order1.add_product(pr2, 2)
    order1.add_product(pr3, 1)
    for pr in list_pr:
        if type(pr.price) == str:
            raise PriceError2("Error. Price is integer or floating, but not string")
except PriceError2 as err:
    print(err.get_message())
else:
    try:
        order1 = Order(client3)
        order1.add_product(pr1, 3)
        order1.add_product(pr2, 2)
        order1.add_product(pr3, 1)
        for pr in list_pr:
            if pr.price <= 0:
                raise PriceError1("Error. Price can't be less or equel to 0")
    except PriceError1 as err:
        print(err.get_message())
    else:
        print(order1)
        print(order1.total())

print("Завдання 2")


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
            raise TypeError('Smth wrong with data type')

        if len(self.__students) >= self.max_students:
            raise ValueError('Max limit exceed')

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

try:
    gr1 = Group("Python PRO", max_students=9)
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
else:
    print(gr1, "\n")