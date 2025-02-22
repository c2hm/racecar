#!/usr/bin/env python
from socket import *
import struct

format_UDP= ">fffI"

# This process should listen to a different port than the PositionBroadcast client.
PORT = 65431

client = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP) #UDP
client.setsockopt(SOL_SOCKET, SO_BROADCAST,1)

client.bind(("", PORT)) # connect to server (block until accepted)

while True:
    data, addr = client.recvfrom(1024)
    data = struct.unpack(format_UDP, data)
    print('x: '+ str(data[0]) +' y: '+ str(data[1]) +' Theta: '+ str(data[2]) +'ID: '+ hex(data[3]))