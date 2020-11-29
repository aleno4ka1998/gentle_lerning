def reverse_binary(n):
    rev = str('')
    while n > 0:
        rev += str(n % 2)
        n //= 2
    return rev


n = int(input())
print(reverse_binary(n))