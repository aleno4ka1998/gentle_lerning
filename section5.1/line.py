A = list(map(int, input().split()))
high = int(input())
k = 1
for el in A:
    if el >= high:
        k += 1
print(k)
