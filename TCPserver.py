#!/usr/bin/env python
import socket
def main():
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
            filename = sentence.split()[1]#get the file name

            print('--------------------------------')
            print('File Name: ')
            print(filename)#display the File name you got

            print('HTML FILE BELOW: ')
            f = open(filename[1:])
            outputdata = f.read()
            print(outputdata)

            connectionSocket.send("""HTTP/1.0 OK
            Content-Type: text/html

            <html>
            Assignment Complete!
            </html>""".encode());
            print('PROGRAM FINISHED')
            print('--------------------------------')
            connectionSocket.send('\n')
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()
            break

        except IOError:#Handle the Exception by sending error message
            print("ERROR 404 FILE NOT FOUND!")
            connectionSocket.send('ERROR 404: FILE NOT FOUND!')
            connectionSocket.close()
            break
    serverSocket.close()
if __name__ == '__main__':
    main()
