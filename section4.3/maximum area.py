import math

class SetOfCoordinates:
    X = []
    Y = []
    def __init__(self, x, y):
        self.X.append(x)
        self.Y.append(y)

    def distance(self, i, j):
        return math.sqrt((self.X[j] - self.X[i]) ** 2 + (self.Y[j] - self.Y[i]) ** 2)

    def semiperimeter(self, a, b, c):
        return (a + b + c) / 2

n = int(input())
maximum = 0
for _ in range(n):
    x, y = map(int, input().split())
    mass_coord = SetOfCoordinates(x, y)
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            dis1 = mass_coord.distance(i, j)
            dis2 = mass_coord.distance(j, k)
            dis3 = mass_coord.distance(i, k)
            p = mass_coord.semiperimeter(dis1, dis2, dis3)
            square = math.sqrt(p * (p - dis1) * (p - dis2) * (p - dis3))
        if square > maximum:
            maximum = square
print(maximum)
