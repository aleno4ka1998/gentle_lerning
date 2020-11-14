n = int(input())
total =1
for i in range(1, n + 1):
    total += (-1) ** i / (2 * i + 1)
print(total * 4)
