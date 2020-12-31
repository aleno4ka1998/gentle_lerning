class Coordinates:
    X = []
    Y = []
    def __init__(self, x, y):
        self.X.append(x)
        self.Y.append(y)

    def center(self):
        cen_x = sum(self.X) / len(self.X)
        cen_y = sum(self.Y) / len(self.Y)
        return(cen_x, cen_y)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    mass_coord = Coordinates(x, y)
print(mass_coord.center())


