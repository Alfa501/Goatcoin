import socket
import threading

ip = "192.168.2.116"
port = 6969

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(i):
    sock.connect((ip, port))
    #sock.send(bytes("client", "UTF-8"))
    print("C0")
    data = sock.recv(1024)
    print("C1")
    print('Received', repr(data))
    print("C2")

def test(j):
    for k in range(j):
        clientthread = threading.Thread(target=connect, args=(j,))
        clientthread.start()