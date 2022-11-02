import socket
from sqlite3 import connect
import time
from unicodedata import numeric
import random

HOST = '127.0.0.1'
PORT = 5405
server_addr = (HOST, PORT)

sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_send.bind(('127.0.0.1', 5406))
# sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock_recv.bind(('127.0.0.1', 5406))

# mini project 1
while True:
    indata, addr = sock_send.recvfrom(2048)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    msg = indata.decode().split()
    if(msg[1]):
        outdata = 'Hello ' + str(msg[1])
        sock_send.sendto(outdata.encode(), ('127.0.0.1', 5405))
        print('proxy send ' + outdata)



