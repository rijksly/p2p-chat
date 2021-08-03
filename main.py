from sys import argv
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((argv[1], int(argv[2])))
print('connected')

s.send(bytes('Hello, world', encoding = 'UTF-8'))

s.close()
