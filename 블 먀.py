import random
card = []
db = 0
mb = 0
p = 0
a = 0
kkk = 1
myca = []
deal = []
mycabackup = []
dealbackup = []
count = 0
numbers = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
numbersbackup = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
score = []
dlist = []
stay = []
burst = []
dlistback = []
stayback = []
burstback = []
plus = 0
plus2 = 0

def ai():
    global stay
    global dlist
    global burst
    global plus
    global plus2
    dlist = dlistback[:]
    stay = stayback[:]
    burst = burstback[:]
    if plus2 > 20:
        print("stay")
    if plus2 < 12:
        print("hit")
    if plus2 < 21 and plus2 > 11:
        longl = int(len(deal))
        plus3 = 0
        sep = 0
        sta = 0
        jack = 0
        me = 0
        stay1 = 0
        hitwin = 0
        hitwin1 = 0
        hitwin2 = 0
        hitwin3 = 0
        staywin = 0
        if longl > 2:
            for x in range(1,longl-1):
                plus3 = plus3 + deal[x]
            sep = 16 - plus3
            if sep < 11:
                fin = sep
            else:
                fin = 11
            if 17 - plus + deal[0] > 2:
                sta = 17 - plus + deal[0]
            else:
                sta = 2
            for y in range(sta,fin+1):
                dlist.append(y)
            if 10 in dlist:
                for x in range(0,3):
                    dlist.append(10)
            if 21 - plus + deal[0]<12:
                jack = 21 - plus + deal[0]
                for z in dlist:
                    if z < jack:
                        stay.append(z)
                    if z > jack:
                        burst.append(z)
            else:
                stay = dlist
            stayy = int(len(stay))
            burstt = int(len(burst))
            dlistt = int(len(dlist))
            if plus2 < plus - deal[0]:
                staywin = burstt / dlistt
                me = 21 - plus2 
                for i in stay:
                    for t in range(1,me):
                        if i + plus - deal[0] < plus2 + t:
                            hitwin1 = hitwin1 + 1
                            if t == 10:
                                hitwin1 = hitwin1 + 3
                hitwin1 = hitwin1 / dlistt / 13
                hitwin2 = (burstt + stayy) / dlistt / 13
                for w in burst:
                    for q in range(1,me):
                        hitwin3 = hitwin3 + 1
                        if q == 10:
                            hitwin3 = hitwin3 + 3
                hitwin3 = hitwin3 / dlistt / 13
                hitwin = hitwin1 + hitwin2 + hitwin3
            if plus2 == plus - deal[0]:
                staywin = burstt / dlistt
                me = 21 - plus2 
                for i in stay:
                    for t in range(1,me):
                        if i + plus - deal[0] < plus2 + t:
                            hitwin1 = hitwin1 + 1
                            if t == 10:
                                hitwin1 = hitwin1 + 3
                hitwin1 = hitwin1 / dlistt / 13
                hitwin2 = (burstt + stayy) / dlistt / 13
                for w in burst:
                    for q in range(1,me):
                        hitwin3 = hitwin3 + 1
                        if q == 10:
                            hitwin3 = hitwin3 + 3
                hitwin3 = hitwin3 / dlistt / 13
                hitwin = hitwin1 + hitwin2 + hitwin3
            if plus2 > plus - deal[0]:
                stay1 = burstt
                me = 21 - plus2
                for d in stay:
                    if d + plus - deal[0] < plus2:
                        stay1 = stay1 + 1
                print(stay1)
                staywin = stay1 / dlistt
                print(staywin)
                print(dlistt)
                print(burstt)
                print(stayy)
                for i in stay:
                    for t in range(1,me):
                        if i + plus - deal[0] < plus2 + t:
                            hitwin1 = hitwin1 + 1
                            if t == 10:
                                hitwin1 = hitwin1 + 3
                hitwin1 = hitwin1 / dlistt / 13
                hitwin2 = (burstt + stayy) / dlistt / 13
                for w in burst:
                    for q in range(1,me):
                        hitwin3 = hitwin3 + 1
                        if q == 10:
                            hitwin3 = hitwin3 + 3
                hitwin3 = hitwin3 / dlistt / 13
                hitwin = hitwin1 + hitwin2 + hitwin3
                print(staywin)
                print(hitwin)
            if staywin < hitwin:
                print("hit")
            if staywin == hitwin:
                print("hit")
            if staywin > hitwin:
                print("stay")
        if longl == 2:
            fin = 11
            if 17 - plus + deal[0] > 2:
                sta = 17 - plus + deal[0]
            else:
                sta = 2
            for y in range(sta,fin+1):
                dlist.append(y)
            if 10 in dlist:
                for x in range(0,3):
                    dlist.append(10)
            if 21 - plus + deal[0]<12:
                jack = 21 - plus + deal[0]
                for z in dlist:
                    if z < jack:
                        stay.append(z)
                    if z > jack:
                        burst.append(z)
            else:
                stay = dlist
            stayy = int(len(stay))
            burstt = int(len(burst))
            dlistt = int(len(dlist))
            if plus2 < plus - deal[0]:
                staywin = burstt / dlistt
                me = 21 - plus2 
                for i in stay:
                    for t in range(1,me):
                        if i + plus - deal[0] < plus2 + t:
                            hitwin1 = hitwin1 + 1
                            if t == 10:
                                hitwin1 = hitwin1 + 3
                hitwin1 = hitwin1 / dlistt / 13
                hitwin2 = (burstt + stayy) / dlistt / 13
                for w in burst:
                    for q in range(1,me):
                        hitwin3 = hitwin3 + 1
                        if q == 10:
                            hitwin3 = hitwin3 + 3
                hitwin3 = hitwin3 / dlistt / 13
                hitwin = hitwin1 + hitwin2 + hitwin3
            if plus2 == plus - deal[0]:
                staywin = burstt / dlistt
                me = 21 - plus2 
                for i in stay:
                    for t in range(1,me):
                        if i + plus - deal[0] < plus2 + t:
                            hitwin1 = hitwin1 + 1
                            if t == 10:
                                hitwin1 = hitwin1 + 3
                hitwin1 = hitwin1 / dlistt / 13
                hitwin2 = (burstt + stayy) / dlistt / 13
                for w in burst:
                    for q in range(1,me):
                        hitwin3 = hitwin3 + 1
                        if q == 10:
                            hitwin3 = hitwin3 + 3
                hitwin3 = hitwin3 / dlistt / 13
                hitwin = hitwin1 + hitwin2 + hitwin3
            if plus2 > plus - deal[0]:
                stay1 = burstt
                print(burstt)
                me = 21 - plus2
                for d in stay:
                    if d + plus - deal[0] < plus2:
                        stay1 = stay1 + 1
                print(stay1)
                staywin = stay1 / dlistt
                for i in stay:
                    for t in range(1,me):
                        if i + plus - deal[0] < plus2 + t:
                            hitwin1 = hitwin1 + 1
                            if t == 10:
                                hitwin1 = hitwin1 + 3
                hitwin1 = hitwin1 / dlistt / 13
                hitwin2 = (burstt + stayy) / dlistt / 13
                for w in burst:
                    for q in range(1,me):
                        hitwin3 = hitwin3 + 1
                        if q == 10:
                            hitwin3 = hitwin3 + 3
                hitwin3 = hitwin3 / dlistt / 13
                hitwin = hitwin1 + hitwin2 + hitwin3
            print("hit",hitwin,"stand",staywin)
            if staywin < hitwin:
                print("hit")
            if staywin == hitwin:
                print("hit")
            if staywin > hitwin:
                print("stay")
    return

