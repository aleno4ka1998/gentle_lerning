def reverse(n):
    rev = str('')
    while n > 0:
        rev += str(n % 10)
        n //= 10
    return rev


n = int(input())
print(reverse(n))