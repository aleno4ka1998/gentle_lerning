s = input()
beg = s[:s.find('h') + 1]
mid = s[s.find('h') + 1:s.rfind('h')]
end = s[s.rfind('h'):]
print(beg, mid, mid, end, sep='')
