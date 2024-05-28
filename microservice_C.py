#receives a starting time and a +/- time difference value to determine the new time
import socket

# Change PORT to match the port called by the main program
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7400  # Port to listen on (non-privileged ports are > 1023)

def newTime(start, timeDif):
    """determines the new time after accounting for time difference, including day roll over"""
    if start + timeDif >= 24:
        newStr = (start + timeDif) - 24
    elif start + timeDif < 0:
        newStr = 24 - (start + timeDif)
    else:
        newStr = str(start + timeDif)
    return newStr


def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:                
                    data = conn.recv(1024).decode()   
                    hour = int(data[:2])
                    diff = int(data[2:])                        
                    conn.sendall(newTime(hour, diff).encode())

if __name__=="__main__":
    main()