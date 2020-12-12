A = list(map(int, input().split()))
k, c = map(int, input().split())
A.insert(k, c)
print(' '.join(map(str, A)))