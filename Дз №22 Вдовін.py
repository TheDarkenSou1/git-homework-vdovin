import abc


class ABC_Class(abc.ABC):

    @abc.abstractmethod
    def prime_num(self):
        raise NotImplementedError


class Number(ABC_Class):

    def __init__(self, num):
        self.num = num

    def prime_num(self):
        if isinstance(self.num, int):
            for i in range(2, self.num):
                if not self.num % i:
                    return False
            else:
                return True
        else:
            raise ValueError("Number must be int type")

    def __str__(self):
        return f"{self.num}"


num1 = Number(5)
print(num1.prime_num())


class Something:

    def __init__(self, somothing):
        self.somothing = somothing

    def prime_num(self, num):
        pass

ABC_Class.register(Something)

smth = Something("Щось")
print(isinstance(smth, ABC_Class))