a = 0
b = 0
sequence_sum = 0
while True:
    sequence_sum += a
    a = int(input())
    if a == 0:
        b = int(input())
        if b == 0:
            break
        else:
            sequence_sum += b
print(sequence_sum)
