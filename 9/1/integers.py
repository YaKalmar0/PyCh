arr = []
N = 10
for i in range(1, 10):
    arr.append(i)

arr2 = []
arr2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, arr)))

print(arr2)