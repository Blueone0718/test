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
pl=0

def ai():
    global stay
    global dlist
    global burst
    global plus
    global plus2
    global pl
    dlist = dlistback[:]
    stay = stayback[:]
    burst = burstback[:]
    if plus2 > 20:
        pl=1
    if plus2 < 12:
        pl=0
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
            if staywin < hitwin:
                pl = 0
            if staywin == hitwin:
                pl = 0
            if staywin > hitwin:
                pl = 1
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
                me = 21 - plus2
                for d in stay:
                    if d + plus - deal[0] < plus2:
                        stay1 = stay1 + 1
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
            if staywin < hitwin:
                pl = 0
            if staywin == hitwin:
                pl = 0
            if staywin > hitwin:
                pl = 1
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
    global pl
    if kkk == 1:
        if p == 0:
            if pl==0:
                lo = int(len(numbers))
                mycard = numbers.pop(random.randint(0,lo-1))
                myca.append(mycard)
                p = 1
            if pl==1:
                if db == 0 and mb == 0:
                    if plus > plus2:
                        score.append(-1)
                        count = count + 1
                        kkk = 1
                    if plus == plus2:
                        score.append(0)
                        count = count + 1
                        kkk = 1
                    if plus < plus2:
                        score.append(1)
                        count = count + 1
                        kkk = 1
                if db == 0 and mb == 1:
                    score.append(-1)
                    count = count + 1
                    kkk = 1
                if db == 0 and mb == 2:
                    score.append(1)
                    
                    count = count + 1
                    kkk = 1
                if db == 1 and mb == 0:
                    
                    score.append(1)
                    
                    count = count + 1
                    kkk = 1
                if db == 1 and mb == 2:
                    
                    score.append(1)
                    
                    count = count + 1
                    kkk = 1
                if db == 1 and mb == 1:
                    
                    score.append(-1)
                    
                    count = count + 1
                    kkk = 1
                if db == 2 and mb == 2:
                    
                    score.append(0)
                    
                    count = count + 1
                    kkk = 1
                if db == 2 and mb == 0:
                    
                    score.append(-1)
                    
                    count = count + 1
                    kkk = 1
                if db == 2 and mb == 1:
                    
                    score.append(-1)
                    
                    count = count + 1
                    kkk = 1
                p=0
                pl=0
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
      
        if plus > 21:
            db = 1
        if plus == 21:
            db = 2
        if plus < 21:
            db = 0
        plus2 = 0
        aC = myca.count(11)
        for x in range(0,len(myca)):
           aaa  = myca[x]
           plus2 = plus2 + aaa
        for t in range(0,aC):
            if plus2 < 22:
                break
            plus2 = plus2 -10
        if plus2 > 21:
            mb = 1
        if plus2 == 21:
            mb = 2
        if plus2 < 21:
            mb = 0
        ai()
        start()
for e in range(0,200):
    for x in range(0,5):
        lo = int(len(numbers))
        mycard = numbers.pop(random.randint(0,lo-1))
        myca.append(mycard)
        start()    
        myca = mycabackup[:]
        deal = dealbackup[:]
    numbers = numbersbackup[:]

losee = score.count(-1)
winn = score.count(1)
same = score.count(0)
print(losee, winn, same)
