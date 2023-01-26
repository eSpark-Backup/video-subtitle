import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageTk, Image

import socket
import logging as log
import json
import uiUtility as uiUtils


LOG_DISABLE = 1
LOG_LEVEL = log.INFO
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

log.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
if LOG_DISABLE:
    log.disable(log.INFO)

CONN_TIMEOUT = 5
MSG_SIZE = 256
CONFIG_MSG_SIZE = 256

listenerConfig = {}

def inputListener():
    listenerId = input('Enter listener id: ')
    return listenerId

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
        
def unmarshalConfig(configMsg):
    global listenerConfig
    listenerConfig = json.loads(configMsg)

def getConfig(cliSock):
    configMsg = cliSock.recv(CONFIG_MSG_SIZE).decode('utf-8')
    unmarshalConfig(configMsg)

def setupUi():
    global listenerConfig
    window, frame = uiUtils.createWindow()
    selFont = uiUtils.fontSelection(listenerConfig)
    charLimit = uiUtils.characterLimit(frame, selFont)
    textLabel = uiUtils.createLabelText(frame, selFont)
    
    return window, charLimit, textLabel

def listen(cliSock, recvLen, window, textLabel):
    # Create an Icon to display on the bottom-right corner
    loadImg=Image.open('Logo.png')
    # Resize the image in the given (width, height)
    resizeImg=loadImg.resize((200  , 100))
    # Conver the image in TkImage
    icon =ImageTk.PhotoImage(resizeImg)
    # Create a Label Widget to display the text or Image
    label = tk.Label(window, image = icon, bg="#141312")
    label.place(relx= 1, rely = 0.9 , anchor='se')

    msg = ''
    while msg.lower().strip() != 'bye':
        msg = cliSock.recv(recvLen).decode()
        print("Msg.:", msg)
        textLabel.config(text=msg)
        window.update()

def sendIdentity(cliSock, listenerId):
    cliSock.send(listenerId.encode())
    # add failure check

def closeConn(cliSock):
    cliSock.close()
    print("\nConnection closed")