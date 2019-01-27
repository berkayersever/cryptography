import random

small_primes = [2, 3, 5, 7, 11, 13, 17]

def BasicTest(n, q, k):
    a = random.randint(2, n-1)
    x = pow(a, q, n)
    if x == 1 or x == n-1:
            return 1
    for i in range(1, k):
        x = pow(x,2,n)
        if x == 1:
            return -1
        if x == n-1:
            return 1
    return -1

def MRTest(n, t):
    k = 0
    q = n-1
    while (q % 2==0):
        q = q//2
        k+=1
    while (t>0):
        t = t-1
        if BasicTest(n, q, k)==1:
            continue
        else:
            return -1
    return 1

def PrimalityTest(n,t):
    for i in small_primes:
        if n % i==0:
            return -1
    else:
        MRTest(n, t)


result = -1
while (result == -1):
    # n = random.randint(3, 2**512)
    n = random.getrandbits(256)
    while (n % 2 == 0):
        n = random.getrandbits(256)
    result = MRTest(n,20)

print ("n: ", n)
