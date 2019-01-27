import math
import random, string
import sys, os
import hashlib

if sys.version_info < (3, 6):
    import sha3

def ValidateChain(ChainFileName, PoWLen, TxLen):
    if os.path.exists(ChainFileName) == True:
        ChainFile = open(ChainFileName, "r")
    else:
        return -2

    lines = ChainFile.readlines()
    ChainLen = int(len(lines)/TxLen)
    # print(len(lines), TxLen, ChainLen)
    print ("\nChain length: ", ChainLen, "\n")

    valid = True
    for i in range(0, ChainLen, 1):
        transaction = "".join(lines[i*TxLen:i*TxLen+TxLen-1])
        h = hashlib.sha3_256((transaction).encode('utf-8')).hexdigest()
        PoW = lines[i*TxLen+TxLen-1]
        print ("h: ", h)
        print (PoW)
        if (h != PoW[15:-1]):
            valid = False
            break
    ChainFile.close()
    if valid == True:
        return 1
    else:
        return -1

print ("Chain Validation:")

# Chain File
PoWLen = 6
TxLen = 8
retVal = ValidateChain("LongestChain.txt", PoWLen, TxLen)
if retVal == 1:
    print ("\n\nHash chain validated:):)")
elif retVal == -1:
    print ("\n\nValidation Fails!!!!")
elif retVal == -2:
    print ("The chain file does not exist")
else:
    print (" Something unexpected happened")
