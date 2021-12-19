#from os import popen
import socket
import threading
import miner

ip = "localhost"
port = 6969

addressList = open("addresses.list", "a+")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

global unvalidated
unvalidated = []

def mining():
    print("[*] Mining Node mode")
    

def full():
    print("[*] Full Node mode")
    server.bind((ip,port))
    server.listen(5)

def super():
    print("[*] Super Node mode")
    server.bind((ip,port))
    print("S6")
    server.listen(5)
    print("S7")
    listen()
    #listener_thread = threading.Thread(target=listen)

def clientHandler(client):
    print("S0")
    request = client.recv(1024)
    print("S1")
    print("[*] Received: " + str(request))
    print("S3")
    client.send(bytes("platzhalter", 'UTF-8'))
    print("S8")
    client.close()
    print("S9")
    return

def listen():
    print("S4")
    while True:
        client,address = server.accept()
        print("S5")
        print("[*] Accepted Connection from: " + str(address[0]) + " " + str(address[1]))
        client_thread = threading.Thread(target=clientHandler, args=(client,))
        client_thread.start()