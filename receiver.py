from sys import argv
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((argv[1], int(argv[2])))
serversocket.listen(1)
(clientsocket, address) = serversocket.accept()
print('accepted')

while True:
    data = clientsocket.recv(1024)
    if not data == b'':
        print(data)

clientsocket.close()
