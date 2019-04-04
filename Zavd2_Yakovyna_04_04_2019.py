class Graph:
    def state(self):
        print("I exist!")

class Rectangle(Graph):
    def __init__(self, s1, s2):
        self.a = s1
        self.b = s2
    def __repr__(self):
        print("Rectangle with a =", self.a, "and b =", self.b)

class Mouse():
    def click(self):
        print("Left Button Pressed")

def main():
    Gr = Graph()
    Rec = Rectangle.__init__(Gr, 10, 15)
    Rec.__repr__()
    M1 = Mouse()
    M1.click()

if __name__ == "__main__":
    main()

Rec = Rectangle(10, 15)
Rec.__repr__()