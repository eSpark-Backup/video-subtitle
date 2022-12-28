import socket
from threading import Thread

# Globals
numOfClients = 5
# addrList = []
connList = []

def inputAddr():
    hostIp = input("Enter IP address: ")
    hostPort = input("Enter port no. 1024: ")
    return hostIp, hostPort

def serverInit(hostIp, hostPort):
    serverSocket = socket.socket()
    serverSocket.bind((hostIp, int(hostPort)))
    print("Hosting on: " + hostIp + ":" + hostPort)
    serverSocket.listen(numOfClients)
    print("Waiting for connection request..")
    
    return serverSocket

def acceptConn(serverSocket):
    conn, addr = serverSocket.accept()
    print("Connection request from: " + str(addr))
    return conn, addr

def serverClose(conn):
    conn.close()
    print("Connection closed")

def connAccount(client, addr):
    # addrList.append((addr))
    connList.append((client))

'New Client Thread'
def newClientSocketHandler(cli, ip):
    print('Connection accepted from:', ip)
    msg = ''
    while True:
        msg = cli.recv(256).decode()
        if not msg:
            break
        print(ip, "msg:", msg)
        connList[1].send(msg.encode())

    if len(connList) != 0:
        connList.remove(cli)

def mainProg():
    hostIp, hostPort = inputAddr()
    srvSock = serverInit(hostIp, hostPort)
    while True:
        conn, addr = acceptConn(srvSock)
        connAccount(conn, addr)
        # 'Create thread for the newly connected client'
        thread = Thread(target=newClientSocketHandler, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    mainProg()