s = input()
a = s.find('h')
b = s.rfind('h')
c = s[0:a]
d = s[b+1::1]
print(c+d)
