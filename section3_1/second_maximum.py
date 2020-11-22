a = 1
k = 0
maximum = 0
sec_maximum = 0
while a != 0:
    k = a
    a = int(input())
    if a > k and a != 0:
        sec_maximum = maximum
        maximum = a
print(sec_maximum)
