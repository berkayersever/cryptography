# Group Members: Emre Özdinçer 19398, Ece Ilayda Yenmez 17501, Berkay Ersever 19626
# Transactions.txt file created under Windows OS using Python 3.6.3

import math
import random, string
import sys, os
import hashlib
# import pdb
from datetime import datetime

if sys.version_info < (3, 6):
    import sha3

# Chain File
if os.path.exists("LongestChain.txt") == True:
    ChainFile = open("LongestChain.txt", "r")
else:
    print ("The chain file does not exist")

lines = ChainFile.readlines()
ChainLen = int(len(lines)/8)
print ("\nChain length: ", ChainLen, "\n")

Transactions = open('Transactions.txt', 'w')

# Generate new serial numbers:
for i in range(0,len(lines)):
    if (str(lines[i]).startswith("Serial number: ")):
        serial = random.getrandbits(128)
        lines[i] = "Serial number: " + str(serial) + "\n"

for i in range(0, ChainLen, 1):
    # print serial no (don't print extra line - confusing)
    # print str(lines[i*8+1])[0:-1]
    print (i)

    # read data
    base_transaction = "".join(lines[i*8:i*8+6])

    # generate hash (proof of work) and add it to the transaction
    h = ""
    while (h[0:6] != "000000"):
        nonce = random.getrandbits(128)
        full_transcation = base_transaction +  "Nonce: " + str(nonce) + "\n"
        h = hashlib.sha3_256((full_transcation).encode('utf-8')).hexdigest()

    # print "Nonce: " + str(nonce)
    # print "Proof of Work: " + str(h) + "\n"

    print (full_transcation + "Proof of Work: " + str(h) + "\n")
    Transactions.write(full_transcation + "Proof of Work: " + str(h) + "\n")

    # Update next transaction's proof of work value (if it exists)
    if (i<ChainLen-1):
        lines[(i+1)*8+5] = "Previous hash in the chain: " + str(h) + "\n"

ChainFile.close()
Transactions.close()
