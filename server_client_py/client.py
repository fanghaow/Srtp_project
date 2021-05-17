import socket
import time
# Address
HOST = '10.190.64.66' # server address, solved by Easyconnect!!! check for its new ip in control broad.
PORT = 8089 # 9999 
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
    reply = s.recv(1024)
    print('reply is: ', reply.decode())
    
# close connection
s.close()