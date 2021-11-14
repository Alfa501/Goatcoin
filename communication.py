#from os import popen
import socket
import threading
import miner

ip = "localhost"
port = 69

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
    server.listen(5)
    listener_thread = threading.Thread(target=listen)

def clientHandler(client):
    request = client.recv(1024)
    print("[*] Received: " + str(request))
    client.send(bytes("platzhalter", 'UTF-8'))
    client.close()

def listen():
    while True:
        client,address = server.accept()
        print("[*] Accepted Connection from: " + str(address[0]) + " " + str(address[1]))
        client_thread = threading.Thread(target=clientHandler, args=(client,))
        client_thread.start()
        return