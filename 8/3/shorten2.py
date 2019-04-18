def shorten(dict0, keyw, link):
    if keyw is None:
        print("Error!")
    elif link is None:
        with open("web.txt", "r") as file:
            for line in file:
                str = line.split()
                if str[0] == keyw:
                    return str[2]
            print("No matches.")
    else:
        with open("web.txt", "a") as file:
            s = keyw + " : " + link + "\n"
            file.write(s)
            dict0.setdefault(keyw, link)