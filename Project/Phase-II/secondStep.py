# from Crypto.Util import number pythonhosted.org/pycrypto
from math import log2
# import math
import random, string
import warnings
import sys, os
import pyprimes
import hashlib

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
        # print(t)
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
    q = random.getrandbits(256)
    while ((q % 2 == 0) | (log2(q) < 255)):
        q = random.getrandbits(256)
    result = MRTest(q,20)
    print(log2(q))

print ("q: ", q)

# p = k*q + 1
result = -1
while (result == -1):
    k = random.randrange(2**1792, 2**1793, 2)
    while ((log2(k*q + 1) < 2047) | (log2(k*q + 1) >= 2048)):
        k = random.randrange(2**1792, 2**1793, 2)
    result = MRTest((k*q + 1),20)
    print(log2(k))
    print(log2(k*q + 1))
print ("p: ", k*q + 1)
print ("q: ", q)


# Sorulması Gereken Kısımların Başlangıcı
p = k*q + 1
a = random.randint(2, p)        # (2, q)
g = pow(a, k, p)                # (a, q, p)
while ((g % p) == 1):
    counter = 0
    a = random.randint(2, p)    # (2, q)
    g = pow(a, k, p)
    print("Counter: ", counter)
    counter += 1
print("g mod p: ", (g % p))
print("g: ", g)

test = pow(g, 1, p)
print("test:", test)

# Key Generation
b = pow(g, a, p)    # Beta

# Signature Generation
# print "message: ", m

def genSignature(q, p, g, a):
    m = random_string(random.randint(1,100))
    h = hashlib.sha3_256((m).encode('utf-8')).hexdigest()
    h = h % q
    k = random.randrange(0, q)
    r = pow(g, k, n) % q
    s = ((a * r) + (k * h)) % q
    return r, s
