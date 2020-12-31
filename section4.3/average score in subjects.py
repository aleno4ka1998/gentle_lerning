class Coordinate:
    def __init__(self, surname, name, math, physics, it):
        self.a = surname
        self.b = name
        self.c = math
        self.d = physics
        self.e = it

    def mathMark(self):
        return int(self.c)

    def mathPhysics(self):
        return int(self.d)

    def mathIt(self):
        return int(self.e)

n = int(input())
A = []
math_sum = 0
physics_sum = 0
it_sum = 0
for _ in range(n):
    surname, name, math, physics, it = input().split()
    pupil = Coordinate(surname, name, math, physics, it)
    A.append(pupil)
for i in range(n):
    pupil = A[i]
    math_sum += pupil.mathMark()
    physics_sum += pupil.mathPhysics()
    it_sum += pupil.mathIt()
print(math_sum / n, physics_sum / n, it_sum / n)
