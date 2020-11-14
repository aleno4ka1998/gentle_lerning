n = int(input())
total = 1
total1 = 1
for i in range(1, n + 1):
    for k in range(1, i + 1):
        total1 *= k
    total += 1 / total1
print("{:.5f}".format(total))
