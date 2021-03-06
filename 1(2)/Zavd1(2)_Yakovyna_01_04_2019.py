class Book:
    def __init__(self, a, n, y ,g, com):
        self.author = a
        self.name = n
        self.year = y
        self.genre = g
        self.response = com.comment

    def __repr__(self):
	    return 'Book: %s, %s, %d, %s' % (self.author, self.name, self.year, self.genre)

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name and self.year == other.year and self.genre == other.genre

    def __ne__(self, other):
        return not (self == other)

class Comment:
    def __init__(self,com):
        self.comment = com


Com1 = Comment("The Best book I've ever read")
Com2 = Comment("Satisfied")
Book1 = Book("Jack London", "Sea Wolf", 1904, "Adventure", Com1)
Book2 = Book("Norman Davis", "Europe", 1996, "Science", Com2)
Book3 = Book1

print ("Equality1: ")
print(Book1 == Book2)
print("Equality2: ")
print(Book1 == Book3)

print('\t')
print(Book1)
print(Book1.response)
print('\t')
print(Book2)
print(Book2.response)