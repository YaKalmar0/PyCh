class Employee:
    def __init__(self, n, s, d, y):
        try:
            self.name = n
            self.surname = s
            self.department = d
            self.year = int(y)
            self.acceptance = True
            if  (not self.name.isalpha()) or (not self.surname.isalpha()) or (not self.department.isalpha()) or (self.year > 2019):
                self.acceptance = False
        except (TypeError, ValueError):
            print("Incorrect data.")
            self.acceptance = False

    def pr(self, n):
        if (self.year > n):
            print(self.surname, self.year)

def add_to_list(obj, list = []):
    if(obj.acceptance):
        list.append(obj)

def print_list(n, list = []):
    for i in range(len(list)):
        list[i].pr(n)

E1 = Employee("Artem", "Mykhayliuk", "Marketing", 2010)
E2 = Employee("Pavlo", "Moroz" , "Human Resource", "LaughAndCry")
E3= Employee("Bogdan", "Kryvenko", "Human Resource", 2050)
E4 = Employee("Pavlo", "Skoropadskiy", "Management", 2009)
E5 = Employee("Ostap", "Bender", "Bookkeeping", 2007)

EmList = []
add_to_list(E1, EmList)
add_to_list(E2, EmList)
add_to_list(E3, EmList)
add_to_list(E4, EmList)
add_to_list(E5, EmList)

print_list(2005, EmList)