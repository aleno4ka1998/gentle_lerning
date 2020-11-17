sec = int(input())
numeral = 1
position = 1
for i in range(1, sec + 1):
    print(numeral, end=' ')
    position += 1
    if position > numeral:
        numeral += 1
        position = 1
