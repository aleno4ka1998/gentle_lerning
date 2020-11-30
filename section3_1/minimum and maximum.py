def max_digit(n: int):
    max_d = 0
    digit = -1
    while n != 0:
        digit = n % 10
        if digit > max_d:
            max_d = digit
        n //= 10
    return max_d


def min_digit(n: int):
    min_d = 10
    digit = -1
    while n != 0:
        digit = n % 10
        if digit < min_d:
            min_d = digit
        n //= 10
    return min_d


n = int(input())
print(min_digit(n), max_digit(n))
