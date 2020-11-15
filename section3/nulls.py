n = int(input())
nulls = 0
for i in range(1, n + 1):
    x = int(input())
    if x == 0:
        nulls += 1
print(nulls)
