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

# mini project 2
PacketDrop = 0
PacketDelay = 0
while True:
    indata, addr = sock_send.recvfrom(2048)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    msg = indata.decode().split()
    if(msg[1]):
        if (int(msg[1])% 2 == 1):
            cnt = random.randint(1,20)
            if cnt == 1:
                time.sleep(0.1)
                print('proxy delay 100ms')
                PacketDelay = PacketDelay + 1
                outdata = 'Hello ' + str(msg[1])
                sock_send.sendto(outdata.encode(), ('127.0.0.1', 5405))
                print('proxy send ' + outdata)
            else:
                outdata = 'Hello ' + str(msg[1])
                sock_send.sendto(outdata.encode(), ('127.0.0.1', 5405))
                print('proxy send ' + outdata)
        else:
            cnt = random.randint(1,10)
            if cnt == 1:
                # drop
                # time.sleep(0.2)
                print('proxy set drop packet')
                PacketDrop = PacketDrop + 1
            else:
                outdata = 'Hello ' + str(msg[1])
                sock_send.sendto(outdata.encode(), ('127.0.0.1', 5405))
                print('proxy send ' + outdata)

    # if (int(msg[1]) == 10):
        print('proxy drop packet for: ' + str(PacketDrop))
        print('proxy delay 100ms packet for: ' + str(PacketDelay))
        # outdata = 'Hello ' + str(msg[1])
        # sock_send.sendto(outdata.encode(), ('127.0.0.1', 5405))
        # print('proxy send ' + outdata)

