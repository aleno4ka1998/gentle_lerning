a = int(input())
maximum = 0
second_maximum = 0
while a != 0:
    if a > maximum:
        second_maximum = maximum
        maximum = a
    a = int(input())
print(second_maximum)
