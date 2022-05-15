import socket
from sys import last_traceback
#import geocoder
import threading
import hashlib
import datetime

global miner
miner = "02e494aaaee0ef3aebeff1a9d3dec738e6e04adfa1f1820c63b5fd2e6c188e67"

global last_block
global difficulty
global blockIte
blockIte = 0

difficulty = "00"

def prevBlockHash(prev_block, nonce):
    blocknonce = prev_block + str(nonce)
    blockHash = hashlib.sha256(blocknonce.encode())
    blockHash = blockHash.hexdigest()
    return blockHash

def mine(prev_block):
    # proof of work
    nonce = 0
    proof = prevBlockHash(prev_block, nonce)
    while str(proof)[0:len(difficulty)] != difficulty:
        try:
            proof = prevBlockHash(prev_block, nonce)
            nonce += 1
        except Exception:
            print("Nonce: " + nonce + "\n")
            print(Exception)
    return proof, nonce

def connection(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    client.send(bytes("Test Test", 'UTF-8'))
    response = client.recv(4096)
    client.send(bytes("difficulty", 'UTF-8'))
    difficulty = str(client.recv(4096))
    client.send(bytes("ready", 'UTF-8'))
    response = client.recv(4096)
    if response == "copy":
        last_block = client.recv(4096)
    mine(last_block)

def createBlock(sender, receiver, amount):
    # creates block w/ transaction info
    global blockIte
    hash, nonce = mine(blockIte)
    block = {"Block": blockIte, "Timestamp": str(datetime.now()), "Sender": sender, "Receiver": receiver, "Amount": amount, "Hash": hash, "Nonce": nonce}
    block = str(block)
    block = block.replace("'", '"')
    #chain.append(block)                Send block
    #output.write(block + "\n")
    print(block)
    blockIte += 1
    return