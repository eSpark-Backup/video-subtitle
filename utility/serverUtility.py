import socket
from threading import Thread
import logging as log
import json
import uiUtility as uiUtils

LOG_DISABLE = 1
LOG_LEVEL = log.INFO
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

log.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
if LOG_DISABLE:
    log.disable(log.INFO)

# Globals
SERVER_SOCK_TIMEOUT = 5
# addrList = []
numOfClients = 0
connList = []
msgLen = 0
# configHolder = {"fontSize": fontSize, "fontType": fontType, "fontColor": fontColor, "fontStyle": fontStyle, "fontWeight": fontWeight}
configHolder = {}

def inputAddr():
    hostIp = input("Enter IP address: ")
    hostPort = input("Enter port no. 1024: ")
    return hostIp, hostPort

def getClients():
    global connList
    numOfClients = input("Enter no. of clients: ")
    connList = [socket.socket()] * int(numOfClients)
    # return connList

def serverInit(hostIp, hostPort):
    serverSocket = socket.socket()
    serverSocket.settimeout(SERVER_SOCK_TIMEOUT)
    try:
        serverSocket.bind((hostIp, int(hostPort)))
    except socket.error as sockErr:
        log.error(" %s" % sockErr)
        exit()
        
    serverSocket.settimeout(None)
    log.info(" Hosting on: " + hostIp + ":" + hostPort)
    serverSocket.listen(numOfClients)
    log.info(" Waiting for connection request..")
    
    return serverSocket

def acceptConn(serverSocket):
    conn, addr = serverSocket.accept()
    log.info(" Connection request from: " + str(addr))
    return conn, addr

def serverClose(srvSock):
    srvSock.close()
    print("\nServer closed")

def connAccount(ind, client):
    connList[ind] = client

def sendMsg(node, connList, buffer):
    _, port = connList[node].getsockname()
    if port != 0:
        connList[node].send(buffer.encode())

def stringProcess(conn, connList):
    global msgLen
    chunkSize = msgLen
    print('chunkSize: ', chunkSize)
    lenOfWord = 0
    buffer = '' * int(chunkSize)
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

        'Do not send the message when no listener is found.'
        if len(connList) > 1:
            if msg.lower().strip() != 'bye':
                sendMsg(node, connList, buffer)
                node += 1
                if node == len(connList):
                    node = 1
        
        buffer = lastWord
        lastWord = ''

def getConfigs():
    fontSize = input('Enter font size: ')
    fontType = input('Enter font type: ')
    fontColor = input('Enter font color: ')
    fontStyle = input('Enter font style: ')
    fontWeight = input('Enter font weight: ')

    return fontSize, fontType, fontColor, fontStyle, fontWeight

def createConfig(fontSize, fontType, fontColor, fontStyle, fontWeight):
    global configHolder
    configHolder = {"fontSize": fontSize, "fontType": fontType, "fontColor": fontColor, "fontStyle": fontStyle, "fontWeight": fontWeight}
   
def setupConfig():
    fontSize, fontType, fontColor, fontStyle, fontWeight = getConfigs()
    createConfig(fontSize, fontType, fontColor, fontStyle, fontWeight)
   
def getMsgLen():
    global configHolder
    global msgLen

    window, frame = uiUtils.createWindow()
    selFont = uiUtils.fontSelection(configHolder)
    msgLen = uiUtils.characterLimit(frame, selFont)
    uiUtils.destroyWindow(window)
    
def createJson(configHolder):
    jsonObj = json.dumps(configHolder)
    return jsonObj

def sendConfigMsg(cli):
    global configHolder
    jsonObj = createJson(configHolder)
    cli.send(jsonObj.encode())

'New Client Thread'
'Pass the output of getMsgLen()'
def newClientSocketHandler(cli, ip, idx):
    log.info(' Connection accepted from:' + str(ip))
    # sendConfigMsg(cli)
    stringProcess(cli, connList)
    cli.close()
    connList[idx] = socket.socket()

def identifySender(conn, addr):
    try:
        msg = conn.recv(20).lower().strip().decode()
        if msg == 'sender':
            log.debug(' Connection accepted from sender:' + str(addr))
            return 0
    except socket.error as sockErr:
        log.error(' %s' % sockErr)
        return -1

def switchCase(msg):
    if msg == '1':
        return 1
    elif msg == '2':
        return 2
    elif msg == '3':
        return 3
    elif msg == '4':
        return 4
    else:
        return -1

def identifylistener(conn, addr):
    try:
        msg = conn.recv(20).lower().strip().decode()
        case = switchCase(msg)
        # log.debug(' Connection accepted from listener:' + str(addr))
        return case
    except socket.error as sockErr:
        log.error(' %s' % sockErr)
        return -1
