#!/usr/bin/python
#client.py
import socket
import readline
import time
    
HOST='127.0.0.1'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

def recv_timeout(the_socket,timeout=2,recv_len=1024):
    the_socket.setblocking(0)
    total_data=b'';data=b'';begin=time.time()
    while True:
        #if you got some data, then break after wait sec
        if total_data and time.time()-begin>timeout:
            break
        #if you got no data at all, wait a little longer
        elif time.time()-begin>timeout*2:
            break
        try:
            data=the_socket.recv(recv_len)
            if data:
                total_data += data
                begin=time.time()
                if len(data) < recv_len: break
            else:
                time.sleep(0.1)
        except:
            pass
    return total_data.decode()


while True:
    cmd=input('CMD:').strip().encode()
    if len(cmd) == 0:continue
    s.sendall(cmd)
    data = recv_timeout(s)
    print('cmd:')
    print(data)
s.close()

