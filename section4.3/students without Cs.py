class Coordinate:
    def __init__(self, surname, name, math, physics, it):
        self.a = surname
        self.b = name
        self.c = math
        self.d = physics
        self.e = it

    def goodPupil(self):
        if int(self.c) > 3 and int(self.d) > 3 and int(self.e) > 3:
            return True

    def __str__(self):
        return str(self.a) + ' ' + str(self.b)

n = int(input())
A = []
for _ in range(n):
    surname, name, math, physics, it = input().split()
    pupil = Coordinate(surname, name, math, physics, it)
    A.append(pupil)
for i in range(n):
    pupil = A[i]
    if pupil.goodPupil() is True:
        print(pupil)