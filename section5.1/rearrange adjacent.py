A = list(map(int, input().split()))
for i in range(1, len(A), 2):
    A[i - 1], A[i] = A[i], A[i - 1]
print(' '.join(map(str, A)))
