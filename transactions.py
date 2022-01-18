import json
import random
import hashlib
import cockchain as cc

def verifypass(pass1, pass2):
	if pass1 == pass2:
		return True

def createWallet():                                         # improve security, easy to brute force | (hash of random string + salt) hashed twice
	key = ""                                                # check blockchain whether key already exists
	for i in range(0,64):
		if random.randint(0,1) == 0:
			key += chr(random.randint(97, 122))
		elif random.randint(0,1) == 1:
			key += chr(random.randint(48, 57))
	passphrase = input("[*] Enter a passphrase: ")
	passphrase1 = input("[*] Repeat passphrase: ")
	if verifypass(passphrase, passphrase1):
		key += passphrase
		key = hashlib.sha256(str(key).encode()).hexdigest()
	else:
		return
	print("[*] Your Private Key: " + str(key))  # write keys to key file 
	hash = hashlib.sha256(str(key).encode()).hexdigest()
	print("[*] Your Public Key: " + str(hash))

def getBalance(sender):
    balance = 0
    chain = cc.dumpChain()
    for block in chain:
        block = json.loads(str(block))
        if "Receiver" in block:
            if block["Receiver"] == sender:
                balance += block["Amount"]
    for block in chain:
        block = json.loads(block)
        if "Sender" in block:
            if block["Sender"] == sender:
                balance -= block["Amount"]
    return balance

def transaction(sender, receiver, amount, balance):
    if int(balance) > int(amount):
        cc.createBlock(sender, receiver, int(amount))
    elif int(balance) < int(amount):
        print("[*] Not enough GTC for this transaction")
        

def checkAuth(publicKey, privateKey):
    publicKeyGenerated = hashlib.sha256(str(privateKey).strip().encode()).hexdigest()
    print(publicKeyGenerated, publicKey)
    if publicKeyGenerated == publicKey:
        return True