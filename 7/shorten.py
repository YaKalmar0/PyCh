def shorten(dict0, keyw, link):
    if keyw is None:
        print("Error!")
    elif link is None:
        return dict0.get(keyw)
    else:
        dict0.setdefault(keyw, link)