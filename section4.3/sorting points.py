class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x + self.y <= other.x + other.y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

n = int(input())
A = []
B = []
for _ in range(n):
    x, y = map(int, input().split())
    point = Coordinate(x, y)
    A.append(point)
B = sorted(A, key=lambda x: x)
print('\n'.join(map(str, B)))
