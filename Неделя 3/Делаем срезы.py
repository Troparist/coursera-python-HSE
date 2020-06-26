s = input()
if (len(s) - 1 - s[::-1].find("f")) == (s.find("f")) and (s.find("f")) != -1:
    print(s.find("f"))
elif (s.find("f")) != -1:
    print(s.find("f"))
    print(len(s) - 1 - s[::-1].find("f"))
