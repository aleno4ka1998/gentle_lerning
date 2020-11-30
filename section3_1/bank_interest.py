x = int(input())
p = int(input())
y = int(input())
k = 0
while x < y:
    x = int(x + (x / 100 * p))
    k += 1
print(k)
