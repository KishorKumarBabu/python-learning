import socket
c=socket.socket()
c.connect(('localhost',8888))
name=input('enter a name')
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())