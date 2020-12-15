A = list(map(int, input().split()))
for i in range(len(A)):
    if A[i] < 0:
        A[i] = 1001
print(min(A))
