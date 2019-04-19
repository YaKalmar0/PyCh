def decor(func):
    def filtered(*args, **kwargs):
        a = list(filter(lambda x: x % 2 == 0, func(*args, **kwargs)))
        return a
    return filtered

@decor
def fib(N):
    arr = [0, 1]
    a = 1
    b = 0
    for i in range(2, N):
        k = a + b
        b = a
        a = k
        arr.append(a)
    return arr

print(fib(10))