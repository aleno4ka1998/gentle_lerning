a = int(input())
maximum = 0
quantity_of_maximum = 1
while a != 0:
    if a > maximum:
        maximum = a
        quantity_of_maximum = 1
    elif a == maximum:
        quantity_of_maximum += 1
    a = int(input())
print(quantity_of_maximum)
