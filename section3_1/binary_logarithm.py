n = int(input())
i = 1
k = 0
while i <= n:
    i *= 2
    k += 1
    if i > n:
        print(k)
        break
