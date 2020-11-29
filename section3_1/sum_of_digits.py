def sum_of_digits(n: int):
    sum_of_d = 0
    digit = -1
    while n != 0:
        digit = n % 10
        sum_of_d += digit
        n //= 10
    return sum_of_d

n = int(input())
print(sum_of_digits(n))