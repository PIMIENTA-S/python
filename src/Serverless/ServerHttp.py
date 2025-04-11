import socket

HOST = 'www.testingmcafeesites.com'  # Standard loopback interface address (localhost)
PORT = 80        # Port to listen on (non-privileged ports are > 1023)

mensaje = """
GET /testcat_au.html HTTP/1.1
Host: www.testingmcafeesites.com
User-Agent: curl/8.6.0
Accept: */*

"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensaje.encode())
    data = s.recv(1024)
    print(data.decode())



    # conn, addr = s.accept()
    # with conn:
    #     print('Connected by', addr)
    #     data = conn.recv(1024)

    #     if data.decode() == "Cuelga tu":
    #         break
    #     print(data.decode()) #la data viene en bits

    #     conn.sendall(mensaje.encode())