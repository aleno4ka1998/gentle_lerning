n = int(input())
a = 0
b = 1
c = 0
k = 1
while b != n:
    c, a = a, b
    b += c
    k += 1
    if n < b:
        k = -1
        break
print(k)