def start():
    global p
    global db
    global mb
    global count
    global kkk
    global myca
    global deal
    global numbers
    global plus
    global plus2
    if kkk == 1:
        if p == 0:
            memo = input("무엇을 하시겠습니까?")
            if memo == 'hit':
                lo = int(len(numbers))
                mycard = numbers.pop(random.randint(0,lo-1))
                myca.append(mycard)
                if mycard == 11:
                    print("A")
                elif mycard != 11:
                    print(mycard)
                p = 1
            if memo == 'stand':
                if db == 0 and mb == 0:
                    if plus > plus2:
                        print("Lose")
                        score.append(-1)
                        print("한게임 끝")
                        count = count + 1
                        kkk = 1
                    if plus == plus2:
                        print("GG")
                        score.append(0)
                        print("한게임 끝")
                        count = count + 1
                        kkk = 1
                    if plus < plus2:
                        print("Win")
                        score.append(1)
                        print("한게임 끝")
                        count = count + 1
                        kkk = 1
                if db == 0 and mb == 1:
                    print("Lose")
                    score.append(-1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 0 and mb == 2:
                    print("Win")
                    score.append(1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 1 and mb == 0:
                    print("Win")
                    score.append(1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 1 and mb == 2:
                    print("Win")
                    score.append(1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 1 and mb == 1:
                    print("Lose")
                    score.append(-1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 2 and mb == 2:
                    print("GG")
                    score.append(0)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 2 and mb == 0:
                    print("Lose")
                    score.append(-1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                if db == 2 and mb == 1:
                    print("Lose")
                    score.append(-1)
                    print("한게임 끝")
                    count = count + 1
                    kkk = 1
                print("딜러 합:",plus)
                return
        if p == 1:
            plus = 0
            ad = int(len(deal))
            if ad == 0:
                ll = int(len(numbers))
                mycards = numbers.pop(random.randint(0,ll-1))
                deal.append(mycards)
            for i in range(0,ad):
                aaa = deal[i]
                plus = plus + aaa
            if plus <17:
                ll = int(len(numbers))
                mycards = numbers.pop(random.randint(0,ll-1))
                deal.append(mycards)
                ad = len(deal)
                start()
                return
            p = 0
        print("나의 패:", end=" ")
        g = int(len(myca))
        for t in range(0,g):
            a = myca[t]
            if t != g-1:
                if a == 11:
                    print("A", end=",")
                if a != 11:
                    print(a, end=",")
            if t == g-1:
                if a == 11:
                    print("A")
                if a != 11:
                    print(a)
        print("딜러의 패:",end=" ")
        k = int(len(deal))
        for s in range(0,k):
            if s != k-1:
                if s == 0:
                    print('?',end=",")
                if s != 0:
                    a = deal[s]
                    print(a,end=",")
            if s == k-1:
                a = deal[s]
                print(a)
        if plus > 21:
            db = 1
        if plus == 21:
            db = 2
        if plus < 21:
            db = 0
        plus2 = 0
        ad = 1
        aC = myca.count(11)
        for x in range(0,aC):
            g = int(input("A를 선택해 주세요"))
            if g == 1:
                plus2 = plus2 + 1
                print("and")
            if g == 11:
                plus2 = plus2 + 11
                print("and")
        for i in myca:
                plus2 = plus2 + i
                if i == 11:
                    plus2 = plus2 - 11
        print("내 합:",end=" ")
        print(plus2)
        if plus2 > 21:
            mb = 1
        if plus2 == 21:
            mb = 2
        if plus2 < 21:
            mb = 0
        ai()
        start()

for x in range(0,3):
    lo = int(len(numbers))
    mycard = numbers.pop(random.randint(0,lo-1))
    myca.append(mycard)
    start()
    myca = mycabackup[:]
    deal = dealbackup[:]
    print(deal)
print(score)
numbers = numbersbackup[:]
