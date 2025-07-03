import socket
from threading import *

a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="127.0.0.1"
port = 5000

a.bind((ip,port))
a.listen(1)
connection,addr=a.accept()

print("connected")

while 1:
    msg = input("Enter your Message: ")
    msg = msg.encode()
    connection.send(msg)
    recv_msg =connection.recv(1024)
    recv_msg =recv_msg.decode()
    print(recv_msg)
