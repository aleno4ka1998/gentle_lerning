class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def absolute(self):
        return(abs(self.x) + abs(self.y))


n = int(input())
maximum = 0
for _ in range(n):
    x, y = map(int, input().split())
    coord = Coordinate(x, y)
    abs_coord = coord.absolute()
    if abs_coord > maximum:
        maximum = abs_coord
        max_x = x
        max_y = y
print(max_x, max_y)
