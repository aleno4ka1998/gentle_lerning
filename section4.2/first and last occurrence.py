s = str(input())
f = s.find('f')
l = s.rfind('f')
if f != l:
    print(f, l)
elif f != -1:
    print(f)
