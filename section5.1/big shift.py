A = list(map(int, input().split()))
k = int(input())
if k > 0:
    for i in range(k):
        A.insert(0, A.pop())
else:
    for i in range(-k):
        A.append(A.pop(0))
print(' '.join(map(str, A)))
