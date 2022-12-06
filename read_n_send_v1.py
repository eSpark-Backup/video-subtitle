import socket
import random
import string
import time

def client_program():
    # host = socket.gethostname()  # for localhost
    host = 'raspberrypi.local'
    print(host)
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    print('Connected to the server')
    file_handle = open("testFile.txt", "r")
    chunk_size = 1024
       
    while True:
        chunk = file_handle.read(chunk_size)
        
        if chunk == '':
            print('end of file')
            break # end of file
        
        client_socket.send(chunk.encode())
        time.sleep(1)
                
    client_socket.close()  # close the connection
    print('Connection closed')
    file_handle.close()

if __name__ == '__main__':
    client_program()
