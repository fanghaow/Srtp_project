import socket
import time
# Address
HOST = '1.15.140.205' # server address
PORT = 80
request = 'Can you hear me?'
# configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connect successfully!')

# send message
while(True):
    s.sendall(request.encode())
    print('sent data :', request)
    time.sleep(0.5)
    # receive message
    # if s.recv(1024) != None:
    #     print('i get the info')
    #     break
reply  = s.recv(1024)
print ('reply is: ',reply)
# close connection
s.close()