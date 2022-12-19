import socket

def server_program():
    # get the hostname
    # host = socket.gethostname()
    host = ''
    print (host)
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print ("Connection from: " + str(address))
    chunkSize = 21
    lenOfWord = 0
    data1 = ''
    flag = 0
    lastWord = ''
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        recvData = conn.recv(chunkSize - lenOfWord).decode()
        if not recvData:
            break
        data1 += recvData + ' '
        if data1[-1] != ' ':
            lastWord = data1.split()[-1]
            data1 = data1.rsplit(' ', 1)[0]
            lenOfWord = len(lastWord)
        if flag == 0:
            print ("from connected user: " + str(data1), end='')
            flag = 1
        else:
            print (" | " + str(data1))
            flag = 0

        data1 = lastWord
        lastWord = ''

    conn.close()  # close the connection
    print ('Connection closed')

if __name__ == '__main__':
    server_program()
