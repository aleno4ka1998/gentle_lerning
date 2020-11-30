max_length = 0
dec_length = 1
inc_length = 1
a = int(input())
while a != 0:
    max_length = max(dec_length, inc_length, max_length)
    b = int(input())
    if a < b:
        inc_length += 1
        dec_length = 1
    elif a > b:
        dec_length += 1
        inc_length = 1
    elif a == b:
        dec_length = 1
        inc_length = 1
    a = b
print(max_length)
