import socket
import logging as log

LOG_DISABLE = 1
LOG_LEVEL = log.INFO
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

log.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
if LOG_DISABLE:
    log.disable(log.INFO)

CONN_TIMEOUT = 5
MSG_SIZE = 256

def inputAddr():
    hostIp = input("Enter server's IP address: ")
    hostPort = input("Enter server's port no.: ")
    return hostIp, hostPort

def makeConn(hostIp, hostPort):
    cliSocket = socket.socket()
    cliSocket.settimeout(CONN_TIMEOUT)
    try:
        cliSocket.connect((hostIp, int(hostPort)))
    except socket.error as sockErr:
        log.error(" %s" % sockErr)
        exit()

    cliSocket.settimeout(None)
    log.info('The client has connected to the server.')

    return cliSocket

def sendMsg(cliSock):
    cliSock.send('sender'.encode())
    print('Type your message')
    msg = ''
    while msg.lower().strip() != 'bye':
        msg = input('-> ') + ' '
        cliSock.send(msg.encode())
        
def listen(cliSock):
    msg = ''
    while msg.lower().strip() != 'bye':
        msg = cliSock.recv(MSG_SIZE).decode()
        print("Msg.:", msg)

def closeConn(cliSock):
    cliSock.close()
    print("\nConnection closed")