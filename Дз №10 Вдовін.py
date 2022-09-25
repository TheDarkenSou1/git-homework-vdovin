print("Завдання 1")
class Product:
    """
    gives a brief description of the product: price, description, size
    """
    def __init__(self, cost, description, size):
        self.cost = cost
        self.description = description
        self.size = size

    def __str__(self):
        return f'Ціна товару: {self.cost} грн.\nОпис товару: {self.description}\nРозмір товару: {self.size}\n'

t1 = Product(100, "Кишеньковий ліхтар", "маленький")
t2 = Product(3500, "Nokia 3310 - легендарний кнопковий телефон", "маленький")
print(t1)
print(t2)

print("Завдання 2")
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

client1 = Customer("Вдовін", "Андрій", "Максимович", "0994123299")
client2 = Customer("Петров", "Петр", "Петрович", "1234567890")
print(client1)
print(client2)

print("Завдання 3")
class Products:
    """
    name and prices of a product
    """
    def __init__(self, title: str, price: int | float):
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

pr1 = Products("Печенье", 25)
pr2 = Products("Конфеты", 30)
pr3 = Products("Зефир", 40)

client3 = Customer("Вдовін", "Андрій", "Максимович", "0994123299")
client4 = Customer("Петров", "Петр", "Петрович", "1234567890")

order1 = Order(client3)
order1.add_product(pr1, 3)
order1.add_product(pr2, 2)
order1.add_product(pr3, 1)
print(order1)
print(order1.total())

order2 = Order(client4)
order2.add_product(pr1, 10)
order2.add_product(pr2, 5)
order2.add_product(pr3, 26)
print(order2)
print(order2.total())