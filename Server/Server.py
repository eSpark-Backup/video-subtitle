import socket

def serverInit():
    # host = socket.gethostname()
    hostIp = input('Enter IP address: ')
    hostPort = input('Enter the port no. > 1024: ')
    print("Hosting on: " + hostIp + ":" + hostPort)

    serverSocket = socket.socket()
    serverSocket.bind((hostIp, int(hostPort)))
    return serverSocket

def serverListen(serverSocket):
    numOfClients = 1
    serverSocket.listen(numOfClients)
    print("Waiting for connection request..")
    conn, addr = serverSocket.accept()
    print("Connection request from: " + str(addr))
    return conn

def serverClose(conn):
    conn.close()
    print("Connection closed")

def stringProcess(conn):
    chunkSize = 21
    lenOfWord = 0
    buffer = '' * 21
    flag = 0
    lastWord = ''

    while True:
        recvData = conn.recv(chunkSize - lenOfWord).decode()
        if not recvData:
            break
        buffer += recvData
        
        if buffer[-1] != ' ':
            lastWord = buffer.split()[-1]
            buffer = buffer.rsplit(' ', 1)[0]
            lenOfWord = len(lastWord)

        if flag == 0:
            print(("Msg.: ") + str(buffer) + ' | ')
            flag = 1
        else:
            print('      ' + str(buffer))
            flag = 0

        buffer = lastWord
        lastWord = ''

def mainProgram():
    serverSocket = serverInit()    
    connection = serverListen(serverSocket)
    stringProcess(connection)
    serverClose(connection)

if __name__ == '__main__':
    mainProgram()