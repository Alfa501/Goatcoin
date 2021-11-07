import os
import json
import time
import hashlib
from datetime import datetime

global miner
miner = "02e494aaaee0ef3aebeff1a9d3dec738e6e04adfa1f1820c63b5fd2e6c188e67"

output = open("cockchain", "a+")
input = open("cockchain", "r")

global blockIte
blockIte = 0
global chain

#print(input.readlines())
test = input.readlines()
chain = test
blockIte = len(chain)
print(blockIte)
print(chain)

def genesis():
    # creates the genesis block
    global blockIte
    genesis = {"Block": 0, "Receiver": "generate", "Amount": 69420, "Timestamp": str(datetime.now())}
    genesis = str(genesis)
    genesis = genesis.replace("'", '"')
    chain.append(str(genesis))
    output.write(genesis + "\n")
    blockIte += 1

def createBlock(sender, receiver, amount):
    # creates block w/ transaction info
    global blockIte
    hash, nonce = verify(blockIte)
    block = {"Block": blockIte, "Timestamp": str(datetime.now()), "Sender": sender, "Receiver": receiver, "Amount": amount, "Hash": hash, "Nonce": nonce}
    block = str(block)
    block = block.replace("'", '"')
    chain.append(block)
    output.write(block + "\n")
    print(block)
    blockIte += 1
    return

def prevBlockHash(blocknum, nonce):
    # get previous block's hash
    encoded = chain[blocknum - 1] + str(nonce)
    blockHash = hashlib.sha256(encoded.encode())
    blockHash = blockHash.hexdigest()
    return blockHash

def verify(blockite):
    # proof of work
    nonce = 0
    proof = prevBlockHash(blockite, nonce)
    while str(proof)[0:2] != "00":
        try:
            proof = prevBlockHash(blockite, nonce)
            nonce += 1
        except:
            print(nonce)
    return proof, nonce

def dumpChain():
    return chain

def end():
    output.close()
    input.close()

#createBlock(blockIte, op, opType)