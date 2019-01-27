import math
import random, string
import warnings
import sys, os
import pyprimes
import hashlib
import DSA, TxGen

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def checkDSAparams(p, q, g):
    warnings.simplefilter('ignore')
    check = pyprimes.isprime(q)
    warnings.simplefilter('default')
    if check == False:
        return -1

    warnings.simplefilter('ignore')
    check = pyprimes.isprime(p)
    warnings.simplefilter('default')
    if check == False:
        return -2

    r = (p-1)%q
    if(r != 0):
        return -3

    k = (p-1)/q

    x = pow(g, k, p)
    if (x==1):
        return -4
    y = pow(g,q,p)
    if (y!=1):
        return -4

    return 0

# random.seed(3) # uncommment if you want it to generate the same random number in every run
ParamGenOn = 0   # set to 1 if you want to generate the DSA parameters
ParamTestOn = 0  # set to 1 if you want to validate the DSA parameters
KeyGenOn = 0     # set to 1 if your want to generate secret/public key pair for a user
KeyTestOn = 0    # set to 1 if you want to validate the DSA keys
SignTestOn = 0   # set to 1 if you want to test your signature generation and verification
TxGenOn = 0      # set to 1 if you want to generate a signed bitcoin transaction

# DSA parameter generation
if ParamGenOn:
    print ("DSA Parameter Generation: ")
    small_bound = 1 << 256
    large_bound = 1 << 2048

    q, p, g = DSA.DL_Param_Generator(small_bound, large_bound)

    outf = open('DSA_params.txt', 'w')
    outf.write(str(q))
    outf.write("\n")
    outf.write(str(p))
    outf.write("\n")
    outf.write(str(g))
    outf.close()
    print ("p, q, and g were written into file DSA_params.txt")

# Validation for DSA parameter generation
if ParamTestOn:
    if ParamGenOn==0:
        if os.path.exists('DSA_params.txt') == True:
            inf = open('DSA_params.txt', 'r')
            q = int(inf.readline())
            p = int(inf.readline())
            g = int(inf.readline())
            inf.close()
            print ("DSA parameters are read from file DSA_params.txt")
        else:
            print ('DSA_params.txt does not exist')
            sys.exit()

    res = checkDSAparams(p, q, g)
    if res ==0:
        print ("\nDSA parameters are OK:))")
    elif res == -1:
        print ("\nq is not prime:(:(")
        sys.exit()
    elif res == -2:
        print ("\np is not prime:(:(")
        sys.exit()
    elif res == -3:
        print ("\nq does not divide p-1:(:(")
        sys.exit()
    elif res == -4:
        print ("\ng is not generator of Gq:(:(")
        sys.exit()
    else:
        print ("\nSomething unexpected happened:(:(")
        sys.exit()

# DSA key generation
if KeyGenOn:
    if ParamGenOn==0:
        if os.path.exists('DSA_params.txt') == True:
            inf = open('DSA_params.txt', 'r')
            q = int(inf.readline())
            p = int(inf.readline())
            g = int(inf.readline())
            inf.close()
            print ("DSA parameters are read from file DSA_params.txt")
        else:
            print ('DSA_params.txt does not exist')
            sys.exit()

    (alpha, beta) = DSA.KeyGen(p, q, g)
    outf = open('DSA_skey.txt', 'w')
    outf.write(str(q)+"\n")
    outf.write(str(p)+"\n")
    outf.write(str(g)+"\n")
    outf.write(str(alpha)+"\n")
    outf.close()
    print ("Public key written into file DSA_skey.txt")

    outf = open('DSA_pkey.txt', 'w')
    outf.write(str(q)+"\n")
    outf.write(str(p)+"\n")
    outf.write(str(g)+"\n")
    outf.write(str(beta)+"\n")
    outf.close()
    print ("Public key written into file DSA_pkey.txt")

# DSA key validation
if KeyTestOn:
    if KeyGenOn==0:
        if os.path.exists('DSA_pkey.txt') == True and os.path.exists('DSA_skey.txt') == True:
            skeyFile = open('DSA_skey.txt', 'r')
            q = int(skeyFile.readline())
            p = int(skeyFile.readline())
            g = int(skeyFile.readline())
            alpha = int(skeyFile.readline())
            skeyFile.close()
            print ("Public key is read from DSA_skey.txt")

            pkeyFile = open('DSA_pkey.txt', 'r')
            lines = pkeyFile.readlines()
            beta = int(lines[3])
            pkeyFile.close()
            print ("Public key is read from DSA_pkey.txt")

        else:
            print ('DSA_skey.txt or DSA_pkey.txt does not exist')
            sys.exit()

    if beta == pow(g, alpha, p):
        print ("Public and secret keys are good:))")
    else:
        print ("Public and secret keys are NOT good:((")
        sys.exit()

# Validate the signature generation and verification functions for randomly generated message m
if SignTestOn:
    if KeyGenOn == 0:
        if os.path.exists('DSA_pkey.txt') == True and os.path.exists('DSA_skey.txt') == True:
            skeyFile = open('DSA_skey.txt', 'r')
            q = int(skeyFile.readline())
            p = int(skeyFile.readline())
            g = int(skeyFile.readline())
            alpha = int(skeyFile.readline())
            skeyFile.close()
            print ("Public key is read from DSA_skey.txt")

            pkeyFile = open('DSA_pkey.txt', 'r')
            lines = pkeyFile.readlines()
            beta = int(lines[3])
            pkeyFile.close()
            print ("Public key is read from DSA_pkey.txt")

        else:
            print ('DSA_skey.txt or DSA_pkey.txt does not exist')
            sys.exit()

    # pick a random message (string)
    m = random_string(random.randint(1,100))
    print ("message: ", m)
    (r, s) = DSA.SignGen(m, p, q, g, alpha, beta)
    print ("Signature:")
    print ("r: ", r)
    print ("s: ", s)

    if DSA.SignVer(m, r, s, p, q, g, beta)==1:
        print ("Signature verifies:))")
    else:
        print ("Signature does not verify:((")
        sys.exit()

# Generate a random transaction along with its signature
if TxGenOn:
    if KeyGenOn == 0:
        if os.path.exists('DSA_pkey.txt') == True and os.path.exists('DSA_skey.txt') == True:
            skeyFile = open('DSA_skey.txt', 'r')
            q = int(skeyFile.readline())
            p = int(skeyFile.readline())
            g = int(skeyFile.readline())
            alpha = int(skeyFile.readline())
            skeyFile.close()
            print ("Public key is read from DSA_skey.txt")

            pkeyFile = open('DSA_pkey.txt', 'r')
            lines = pkeyFile.readlines()
            beta = int(lines[3])
            pkeyFile.close()
            print ("Public key is read from DSA_pkey.txt")

        else:
            print ('DSA_skey.txt or DSA_pkey.txt does not exist')
            sys.exit()


    transaction=TxGen.GenSingleTx(p, q, g, alpha, beta)
    TxFile = open("SingleTransaction.txt", "w")
    TxFile.write(transaction)
    TxFile.close()
    print ("Transaction is written into SingleTransaction.txt")
