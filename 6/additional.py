def func(count, *strings):
    if count <= 0:
        return("Error")
    strn = []
    for i in strings:
        print("NEW KEY")
        str0 = []
        for j in i:
            key = ord(j)
            print("key1 = ", key)
            k = 0
            while(k < count):
                key += 1
                print("key2 = ", key)
                if key is 123:
                    key = 92
                k += 1
                print("key3 = ", key)
                
            sym = chr(key)
            str0 += sym
            str0 = [''.join(str0)]
        strn += str0
    return strn



str1 = 'abc'
str2 = 'dklt'

print(func(12, str1, str2))
