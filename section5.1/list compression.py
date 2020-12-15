A = list(map(int, input().split()))
for i in reversed(range(len(A))):
    if A[i] == 0:
        A.append(A.pop(i))
print(' '.join(map(str, A)))
