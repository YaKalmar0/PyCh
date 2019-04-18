import shorten2 as func

print("Welcome to shorten!")
print("Here you can store full and shortened name of website.")

a = input("Enter full-version: ")
b = input("Enter short-version: ")

dictmain = {}
func.shorten(dictmain, b, a)

c = input("Print? Y/N ")
if c is ('y' or 'Y'):
    print(dictmain)

print("Do you want to add another link? Y/N ")
c = input()
if c is ('y' or 'Y'):
    a = input("Enter full-version ")
    b = input("Enter short-version ")
    func.shorten(dictmain, b, a)
else:
    pass

c = input("Enter short-version to get full: ")
print("Your full version: ", func.shorten(dictmain, c, None))