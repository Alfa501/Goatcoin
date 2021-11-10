import json
import socket
import geocoder
import threading

#def location():
#    location = geocoder.ip("me").country
#    print("[*] Location: " + str(location))

def connection(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    client.send(bytes("Test Test", 'UTF-8'))
    response = client.recv(4096)
    return response



    #def getBalance(sender):
    #balance = 0
    #chain = cc.dumpChain()
    #for block in chain:
    #    block = json.loads(str(block))
    #    if "Receiver" in block:
    #        if block["Receiver"] == sender:
    #            balance += block["Amount"]
    #for block in chain:
    #    block = json.loads(block)
    #    if "Sender" in block:
    #        if block["Sender"] == sender:
    #            balance -= block["Amount"]
    #return balance