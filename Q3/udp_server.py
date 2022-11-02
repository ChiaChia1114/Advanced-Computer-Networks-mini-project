#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from sqlite3 import connect

HOST = '127.0.0.1'
PORT = 5405

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')
count = 1

while True:
    indata, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    msg = indata.decode().split()
    if(msg[1]):
        if (count == int(msg[1])):
            outdata = 'World ' + str(msg[1])
            s.sendto(outdata.encode(), ('127.0.0.1', 5407))
            print(outdata)
            count = count + 1
        else:
            count = count