x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if (abs(x1 - x) + abs(y1 - y)) == 3 and x1 != x and y1 != y:
    print('YES')
else:
    print('NO')
