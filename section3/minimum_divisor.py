x = int(input())
y = 0
for i in range(x, 1, -1):
    if x % i == 0:
        y = i
print(y)
