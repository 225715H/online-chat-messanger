import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 9001

username = input('Enter your username: ').encode()
print(username, server_address, server_port)
sock.sendto(username, (server_address, server_port))
can_connect, _ = sock.recvfrom(4096)

def receive():
    while True:
        data, _ = sock.recvfrom(4096)
        user, _ = sock.recvfrom(4096)
        print('\nreceived {} {}\nEnter your message.'.format(data, user))

while True:
    response = threading.Thread(target=receive)
    response.start()
    message = input('').encode()

    print('sending {!r}'.format(message))
    sent = sock.sendto(message, (server_address, server_port))

