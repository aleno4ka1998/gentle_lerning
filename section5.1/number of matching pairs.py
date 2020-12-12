A = list(map(int, input().split()))
n = 0
for i in A:
    n += A.count(i) - 1
print(n // 2)
