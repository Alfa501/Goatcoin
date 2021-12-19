import socket
import threading

ip = "localhost"
port = 6969

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(i):
    sock.connect((ip, port))
    sock.send(bytes("client", "UTF-8"))
    print("C0")
    data = sock.recv(1024)
    print("C1")
    print('Received', repr(data))
    print("C2")

#for i in range(3):
#    client_thread = threading.Thread(target=connect, args=(i,))



#   import socket
#   
#   HOST = '127.0.0.1'  # The server's hostname or IP address
#   PORT = 65432        # The port used by the server
#   
#   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#       s.connect((HOST, PORT))
#       s.sendall(b'Hello, world')
#       data = s.recv(1024)
#   
#   print('Received', repr(data))