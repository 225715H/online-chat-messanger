import socket
import threading


def broadcast(message):
    for c, user in clients.items():
        try:
            sock.sendto(message, c)
            sock.sendto(user, c)
            print(message, 'send to', user)
        except Exception as e:
            print(e)
            print('Error broadcasting to', c)
            continue

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '0.0.0.0'
server_port = 9001
print('starting up on {} port {}'.format(server_address, server_port))
sock.bind((server_address, server_port))
clients = {}
print('Server is running...')

while True:
    data, client_address = sock.recvfrom(4096)
    user = data.decode()
    if client_address not in clients:
        clients[client_address] = user
        print(client_address[1], 'connected as', user)
        sock.sendto(b'You are now connected to the server.', client_address)

    else:
        broadcast(data)
    
    


