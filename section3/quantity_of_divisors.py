x = int(input())
y = 0
for i in range(1, x + 1):
    if x % i == 0:
        y += 1
print(y)
