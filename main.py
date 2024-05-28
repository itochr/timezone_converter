import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
#PORT = 7200  # The port used by the server

while True:
    print("\nWelcome to the timezone converter! This program will allow you to enter a time and a US state.\nThe program will tell you the equivalent time in whatever state you choose! It will take roughly 30 seconds to a minute to use.\nTo start, please enter the two-letter state code for a US state (or DC for Washington DC).")
    myMessage = input("Enter a two-letter code for your starting state: ")
    
    #do I need to set up a new socket for each microservice? Probably...
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 7200))

        #Microservice A
        s.sendall(myMessage.encode())
        data = s.recv(1024).decode()
        start = data

        message2 = input("Enter a second two-letter state code for your ending state: ")
        s.sendall(message2.encode())
        data2 = s.recv(1024).decode()
        end = data2
        states = (start, end)
        s.close()

    #Microservice B
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 7300))   
        states_concat = str(start) + str(end)
        s.sendall(states_concat.encode())
        data2 = s.recv(1024).decode()

    #Microservice C
    time = str(input("Please enter a time in 24hr format (HH:MM): "))
    hour = time[:2]
    minute = time[2:]
    time_concat = hour + data2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 7400))
        s.sendall(time_concat.encode())
        data3 = s.recv(1024).decode()
    newtime = data3 + minute

    #Microservice D
    data_concat = time + newtime + myMessage + message2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 7500))
        s.sendall(data_concat.encode())
        result = s.recv(1024).decode()
    print(result)