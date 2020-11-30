s = str(input())
if s.find('f') == s.rfind('f'):
    if s.find('f') == -1:
        print('')
    else:
        print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))
