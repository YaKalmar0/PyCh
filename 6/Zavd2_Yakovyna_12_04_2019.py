def shorten(dict0, keyw, link):
    if keyw is None:
        print("Error!")
    elif link is None:
        return dict0.get(keyw)
    else:
        dict0.setdefault(keyw, link)

str1 = "facebook.com"
str2 = "fb.com"
dict2 = {}
shorten(dict2, str2, str1)
str3 = "vkontakte.com"
str4 = "vk.com"
shorten(dict2, str4, str3)
print(dict2)

print(shorten(dict2, str2, None))