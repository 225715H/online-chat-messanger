import socket
import threading
from datetime import datetime, timedelta
import time

# クライアントを削除するタイマーを開始
def remove_inactive_clients():
    while True:
        current_time = datetime.now()
        for client_address, last_time in last_message_time.items():
            if (current_time - last_time) > timedelta(minutes=1):
                remove_client(client_address)
        # 30秒ごとにチェック
        time.sleep(10)

def remove_client(client_address):
    user = clients.pop(client_address)
    print(f'{user} disconnected')

def broadcast(message):
    for c, user in clients.items():
        try:
            sock.sendto(message, c)
            print(f'{user}: {message}')
        except:
            remove_client(c)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '0.0.0.0'
server_port = 9001
print('starting up on {} port {}'.format(server_address, server_port))
sock.bind((server_address, server_port))
clients = {}
last_message_time = {}
print('Server is running...')
threading.Thread(target=remove_inactive_clients).start()

while True:
    data, client_address = sock.recvfrom(4096)
    last_message_time[client_address] = datetime.now()
    user = data.decode()
    user = user[:user.find(':') + 1] if ':' in user else user
    if client_address not in clients:
        clients[client_address] = user
        print(client_address[1], 'connected as', user)
        sock.sendto(b'You are now connected to the server.', client_address)

    else:
        broadcast(data)
    
    


