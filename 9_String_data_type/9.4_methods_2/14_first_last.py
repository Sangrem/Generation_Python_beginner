s = input()

if s.count("f") == 0:
    print("NO")
elif s.find("f") == s.rfind("f"):
    print(s.find("f"))
else:
    print(s.find("f"), s.rfind("f"))
