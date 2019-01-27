import sys, os
import random
import DSA

def GenTxBlock(p, q, g, count):
    transactions = ""
    for i in range(0, count):
        transaction = "*** Bitcoin transaction ***\n"

        serial_number = random.getrandbits(128)
        transaction +="Serial number: " + str(serial_number)+ "\n"
        transaction += "p: " + str(p) + "\n"
        transaction += "q: " + str(q) + "\n"
        transaction += "g: " + str(g) + "\n"

        payer_alpha, payer_beta = DSA.KeyGen(p,q,g)
        payee_alpha, payee_beta = DSA.KeyGen(p,q,g)

        transaction += "Payer Public Key (beta): " + str(payer_beta) + "\n"
        transaction += "Payee Public Key (beta): " + str(payee_beta) + "\n"

        amount = random.getrandbits(10)
        transaction += "Amount: " + str(amount) + " Satoshi\n"

        (r, s) = DSA.SignGen(transaction, p, q, g, payer_alpha, payer_beta)
        transaction += "Signature (r): " + str(r) + "\n"
        transaction += "Signature (s): " + str(s) + "\n"

        transactions += transaction
    return transactions
