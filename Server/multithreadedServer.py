import socket
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
    except socket.error as sockErr:
        print("Error: %s" % sockErr, "Please try another port.")
        exit()
        
    serverSocket.settimeout(None)
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

def connAccount(ind, client):
    connList.insert(ind, client)

def sendMsg(node, connList, buffer):
    connList[node].send(buffer.encode())

def stringProcess(conn, connList):
    chunkSize = 21
    lenOfWord = 0
    buffer = '' * 21
    node = 1
    lastWord = ''

    while True:
        msg = conn.recv(chunkSize - lenOfWord).decode()
        if msg.lower().strip() == 'bye':
            for x in range(1, len(connList)):
                sendMsg(x, connList, msg)

        if not msg:
            break
        buffer += msg
        
        if buffer[-1] != ' ':
            lastWord = buffer.split()[-1]
            buffer = buffer.rsplit(' ', 1)[0]
            lenOfWord = len(lastWord)

        if msg.lower().strip() != 'bye':
            sendMsg(node, connList, buffer)
            node += 1
            if node == len(connList):
                node = 1
        
        buffer = lastWord
        lastWord = ''

'New Client Thread'
def newClientSocketHandler(cli, ip):
    print('Connection accepted from:', ip)
    stringProcess(cli, connList)
    if len(connList) != 0:
        connList.remove(cli)

def identifySender(conn, addr):
    try:
        msg = conn.recv(20).lower().strip().decode()
        if msg == 'sender':
            print('Connection accepted from sender:', addr)
            return 0
    except socket.error as sockErr:
        print('Error: %s' % sockErr)
        return 1
        
def mainProg():
    hostIp, hostPort = inputAddr()
    srvSock = serverInit(hostIp, hostPort)
    idx = 1
    sender_id = 1

    try:
        while True:
            conn, addr = acceptConn(srvSock)
            conn.settimeout(5)
            sender_id = identifySender(conn, addr)
            conn.settimeout(None)
            if sender_id != 0:
                connAccount(idx, conn)
            else:
                connAccount(sender_id, conn)
            idx += 1
            'Create thread for the newly connected client'
            thread = Thread(target=newClientSocketHandler, args=(conn, addr))
            thread.start()
            print(connList)
    except KeyboardInterrupt:
        srvSock.close()
        print('')

if __name__ == '__main__':
    mainProg()