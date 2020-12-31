import math

class SetOfCoordinates:
    X = []
    Y = []
    def __init__(self, x, y):
        self.X.append(x)
        self.Y.append(y)

    def distance(self, i, j):
        return math.sqrt((self.X[j] - self.X[i]) ** 2 + (self.Y[j] - self.Y[i]) ** 2)

n = int(input())
maximum = 0
for _ in range(n):
    x, y = map(int, input().split())
    mass_coord = SetOfCoordinates(x, y)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        dis = mass_coord.distance(i, j)
        if dis > maximum:
            maximum = dis
print(maximum)
