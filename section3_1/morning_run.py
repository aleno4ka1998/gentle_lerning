x = int(input())
y = int(input())
k = 0
while x < y:
    x += x / 10
    k += 1
    if x >= y:
        k += 1
print(k)
