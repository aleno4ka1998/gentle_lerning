a = int(input())
b = int(input())
c = -1
k = 0
while c != 0:
    c = int(input())
    if a < b > c:
        k += 1
    a = b
    b = c
print(k)
