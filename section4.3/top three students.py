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
print(A[0], A[1], A[2], sep='\n')
pupil = A[2]
for i in range(3, n):
    next_pupil = A[i]
    if pupil.averageMark == next_pupil.averageMark:
        print(A[i])
