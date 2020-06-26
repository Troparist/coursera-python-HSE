s = input()
if s.find("f") == -1:
    print(-2)
elif len(s) - 1 - s[::-1].find("f") == s.find("f"):
    print(-1)
else:
    print(s.find("f") + 1 + s[s.find("f") + 1:].find("f"))
