#!/usr/bin/python
#server.py
import socketserver
import os
class MyTCP(socketserver.BaseRequestHandler):
    def handle(self):
        print('Connect:',self.request)
        print('Addr:',self.client_address)
        while True:
            self.data=self.request.recv(1024).strip().decode()
            #print(self.data)
            if self.data == 'quit' or not self.data:break
            
            #cmd=os.popen(self.data).read()
            #if cmd == '':cmd= self.data + ': Command not found'
            cmd='一1'*256
            self.request.sendall(cmd.encode())
if __name__ == '__main__':
    HOST,PORT = '127.0.0.1',50007
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCP)
    server.serve_forever()


