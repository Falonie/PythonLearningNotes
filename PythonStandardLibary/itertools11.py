from itertools import accumulate

a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
resutls = list(accumulate(a, max))
print(resutls)