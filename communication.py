import socket
import threading

ip = "localhost"
port = 69

addressList = open("addresses.list", "a+")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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