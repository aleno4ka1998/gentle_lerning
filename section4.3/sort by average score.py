class Pupil:

    def __init__(self, surname, name, math, physics, it):
        self.surname = surname
        self.name = name
        self.math = math
        self.physics = physics
        self.it = it
        self.averageMark = float(int((self.math + self.physics + self.it)) / 3)

    def __str__(self):
        return str(self.surname) + ' ' + str(self.name)

n = int(input())
A = []
for _ in range(n):
    surname, name, math, physics, it = input().split()
    pupil = Pupil(surname, name, math, physics, it)
    A.append(pupil)
A = sorted(A, key=lambda x: - x.averageMark)
for pupil in A:
    print(pupil)
