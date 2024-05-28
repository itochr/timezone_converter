#receives a starting state, ending state, start/end time, and formats it into a sentence
#'When it is _ (time) in _ (state), it is _ (time) in _ (state)'

import socket

# Change PORT to match the port called by the main program
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7500  # Port to listen on (non-privileged ports are > 1023)

def stringFormat(st_state, end_state, st_time, end_time):
    """takes all the data and formats it into a string to return"""
    sentence = ('When it is ' + st_time + ' in ' + st_state + ', it is ' + end_time + ' in ' + end_state + '.' )
    return sentence

def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:                
                    data = conn.recv(1024).decode()   
                    st_time = data[:5]
                    st_state = data[5:10]
                    end_time = data[10:12]
                    end_state = data[12:]                         
                    conn.sendall(stringFormat(st_time, st_state, end_time, end_state).encode())

if __name__=="__main__":
    main()