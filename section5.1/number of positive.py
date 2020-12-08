A = list(map(int, input().split()))
k = 0
for i in range(len(A)):
    if A[i] > 0:
        k += 1
print(k)
