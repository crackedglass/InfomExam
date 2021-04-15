a = ["7"] * 143
s = "".join(a)


while s.find("777") != -1:
    i = s.find("777")
    a[i:i+3] = ["2"] * 2
    s = "".join(a)
    i = s.find("222")
    if i != -1:
        a[i:i+3] = ["7"]
        s = "".join(a)
print(a)
