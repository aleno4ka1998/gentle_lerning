A = list(map(int, input().split()))
min_i = A.index(min(A))
max_i = A.index(max(A))
A[min_i], A[max_i] = A[max_i], A[min_i]
print(' '.join(map(str, A)))
