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

def sendMessage(clientSock):
    print('Type your message')
    message = input("Client1-> ") + ' ' # take input

    while message.lower().strip() != 'bye':
        clientSock.send(message.encode())  # send message
        message = input("Client1-> ") + ' '  # again take input

def mainProgram():
    clientSocket = connInit()
    sendMessage(clientSocket)
    connClose(clientSocket)

if __name__ == '__main__':
    mainProgram()
