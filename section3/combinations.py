n = int(input())
k = int(input())
n1 = 1
k1 = 1
factorial_sum = 1
for i in range(1, n + 1):
    n1 *= i
for i in range(1, k + 1):
    k1 *= i
for i in range(1, n - k + 1):
    factorial_sum *= i
print(int(n1 / (k1 * factorial_sum)))
