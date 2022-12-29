import socket

def inputAddr():
    hostIp = input("Enter IP address: ")
    hostPort = input("Enter port no. 1024: ")
    return hostIp, hostPort

def makeConn(hostIp, hostPort):
    cliSocket = socket.socket()
    cliSocket.settimeout(5)
    try:
        cliSocket.connect((hostIp, int(hostPort)))
    except cliSocket.error as sockErr:
        print("Error: %s" % sockErr)
        exit()

    print('The client has connected to the server.')
    # cliSocket.send('sender'.encode())

    return cliSocket

def sendMsg(cliSock):
    print('Type your message')
    msg = ''
    while msg.lower().strip() != 'bye':
        msg = input('-> ') + ' '
        cliSock.send(msg.encode())

def closeConn(cliSock):
    cliSock.close()

def mainProg():
    hostIp, hostPort = inputAddr()
    cliSock = makeConn(hostIp, hostPort)
    sendMsg(cliSock)
    closeConn(cliSock)

if __name__ == '__main__':
    mainProg()