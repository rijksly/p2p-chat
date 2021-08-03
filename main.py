from sys import argv
import socket

def init_send_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    print('send socket connected')

    return s

def init_accept_socket(ip, port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip, int(port)))
    serversocket.listen(1)
    (clientsocket, address) = serversocket.accept()
    print('accept socket connected')

    return clientsocket

read_or_write = input('Would you like to send (s) or to receive (r)?: ')

if read_or_write == 's':
    send = init_send_socket(argv[1], argv[2])

    message = input('Message: ')
    send.send(bytes(message, encoding = 'UTF-8'))
elif read_or_write == 'r':
    receive = init_accept_socket(argv[1], argv[3])

    while True:
        data = receive.recv(1024)
        if not data == b'':
            print(data.decode())
            break

if read_or_write == 's':
    send.close()
elif read_or_write == 'r':
    receive.close()
