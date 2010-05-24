#!/usr/bin/env python

"""
An echo server that uses select to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket

SIZE = 1024

def main():
    host = ''
    port = 50050
    backlog = 5
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(5)
    input = [server]
    running = 1
    while True:
        inputready, outputready, exceptready = select.select(input,[],[])

        for s in inputready:

            if s is server:
                # handle the server socket
                client, address = server.accept()
                input.append(client)

            else:
                # handle all other sockets
                data = s.recv(SIZE)
                if data:
                    s.send(data)
                else:
                    s.close()
                    input.remove(s)
    server.close()

if __name__ == '__main__':
    main()
