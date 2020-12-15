N, K = map(int, input().split())
skittles = ['I' for _ in range(N)]
for _ in range(K):
    l, r = map(int, input().split())
    for i in range(l - 1, r):
        skittles[i] = '.'
print(''.join(skittles))