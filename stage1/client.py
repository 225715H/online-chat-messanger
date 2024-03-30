import socket
import threading
from datetime import datetime, timedelta
import time

def remove_inactive_clients():
    while True:
        current_time = datetime.now()
        if (current_time - last_time) > timedelta(minutes=1):
            print('No activity for 5 minutes. You have been disconnected.')
            sock.close()
        # 30秒ごとにチェック
        time.sleep(10)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 9001

last_time = datetime.now()

username = input('Enter your username: ')
print(username, server_address, server_port)
sock.sendto(username.encode(), (server_address, server_port))
can_connect, _ = sock.recvfrom(4096)

def receive():
    global flag
    try:
        while flag:
            data, _ = sock.recvfrom(4096)
            data = data.decode()
            print('\n{}\nEnter your message.'.format(data))
    except OSError as e:
        if e.errno == 9:
            print('You have been disconnected.')
        else:
            False

flag = True

try:
    while True:
        responce = threading.Thread(target=receive)
        responce.start()
        threading.Thread(target=remove_inactive_clients).start()
        
        message = input()
        last_time = datetime.now()
        message = username + ': ' + message
        print('sending {!r}'.format(message))
        sent = sock.sendto(message.encode(), (server_address, server_port))

except KeyboardInterrupt:
    print('You have been disconnected.')

finally:
    flag = False
    print('closing socket')
    sock.close()
