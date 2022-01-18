import socket

ip = "10.10.10.1"
port = 6969

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(i):
    sock.connect((ip, port))
    sock.send(bytes("{s}", "UTF-8").format(str(i)))
    data = sock.recv(1024)
    print('Received', repr(data))

def getBalance():
    pass

def checkAuth():
    pass

def transaction():
    pass

def createWallet():
    pass

while True:
    selection = input("[*] Get Balance: 1\n[*] Make Transaction: 2\n[*] Create Wallet: 3\n")
    if selection == "1":
        balance = getBalance(input("[*] Please enter your public key: "))
        print(balance)

    elif selection == "2":
        sender = input("[*] Sender Public Key: ")
        receiver = input("[*] Receiver Public Key: ")
        amount = input("[*] Enter amount of GTC to be sent: ")
        auth = input("[*] Sender Private Key ")

        if checkAuth(sender, auth) == True:
            currentBalance = getBalance(sender)
            print("[*] Your current balance is: {} GTC".format(currentBalance))

            if input("[*] Do you want to continue? y/n") == "y":
                transaction(sender, receiver, amount, currentBalance)
                print("[*] Your current balance is: {} GTC".format(getBalance(sender)))

            else:
                pass

        else:
            print("[*] Incorrect Key")
    elif selection == "3":
        createWallet()
    else:
        print("[*] Please choose one of the above options")