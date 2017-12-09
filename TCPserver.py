#!/usr/bin/env python
import socket
#serverName = '127.0.0.1'
serverPort = 80
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The SERVER is on PORT: ' , serverPort)
while True:
    print('PROGRAM STARTED...')
    print('SERVER ON!')
    connectionSocket, addr = serverSocket.accept()
    try:
        sentence = connectionSocket.recv(1024).decode()
        parser = sentence.split()[1]#get the file name
        print('--------------------------------')
        print('File Name: ')
        print(parser)#display the File name you got
        print('HTML FILE BELOW: ')
        file = open(parser[1:])
        file_data = file.read()
        print(file_data)

        connectionSocket.send("""HTTP/1.0 OK
        Content-Type: text/html

        <html>
        <head>
        <title>Assignment Complete!</title>
        </head>
        <body>
        FILE FOUND...
        PROGRAM FINISHED
        </body>
        </html>""".encode());
        print('PROGRAM FINISHED')
        print('--------------------------------')
        connectionSocket.close()
        break

    except IOError:#Handle the Exception by sending error message
        print("ERROR 404 FILE NOT FOUND!")
        connectionSocket.send('ERROR 404: FILE NOT FOUND!')
        connectionSocket.close()
        break
