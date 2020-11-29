def reverse(n):
    rev = str('')
    while n > 0:
        rev += str(n % 10)
        n //= 10
    return rev


n = int(input())
k = 0
for i in range(1, n + 1):
    r = int(reverse(i))
    if i == r:
        k += 1
    r = 0
print(k)
