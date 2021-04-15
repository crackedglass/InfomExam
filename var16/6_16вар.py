
for i in range(0,100000):
    s = i
    n = 127
    while s – n > 0:
        s = s + 15
        n = n + 20
    if s // 1000 > 0:
        print(s)
        break
    
