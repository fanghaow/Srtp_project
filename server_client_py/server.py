import socket
import threading
import time
# Address
HOST = '' # server address, bind self
PORT = 8089 # 9999
print('Host:', HOST, 'Port :', PORT)
# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('bind ok')

s.listen(3) # Max number of clients
print('Waiting for connection...')

def main():
    while True:
        print('start loop in main')
        # accept a new connection
        sock, addr = s.accept()
        print('receive msg from client')
        # create a new thread to proceed Tcp connection
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(0.5)
        print('Receive data is:', data.decode('utf-8'))
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello! ' + addr[0] + ' : ' + str(addr[1])).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    print('Start main')
    main()
