def func(count, *strings):
    strn = []
    for i in strings:
        str0 = []
        for j in i:
            key = ord(j)
            sym = chr(key + count)
            str0 += sym
            str0 = [''.join(str0)]
        strn += str0
    return strn



str1 = 'abc'
str2 = 'dklt'

print(func(1, str1, str2))