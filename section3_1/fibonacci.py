n = int(input())
a = 0
b = 1
c = 0
k = 1
while k != n:
    c, a = a, b
    b = c + b
    k += 1
print(b)
