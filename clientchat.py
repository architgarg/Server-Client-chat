import socket
import sys
HOST = '98.195.68.10'   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
s.connect((HOST,PORT))
while True:
    message=raw_input('Enter Message: ')
    s.send(message)
    print('Awaiting Reply')
    reply=s.recv(1024)
    print('Received:',repr(reply))
s.close()
