def my_iter(iterable):
    i = 0
    j = len(iterable)-1
    while i <= j:
        temp = iterable[i]
        iterable[i] = iterable[j]
        iterable[j] = temp
        i+=1
        j-=1
    return iterable

def my_gen(iterable):
    for x in iterable[::-1]:
        yield x


#def my_gen(iterable)


my_list = [1 ,2, 53, 78, 120, 3]
my_iter(my_list)

rev_iter = my_gen(my_list)

print(next(rev_iter))
print(next(rev_iter))
print(next(rev_iter))