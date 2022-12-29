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
    except socket.error as sockErr:
        print("Error: %s" % sockErr)
        exit()

    cliSocket.settimeout(None)
    print('The client has connected to the server.')
    print('Listening to server for the messages...')

    return cliSocket

def listen(cliSock):
    msg = ''
    while msg.lower().strip() != 'bye':
        msg = cliSock.recv(256).decode()
        print("Msg.:", msg)

def closeConn(cliSock):
    cliSock.close()

def mainProg():
    hostIp, hostPort = inputAddr()
    cliSock = makeConn(hostIp, hostPort)
    listen(cliSock)
    closeConn(cliSock)

if __name__ == '__main__':
    mainProg()