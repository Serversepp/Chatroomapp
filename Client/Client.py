import socket

HOSTIP = '127.0.0.1'
HOSTPORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOSTIP, HOSTPORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))