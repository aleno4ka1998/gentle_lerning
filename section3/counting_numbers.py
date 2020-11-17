n = int(input())
null = 0
positive = 0
negative = 0
for i in range(1, n + 1):
    x = int(input())
    if x == 0:
        null += 1
    elif x > 0:
        positive += 1
    elif x < 0:
        negative += 1
print(null, positive, negative)
