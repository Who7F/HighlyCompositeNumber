# Highly Factorable Numbers
# Finds the most factorable number up to the number entered
# Know bugs.  No data validation,  An upper limmit on number, ugly code.
# Progam dosn't self loop

import time


def funCount (n):
    pExpon[n] = pExpon[n] + 1

def funGen():
    xGen = 1
    for iii in range(20):
        xGen = xGen * (pPrime[iii]**pExpon[iii])
    return xGen

def funComposit():
    nComposite = 0
    for iii in range(20):
        nComposite = nComposite + (nComposite * pExpon[iii]) + pExpon[iii]
    return nComposite

def funGenRe(n):
    for iii in range(n,20):
        pExpon[iii] = 0

def funLoop(n):
    xGen = funGen()
    while xGen * pPrime[n] < (int(yGen))+1:
        funCount(n)
        xGen = funGen()
        n += 1


yGen = input ('Enter Number ')
start = time.time()
    

pExpon = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pPrime = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
nComposite = 0
nGen = 0

if int(yGen) < 2 :
    nGen = 1
        
else:
    n = 0
    while 2**(pExpon[0] + 1) < (int(yGen))+1:
        funGenRe(n+1)
        if n == 0:
            funLoop(n)
            n += 1
        elif pExpon[n] < pExpon[n-1]:
            xGen = funGen()
            if xGen * pPrime[n] < (int(yGen))+1:
                funLoop(n)
                n += 1
            else:
                n += - 1
        else:
            n += - 1
            xGen = 0
    
        if funComposit() > nComposite:
            nComposite = funComposit()
            nGen = funGen()
        elif funComposit() == nComposite:
            if nGen > funGen():
                nGen = funGen()
                nComposite = funComposit()


print (nGen)
end = time.time()
print ('Calculation time')
print (end - start)
