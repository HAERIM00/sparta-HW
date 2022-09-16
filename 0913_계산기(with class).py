class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.num1} {self.num2}"

    def plus(self):
        return f"{self.num1+self.num2}"

    def minus(self):
        return f"{self.num1 - self.num2}"

    def multiple(self):
        return f"{self.num1 * self.num2}"

    def divide(self):
        return f"{self.num1 // self.num2}"

calc = Calc(20, 10)
print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())
