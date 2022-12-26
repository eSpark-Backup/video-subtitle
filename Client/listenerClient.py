import socket

host = input("Enter IP address: ")
port = input("Enter port no. 1024: ")

clisocket = socket.socket()

clisocket.connect((host, int(port)))
print('The client has connected to the server.')
print('Server:', clisocket.recv(256).decode())
print('Listening to server for the messages...')

msg = ''
while msg.lower().strip() != 'bye':
    msg = clisocket.recv(256).decode()
    print("Msg.:", msg)

clisocket.close()