#!/usr/bin/env python

"""
An echo server that can serve many clients
"""

import socket
import select
from greenlet import greenlet

SIZE = 1024

def handle_single_client(client):
    while True:
        data = client.recv(SIZE)
        if data:
            client.send(data)
        else:
            client.close()
            return

class SockWrapper(object):
    def __init__(self, client, main):
        self.client = client
        self.main = greenlet.getcurrent()

    def recv(self, size):
        return self.main.switch(False)

    def send(self, data):
        self.client.send(data)

    def close(self):
        self.main.switch(True)

def main():
    host = ''
    port = 50050
    backlog = 5
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(backlog)
    input = [server]
    handlers = {}
    while 1:
        inputready, outputready, exceptready = select.select(input,[],[])
        for s in inputready:

            if s is server:
                # handle the server socket
                client, address = server.accept()
                input.append(client)
                handler = handlers[client] = greenlet(handle_single_client)
                clientwrapper = SockWrapper(client)
                close = handler.switch(clientwrapper)
                assert not close
            else:
                close = handlers[s].switch(s.recv(SIZE))
                if close:
                    input.remove(s)
                    del handlers[s]

if __name__ == '__main__':
    main()
