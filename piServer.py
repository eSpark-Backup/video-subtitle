import socket


def server_program():
    host = '' # enter the ip of the interface 
    print(host)
    port = 5000  # initiate port no. above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    file_handle = open('my-file.txt', 'a') # check the file to be created
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        file_handle.write(data)

    conn.close()  # close the connection
    file_handle.close()

if __name__ == '__main__':
    server_program()
