import socket
from builtins import filter

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print(f"Connection from {client_address}")

data = connection.recv(1024)
print(f"Received: {data.decode()}")

connection.sendall(b"Hello from server!")

connection.close()
server_socket.close()
t=1
print(t)
print(t)