import socket
from threading import *
from tkinter import *

root=Tk()
root.title("chat")
e= Entry(root, width=50 , bg="Black" ,fg="white",borderwidth=10)
import socket
from threading import *
from tkinter import *
root=Tk()
root.title("chat")

a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="127.0.0.1"
port = 5000

a.connect((ip,port))
print("connected")

while 1:
    recv_msg =a.recv(1024)
    recv_msg =recv_msg.decode()
    print(recv_msg)
    msg = input("Enter your Message: ")
    msg = msg.encode()
    a.send(msg)

