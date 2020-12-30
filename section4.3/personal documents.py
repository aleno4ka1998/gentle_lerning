class Pupil:
    def __init__(self, surname, name, group_kind, date_of_birth):
        self.surname = surname
        self.name = name
        self.group_kind = group_kind
        self.date_of_birth = date_of_birth

    def __str__(self):
        return str(self.group_kind) + ' ' + str(self.surname) + ' ' + str(self.name) + ' ' + str(self.date_of_birth)

n = int(input())
A = []
for _ in range(n):
    surname = str(input())
    name = str(input())
    group_kind = str(input())
    date_of_birth = str(input())
    pupil = Pupil(surname, name, group_kind, date_of_birth)
    A.append(pupil)
A.sort(key=lambda x: (x.group_kind, x.surname))
for pupil in A:
    print(pupil)
