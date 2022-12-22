import socket
import tkinter as tk
import time

#Create UI main window
root = tk.Tk()
root.title("Subtitle Display")
root.geometry("1920x515");

#Create text label
text_label1 = tk.Label(root, font=("Arial", 100))
text_label1.pack()
text_label2 = tk.Label(root, font=("Arial", 100))
text_label2.pack()

def serverInit():
    # host = socket.gethostname()
    hostIp = input('Enter IP address: ')
    hostPort = input('Enter the port no. > 1024: ')
    print("Hosting on: " + hostIp + ":" + hostPort)

    serverSocket = socket.socket()
    serverSocket.bind((hostIp, int(hostPort)))
    return serverSocket

def serverListen(serverSocket):
    numOfClients = 5
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
    t_now = 0

    while True:
        
        recvData = conn.recv(chunkSize - lenOfWord).decode()
        if t_now + 1 <= time.time() :
            flag = 0
            text_label1.config(text = ' ')
            text_label2.config(text = ' ')

        if not recvData:
            break
        buffer += recvData
        
        if buffer[-1] != ' ':
            lastWord = buffer.split()[-1]
            buffer = buffer.rsplit(' ', 1)[0]
            lenOfWord = len(lastWord)

        if flag == 0:
            print(("Msg: ") + str(buffer) + ' | ')
            text_label1.config(text=buffer + ' | ')
            # root.update()
            flag = 1
            t_now = time.time()
        else:
            print('      ' + str(buffer))
            text_label2.config(text=buffer)
            # root.update()
            flag = 0

        # time.sleep(0.5)
        root.update()
        buffer = lastWord
        lastWord = ''

def mainProgram():
    serverSocket = serverInit()    
    connection = serverListen(serverSocket)
    stringProcess(connection)
    serverClose(connection)

if __name__ == '__main__':
    mainProgram()