#!/usr/bin/env python
import socket
serverName = '127.0.0.1'
serverPort = 80
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to recieve on port:", serverPort)
while True:
    print 'Server on!'
    connectionSocket, addr = serverSocket.accept()
    try:
        sentence = connectionSocket.recv(1024).decode()
        parser = sentence.split()[1]
        print('--------------------------------')
        print('File Name:')
        print(parser)
        print('HTML FILE BELOW: ')
        f = open(parser[1:])
        data = f.read()
        print(data)

        connectionSocket.send("""HTTP/1.0 200 OK
        Content-Type: text/html

        <html>
        <head>
        <title>Done!</title>
        </head>
        <body>
        File Found!
        </body>
        </html>""".encode());


        connectionSocket.close()
    except IOError:
        print("404 File Not Found!")
        connectionSocket.send('404 File Not Found!')
        connectionSocket.close()
        break
