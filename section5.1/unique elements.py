A = list(map(int, input().split()))
B = []
for i in A:
    if A.count(i) == 1:
        B.append(i)
print(' '.join(map(str, B)))
