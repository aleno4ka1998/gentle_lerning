def number_of_zeros(n: int):
    number_of_z = 0
    digit = -1
    while n != 0:
        digit = n % 10
        if digit == 0:
            number_of_z += 1
        n //= 10
    return number_of_z

n = int(input())
print(number_of_zeros(n))