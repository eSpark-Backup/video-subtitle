import socket

def connInit():
    hostIp = input('Enter IP of the server: ')
    hostPort = input('Enter the port: ')

    print('Establishing connection')
    clientSocket = socket.socket()  # instantiate
    clientSocket.connect((hostIp, int(hostPort)))  # connect to the server
    print('Connection established')

    return clientSocket

def connClose(clientSock):
    clientSock.close()  # close the connection

def recvMessage(clientSock):
    msg = ''
    while True:
        # if not msg:
        if msg == 'random':
            print('Check')
            break
        msg = clientSock.recv(21).decode()  # send message
        print("msg.: " + msg)

def mainProgram():
    clientSocket = connInit()
    recvMessage(clientSocket)
    connClose(clientSocket)

if __name__ == '__main__':
    mainProgram()
