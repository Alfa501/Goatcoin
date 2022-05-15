import os
import json
import time
import hashlib
from datetime import datetime

output = open("cockchain", "a+")
input = open("cockchain", "r")

global blockIte
blockIte = 0
global chain

#print(input.readlines())
test = input.readlines()
chain = test
blockIte = len(chain)

#print(blockIte)
#print(chain)

################# Full Node #################
def genesis():
    # creates the genesis block
    global blockIte
    genesis = {"Block": 0, "Receiver": "generate", "Amount": 69420, "Timestamp": str(datetime.now())}
    genesis = str(genesis)
    genesis = genesis.replace("'", '"')
    chain.append(str(genesis))
    output.write(genesis + "\n")
    blockIte += 1


################# Mining Node #################
#def createBlock(sender, receiver, amount):
#    creates block w/ transaction info
#   global blockIte
#   hash, nonce = verify(blockIte)
#   block = {"Block": blockIte, "Timestamp": str(datetime.now()), "Sender": sender, "Receiver": receiver, "Amount": amount, "Hash": hash, "Nonce": nonce}
#   block = str(block)
#   block = block.replace("'", '"')
#   #chain.append(block)                Send block
#   output.write(block + "\n")
#   print(block)
#   blockIte += 1
#   return

################# Mining Node #################
#def prevBlockHash(blocknum, nonce):
#   encoded = chain[blocknum - 1] + str(nonce)
#   blockHash = hashlib.sha256(encoded.encode())
#   blockHash = blockHash.hexdigest()
#   return blockHash

################# Mining Node #################
#def verify(blockite):
#   # proof of work
#   nonce = 0
#   proof = prevBlockHash(blockite, nonce)
#   while str(proof)[0:2] != "00":
#       try:
#           proof = prevBlockHash(blockite, nonce)
#           nonce += 1
#       except:
#           print(nonce)
#   return proof, nonce

################# Frontend #################
def dumpChain():
    return chain

def end():
    output.close()
    input.close()

#createBlock(blockIte, op, opType)