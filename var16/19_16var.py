# +2 или *2
# Победа когда сумма дву >= 79
# начальный момент (9, S) S Принадлежит [1 ; 69] 
# Петя = 1, Ваня = -1


p0 = 9

def choice(p, player):
    global count

    if p[0]+2 + p[1] >= 79:
        return (player,count)
    else:
        count +=1
        b = p
        b[0] += 2
        player = player * (-1)
        return choice(b,player)
    
    if p[0] + p[1]+2 >= 79:
        return (player,count)
    else:
        count +=1
        b = p
        b[1]+= 2
        player = player * (-1)
        return choice(b,player)

    if p[0]*2 + p[1] >= 79:
        return (player,count)
    else:
        count +=1
        b = p
        b[0] = b[0] * 2
        player = player * (-1)
        return choice(b,player)

    if p[0] + p[1] * 2 >= 79:
        return (player,count)
    else:
        count +=1
        b = p
        b[1]= b[1] * 2
        player = player * (-1)
        return choice(b,player)
    

for s in range(1, 70):
    a = [p0, s]
    count = 1
    print(choice(a,1))
    if choice(a , 1) == (1,3):
        print(s)
        break
