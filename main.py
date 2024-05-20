import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7200  # The port used by the server

while True:
    myMessage = input("Enter a two-letter state code to get a response from the microservice: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(myMessage.encode())
        data = s.recv(1024).decode()
        print(data)
