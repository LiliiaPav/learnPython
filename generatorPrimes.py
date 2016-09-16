def genPrimes():
    primeList=[2]
    new=3
    memor=2
    while True:
        for i in primeList:
            if new%i==0:
                break
        else:
            yield memor
            memor=new
        if memor not in primeList:
            primeList.append(memor)
        new+=1
    #return primeList

for i in genPrimes():
    print i