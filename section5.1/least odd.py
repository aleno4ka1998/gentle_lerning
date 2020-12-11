A = list(map(int, input().split()))
k = 0
for el in A:
    if el % 2 != 0:
        k = 1
        print(min(filter(lambda i: i % 2 != 0, A)))
        break
if k == 0:
    print(k)
