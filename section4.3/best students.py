class Pupil:

    def __init__(self, surname, name, math, physics, it):
        self.a = surname
        self.b = name
        self.c = math
        self.d = physics
        self.e = it

    def averageMark(self):
        return float(int((self.c + self.d + self.e)) / 3)

    def __str__(self):
        return str(self.a) + ' ' + str(self.b)

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
