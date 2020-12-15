x = [0] * 8
y = [0] * 8
for i in range(8):
    x[i], y[i] = map(int, input().split())
for a in range(8):
    for b in range(a + 1, 8):
        if abs(x[a] - x[b]) == abs(y[a] - y[b]) or x[a] == x[b] or y[a] == y[b]:
            print('YES')
            exit()
print('NO')
