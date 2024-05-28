import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
#PORT = 7200  # The port used by the server

while True:
    myMessage = input("Enter a two-letter code for your starting state: ")
    
    #do I need to set up a new socket for each microservice? Probably...
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 7200))

        #Microservice 1
        s.sendall(myMessage.encode())
        data = s.recv(1024).decode()
        start = data

        message2 = input("Enter a second two-letter state code for your ending state: ")
        s.sendall(message2.encode())
        data2 = s.recv(1024).decode()
        end = data2
        states = (start, end)
        s.close()

    #Microservice 2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 7300))   
        states_concat = str(start)+str(end)
        s.sendall(states_concat.encode())
        data2 = s.recv(1024).decode()
        print(data2)
        s.close()
        
