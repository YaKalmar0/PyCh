def average(fst, snd, *num):
    if fst and snd is None:
       aver = (sum(num)) / len(num)
    else:
        aver = (sum(num[fst:snd])) / len(num[fst:snd])
    return aver


so = average(None, None, 2, 4)
print(so)
so = average(0, 2, 10, 230, 321, 32)
print("average = ", so)