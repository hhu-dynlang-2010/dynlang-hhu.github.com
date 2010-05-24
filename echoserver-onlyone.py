#!/usr/bin/env python

"""
An echo server that can only serve one client at a time
"""

import socket

SIZE = 1024

def handle_single_client(client):
    while True:
        data = client.recv(SIZE)
        if data:
            client.send(data)
        else:
            client.close()
            return

def main():
    host = ''
    port = 50050
    backlog = 5
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(backlog)
    while 1:
        client, address = s.accept()
        running = 1
        handle_single_client(client)

if __name__ == '__main__':
    main()
