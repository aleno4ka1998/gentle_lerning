A = list(map(int, input().split()))
for i in range(1, len(A)):
    if A[i] * A[i - 1] > 0:
        print(A[i - 1], A[i], end=' ')
        break
