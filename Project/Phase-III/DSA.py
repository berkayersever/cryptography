# from Crypto.Util import number pythonhosted.org/pycrypto
from math import log
import random, string
import sys, os
import pyprimes
import hashlib

if sys.version_info < (3, 6):
    import sha3

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# def SignGen(message, p, q):
def SignGen(m, p, q, g, alpha, beta):
    # print "DSA: Generating signature..."
    h = hashlib.sha3_256(m).hexdigest()
    h = int(h,16)
    h = h % q

    k = random.randint(0, q)
    r = pow(g, k, p) % q

    s = ((alpha * r) + (k * h)) % q

    # print "r: ", r
    # print "s: ", s

    return r, s

def SignVer(m, r, s, p, q, g, beta):
    # print "DSA: Verifying signature..."
    h = hashlib.sha3_256(m).hexdigest()
    h = int(h,16)
    h = h % q
    v = modinv(h,q)

    z1 = (s*v) % q
    z2 = ((q - r) * v) % q

    factor1 = pow (g,z1,p)
    factor2 = pow (beta,z2,p)
    u = (factor1 * factor2) % p

    # print "u: ", u
    # print "z1: ", z1
    # print "z2: ", z2

    if (r == u % q):
        return 1
    else:
        return -1

def DL_Param_Generator(small_bound, large_bound):
    # print "DSA: Generating parameters..."
    # 1. Choose a random prime q.
    if ( (log(small_bound,2) == 256) and (log(large_bound,2) == 2048) ):
        small_bound = 256
        large_bound = 2048
    else:
        print "ERROR: small and large bounds are not 256-bit and 2048-bit, respectively"
        return

    result = -1
    while (result == -1):
        q = random.randint(2**(small_bound-1), 2**small_bound)
        result = MRTest(q,20)
    # print "q: ", q

    # 2. Find prime p such that q divides (p - 1)
    result = -1
    bit_dif = large_bound - small_bound
    while (result == -1):
        p = 1 # dummy
        # find 2048-bit p
        while ((log(p,2) < large_bound-1 ) or (log(p,2) >= large_bound)):
            k = random.randrange(2**(bit_dif-1), 2**bit_dif, 2)
            p = k*q + 1
        result = MRTest((p),30)
    # print "p: ", p
    # # print "k: ", k # debug

    a = random.randint(2, p)

    g = pow(a, k, p)
    while ((g % p) == 1):
        a = random.randint(2, p)
        g = pow(a, k, p)
    # print "g: ", g
    # print "Right-hand-side must be 1: " , pow(g,q,p) # debug

    return q,p,g

def KeyGen(p, q, g):
    # print "DSA: Generating keys..."
    alpha = random.randint(2, p)
    beta = pow(g, alpha, p)
    return alpha, beta

# def GetSignatures(transaction):
#     small_bound = 1 << 256
#     large_bound = 1 << 2048
#     q,p,g = DL_Param_Generator(small_bound,large_bound)
#     alpha, beta = KeyGen(p, q, g)
#
#     (r, s) = SignGen(transaction, p, q, g, alpha, beta)
#     return r,s
