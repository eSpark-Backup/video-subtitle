import socket
from threading import Thread

host = input("Enter IP address: ")
port = input("Enter port no. > 1024: ")

srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')

srvSocket.bind((host, int(port)))
print('Bind to the local port')

srvSocket.listen(5)
print('Started listening...')

addrList = []
connList = []

def connAccount(client, addr):
    addrList.append((addr))
    connList.append((client))

'New Client Thread'
def newClientSocketHandler(cli, ip):
    print('Connection accepted from:', ip)
    # print('The new client has socket id:', cli)
    msg = ''
    while True:
        msg = cli.recv(256).decode()
        if not msg:
            break
        # print('The message got for client socket:', cli)
        print(ip, "msg:", msg)
        connList[1].send(msg.encode())
    cli.close()
    connList[1].close()

while True:
    print('Waiting for the incoming connections')
    cli, ip = srvSocket.accept()
    cli.send(str.encode("Hi from server"))
    connAccount(cli, ip)
    'Start the new client thread'
    thread = Thread(target=newClientSocketHandler, args=(cli, ip))
    thread.start()