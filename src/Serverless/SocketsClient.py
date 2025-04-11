import socket

# HOST = '127.0.0.1'  # The server's hostname or IP address

HOST = '168.176.122.36' 
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while (True):
        mensaje = input("> ")
        s.sendall(mensaje.encode())
        data = s.recv(1024)
        print(data.decode())


# print('Received', repr(data))