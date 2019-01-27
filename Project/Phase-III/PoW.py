import math
import random, string
import sys, os
import hashlib
from datetime import datetime

if sys.version_info < (3, 6):
    import sha3

def PoW(TxBlockFileName, ChainFileName, PoWLen, TxLen):
    # Open Transaction Block
    TxBlockFile = open(TxBlockFileName, "r")
    tx_lines = TxBlockFile.readlines()
    num_transactions = len(tx_lines) / TxLen # 8

    # Create/Open Chain File
    if os.path.exists(ChainFileName) != True:
        open(ChainFileName, 'a').close()

    ChainFile = open(ChainFileName, "r+")
    chain_lines = ChainFile.readlines()
    # Read PoW of previous block (last line of chain file)
    if len(chain_lines) == 0:
        pow_prev = "First transaction."
    elif len(chain_lines) < 4:
        print "Erronous ChainFile"
        sys.exit()
    else:
        pow_prev = chain_lines[-1][:-1]

    # Calculate root-hash
    hashTree = []
    for i in range(0,num_transactions):
        transaction = "".join(tx_lines[i*TxLen:(i+1)*TxLen])
        hashTree.append(hashlib.sha3_256(transaction).hexdigest())

    t = num_transactions
    j = 0
    while (t>1):
        for i in range(j,j+t,2):
            hashTree.append(hashlib.sha3_256(hashTree[i]+hashTree[i+1]).hexdigest())
        j += t
        t = t>>1
    root_hash = hashTree[2*num_transactions-2]

    # Find a convenient hash as the proof of work
    pow_current = "dummy"
    while (pow_current[0:PoWLen] != "0" * PoWLen):
        nonce = str( random.getrandbits(128) )
        text = pow_prev + "\n" + root_hash + "\n" + str(nonce) + "\n"
        pow_current = hashlib.sha3_256(text).hexdigest()

    # Append to chain file.
    text += pow_current + "\n"

    ChainFile.write(text)
    ChainFile.close()
    TxBlockFile.close()
