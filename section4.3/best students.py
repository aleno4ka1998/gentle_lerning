class Pupil:

    def __init__(self, surname, name, math, physics, it):
        self.surname = surname
        self.name = name
        self.math = math
        self.physics = physics
        self.it = it

    def averageMark(self):
        return float(int((self.math + self.physics + self.it)) / 3)

    def __str__(self):
        return str(self.surname) + ' ' + str(self.name)

n = int(input())
A = []
B = []
maximum = 0
for _ in range(n):
    surname, name, math, physics, it = input().split()
    pupil = Pupil(surname, name, math, physics, it)
    A.append(pupil)
for el in A:
    if el.averageMark() == maximum:
        B.append(el)
    if el.averageMark() > maximum:
        maximum = el.averageMark()
        B.clear()
        B.append(el)
print('\n'.join(map(str, B)))
