import socket
import sys
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print ('Socket bind complete')
s.listen(10)
print ('Socket now listening')
conn,addr=s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))
while True:
    data=conn.recv(1024)
    print('Received',repr(data))
    reply=raw_input('Reply: ')
    conn.sendall(reply)
conn.close
