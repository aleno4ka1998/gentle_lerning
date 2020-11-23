current = -1
previous = -1
seq_num = 1
max_seq_num = 1
while current != 0:
    current = int(input())
    if current == previous:
        seq_num += 1
    else:
        if seq_num > max_seq_num:
            max_seq_num = seq_num
            seq_num = 0
    previous = current
print(max_seq_num)
