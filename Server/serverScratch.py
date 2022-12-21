import socket
import os
# from _thread import *
from threading import Thread

# def serverInit():
#     # host = socket.gethostname()
#     hostIp = input('Enter IP address: ')
#     hostPort = input('Enter the port no. > 1024: ')
#     print("Hosting on: " + hostIp + ":" + hostPort)

#     serverSocket = socket.socket()
#     serverSocket.bind((hostIp, int(hostPort)))
#     numOfClients = 5
#     serverSocket.listen(numOfClients)
#     print("Waiting for connection request..")
#     return serverSocket

# def acceptConn(serverSocket):
#     conn, addr = serverSocket.accept()
#     print("Connection request from: " + str(addr))
#     return conn

# def multiThreadedClient(connection):
#     connection.send(str.encode('Server is working:'))
#     while True:
#         data = connection.recv(2048)
#         response = 'Server message: ' + data.decode('utf-8')
#         if not data:
#             break
#         connection.sendall(str.encode(response))
#     connection.close()


# def serverClose(conn):
#     conn.close()
#     print("Connection closed")

# def stringProcess(conn, servSock):
#     chunkSize = 21
#     lenOfWord = 0
#     buffer = '' * 21
#     flag = 0
#     lastWord = ''

#     while True:
#         conn = acceptConn(servSock)
#         recvData = conn.recv(chunkSize - lenOfWord).decode()
#         if not recvData:
#             break
#         buffer += recvData
        
#         start_new_thread(multiThreadedClient, (conn, ))
#         ThreadCount += 1
#         print('Thread Number: ' + str(ThreadCount))
        
#         if buffer[-1] != ' ':
#             lastWord = buffer.split()[-1]
#             buffer = buffer.rsplit(' ', 1)[0]
#             lenOfWord = len(lastWord)

#         if flag == 0:
#             print(("Msg.: ") + str(buffer) + ' | ')
#             flag = 1
#         else:
#             print('      ' + str(buffer))
#             flag = 0

#         buffer = lastWord
#         lastWord = ''

# def mainProgram():
#     serverSocket = serverInit()    
#     connection = acceptConn(serverSocket)
#     stringProcess(connection, serverSocket)
#     serverClose(connection)

# if __name__ == '__main__':
#     mainProgram()

# Global vars:
addrList = []
connList = []
numOfConn = 0
connLimit = 3

def serverInit():
    ServerSideSocket = socket.socket()
    host = input("Enter IP address: ")
    port = input("Enter port no. > 1024: ")
    try:
        ServerSideSocket.bind((host, int(port)))
    except socket.error as e:
        print(str(e))

    ServerSideSocket.listen(connLimit)
    print('Server is listening..')

    return ServerSideSocket

def connAccount(client, addr):
    addrList.append((addr))
    connList.append((client))    

def acceptConn(servSock):
    conn, addr = servSock.accept()
    numOfConn = numOfConn + 1
    return conn, addr

def ackMsg():
    msg = "This is from server.."
    for i in range(0, numOfConn):
        connList[i].sendto(msg.encode('utf-8'), addrList[i])    
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if data == "tada":
        # if not data:
            print('mic check 123')
            break
        connection.sendall(str.encode(response))
    connection.send(str.encode('random'))
    connection.close()

def mainProg():
    ThreadCount = 0
    serverSock = serverInint()
    while True:
        Client, address = serverSock.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
        if ThreadCount == 3:
            break
    serverSock.send(str.encode('random'))
    serverSock.close()

if __name__ == '__main__':
    mainProg()