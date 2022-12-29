import socket
import select
from threading import Thread

# Globals
numOfClients = 5
# addrList = []
connList = []
count = 1

def inputAddr():
    hostIp = input("Enter IP address: ")
    hostPort = input("Enter port no. 1024: ")
    return hostIp, hostPort

def serverInit(hostIp, hostPort):
    serverSocket = socket.socket()
    serverSocket.settimeout(5)
    try:
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

# def connAccount(srvSock, client, addr):
#     srvSock.settimeout(2)
#     try:
#         if srvSock.recv(256).decode().lower().strip() != 'sender':
#             connList.insert(0, client)
#     except srvSock.timeout as tOut:
#         # addrList.append((addr))
#         connList.insert(count, client)
#         count += 1

#     srvSock.settimeout(None)   

def connAccount(client, addr):
    connList.append(client)

# def connAccount(srvSock, client, addr):
#     # srvSock.setblocking(0)
#     try:
#         if srvSock.recv(256).decode().lower().strip() != 'sender':
#             connList.insert(0, client)
#     except:
#         # addrList.append((addr))
#         connList.insert(count, client)
#         count += 1

#     srvSock.setblocking(1)

def sendMsg(flag, connList, buffer):
    connList[flag].send(buffer.encode())

def stringProcess(conn, connList):
    chunkSize = 21
    lenOfWord = 0
    buffer = '' * 21
    flag = 1
    lastWord = ''

    while True:
        msg = conn.recv(chunkSize - lenOfWord).decode()
        if msg.lower().strip() == 'bye':
            for x in range(1, len(connList)):
                connList[x].send(msg.encode())

        if not msg:
            break
        buffer += msg
        
        if buffer[-1] != ' ':
            lastWord = buffer.split()[-1]
            buffer = buffer.rsplit(' ', 1)[0]
            lenOfWord = len(lastWord)

        if msg.lower().strip() != 'bye':
            sendMsg(flag, connList, buffer)
            flag += 1
            if flag == len(connList):
                flag = 1
        
        buffer = lastWord
        lastWord = ''

'New Client Thread'
def newClientSocketHandler(cli, ip):
    print('Connection accepted from:', ip)
    stringProcess(cli, connList)
    if len(connList) != 0:
        connList.remove(cli)

# def newClientSocketHandler(cli, ip):
#     print('Connection accepted from:', ip)
#     msg = ''
#     while True:
#         msg = cli.recv(256).decode()
#         if not msg:
#             break
#         print(ip, "msg:", msg)
#         for x in range(1, len(connList)):
#             connList[x].send(msg.encode())

#     if len(connList) != 0:
#         connList.remove(cli)

def mainProg():
    hostIp, hostPort = inputAddr()
    srvSock = serverInit(hostIp, hostPort)
    try:
        while True:
            conn, addr = acceptConn(srvSock)
            # connAccount(srvSock, conn, addr)
            connAccount(conn, addr)
            # 'Create thread for the newly connected client'
            thread = Thread(target=newClientSocketHandler, args=(conn, addr))
            thread.start()
    except KeyboardInterrupt:
        srvSock.close()

if __name__ == '__main__':
    mainProg()