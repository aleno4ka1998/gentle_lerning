A = list(map(int, input().split()))
n = 0
for i in A:
    n += A.count(A[i]) - 1
print(n // 2)
