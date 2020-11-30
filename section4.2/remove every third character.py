s = input()
p = ''
for i in range(0, len(s)):
    if i % 3 != 0:
        p += s[i]
print(p)