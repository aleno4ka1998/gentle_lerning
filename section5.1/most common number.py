A = list(map(int, input().split()))
print(max(A, key=A.count))
