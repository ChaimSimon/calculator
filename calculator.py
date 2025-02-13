from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        pass

    def mul(self, a, b):
        x = int(input("enter a number"))
        y = int(input("enter a number"))
        c = 0
        for i in range(y):
            c += x
        return c
    @staticmethod
    def pow(basis, appraiser):
        result = 1
        while appraiser:
            result *= basis
            appraiser -= 1
        return result


    def div(self, a, b):
        x = int(input("enter a number"))
        y = int(input("enter a number"))
        c = x
        d = 0
        while c:
            c -= y
            d += 1
        return d

    def root(self, a, b):
        pass


print(Calculator.pow(2,5))