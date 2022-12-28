import socket

def inputAddr():
    hostIp = input("Enter IP address: ")
    hostPort = input("Enter port no. 1024: ")
    return hostIp, hostPort

def makeConn(hostIp, hostPort):
    cliSocket = socket.socket()
    cliSocket.connect((hostIp, int(hostPort)))
    print('The client has connected to the server.')

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