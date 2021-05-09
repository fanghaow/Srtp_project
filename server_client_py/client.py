import socket
import time
# Address
HOST = '10.185.10.3'  # server address
PORT = 9999 
print('Host:', HOST, 'Port :', PORT)
request = 'This is fanghao_wdewindow client'
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
    reply = s.recv(1024)
    print('reply is: ', reply.decode())
# close connection
s.close()