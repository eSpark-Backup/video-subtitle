import socket

host = input("Enter IP address: ")
port = input("Enter port no. 1024: ")

clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clisocket.connect((host, int(port)))
print('The client has connected to the server')
print('Server:', clisocket.recv(256).decode())
print('Type your message:')

msg = ''
while msg.lower().strip() != 'bye':
    msg = input('-> ')
    clisocket.send(msg.encode())

clisocket.close()