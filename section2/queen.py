x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if (x1 - y1) == (x - y) or (x1 + y1) == (x + y) or x == x1 or y == y1:
    print('YES')
else:
    print('NO')