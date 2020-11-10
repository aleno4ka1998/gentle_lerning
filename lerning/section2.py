a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

a = int(input())
if a % 4 == 0 and not a % 100 == 0:
    print('YES')
elif a % 400 == 0:
    print('YES')
else:
    print('NO')
