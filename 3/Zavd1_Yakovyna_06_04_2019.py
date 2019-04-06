class Sum:
    def __init__(self, a, b):
        self.arg1 = a
        self.arg2 = b
        self.sum = 0

    def do(self):
        try:
            self.sum = self.arg1 + self.arg2
        except (TypeError, ValueError):
            print("Error: Unsupported operation. Try again:")
            a1 = float(input())
            a2 = float(input())
            self.__init__(a1, a2)
            self.do()

    def __str__(self):
        print(self.arg1, "+", self.arg2, "=", self.sum)

class Sub:
    def __init__(self, a, b):
        self.arg1 = a
        self.arg2 = b
        self.subs = 0

    def do(self):
        try:
            self.subs = self.arg1 - self.arg2
        except (TypeError, ValueError):
            print("Error: Unsupported operation. Try again:")
            a1 = float(input())
            a2 = float(input())
            self.__init__(a1, a2)
            self.do()


    def __str__(self):
        print(self.arg1, "-", self.arg2, "=", self.subs)

class Mul:
    def __init__(self, a, b):
        self.arg1 = a
        self.arg2 = b
        self.mult = 0

    def do(self):
        try:
            self.mult = self.arg1 * self.arg2
        except (TypeError, ValueError):
            print("Error: Unsupported operation. Try again:")
            a1 = float(input())
            a2 = float(input())
            self.__init__(a1, a2)
            self.do()


    def __str__(self):
        print(self.arg1, "*", self.arg2, "=", self.mult)

class Div:
    def __init__(self, a, b):
        self.arg1 = a
        self.arg2 = b
        self.div = 0

    def do(self):
        try:
            self.div = self.arg1 / self.arg2
        except ZeroDivisionError:
            print("Error: Division by Zero. Try again:")
            a1 = float(input())
            a2 = float(input())
            self.__init__(a1, a2)
            self.do()
        except (TypeError, ValueError):
            print("Error: Unsupported operation. Try again:")
            a1 = float(input())
            a2 = float(input())
            self.__init__(a1, a2)
            self.do()


    def __str__(self):
        print(self.arg1, "/", self.arg2, "=", self.div)


class Raise:
    def __init__(self, a, b):
        self.arg1 = a
        self.arg2 = b
        self.rai = 0

    def do(self):
        try:
            self.rai = pow(self.arg1, self.arg2)
        except (TypeError, ValueError):
            print("Error: Unsupported operation. Try again:")
            a1 = float(input())
            a2 = float(input())
            self.__init__(a1, a2)
            self.do()

    def __str__(self):
        print("{0}^{1} =".format(self.arg1, self.arg2), self.rai)

div1 = Div(10, 0)
div1.do()
div1.__str__()
rai1 = Raise(5, 0)
rai1.do()
rai1.__str__()
sum1 = Div(2, 10)
sum1.do()
sum1.__str__()
subs1 = Sub(20, 17)
subs1.do()
subs1.__str__()
mul1 = Mul("Skoropadsky", "is what we need.")
mul1.do()
mul1.__str__()