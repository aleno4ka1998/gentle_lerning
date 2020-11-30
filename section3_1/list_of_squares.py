from math import sqrt
n = int(input())
i = 1
while i <= n:
    if int(sqrt(i)) ** 2 == i:
        print(i, end=' ')
    i += 1
