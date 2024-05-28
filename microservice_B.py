#receives 2 timezone codes (starting and ending) and returns the difference between them

import socket

# Change PORT to match the port called by the main program
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7300  # Port to listen on (non-privileged ports are > 1023)

def timeDifference(tz1, tz2):
    """receives a tuple of two time zone codes from the program and returns the time difference between them"""
    if tz1 == tz2:
        return str(0)
    if (tz1 == 'HT' and tz2 == 'AKT') or (tz1 == 'AKT' and tz2 == 'PT') or (tz1 == 'PT' and tz2 == 'MT') or (tz1 == 'MT' and tz2 == 'CT') or (tz1 == 'CT' and tz2 == 'ET'):
        return str(1)
    if (tz1 == 'HT' and tz2 == 'PT') or (tz1 == 'AKT' and tz2 == 'MT') or (tz1 == 'PT' and tz2 == 'CT') or (tz1 == 'MT' and tz2 == 'ET'):
        return str(2)
    if (tz1 == 'HT' and tz2 == 'MT') or (tz1 == 'AKT' and tz2 == 'CT') or (tz1 == 'PT' and tz2 == 'ET'):
        return str(3)
    if (tz1 == 'HT' and tz2 == 'CT') or (tz1 == 'AKT' and tz2 == 'ET'):
        return str(4)
    if (tz1 == 'HT' and tz2 == 'ET'):
        return str(5)
    if (tz1 == 'ET' and tz2 == 'CT') or (tz1 == 'CT' and tz2 == 'MT') or (tz1 == 'MT' and tz2 == 'PT') or (tz1 == 'PT' and tz2 == 'AKT') or (tz1 == 'AKT' and tz2 == 'HT'):
        return str(-1)
    if (tz1 == 'ET' and tz2 == 'MT') or (tz1 == 'CT' and tz2 == 'PT') or (tz1 == 'MT' and tz2 == 'AKT') or (tz1 == 'PT' and tz2 == 'HT'):
        return str(-2)
    if (tz1 == 'ET' and tz2 == 'PT') or (tz1 == 'CT' and tz2 == 'AT') or (tz1 == 'MT' and tz2 == 'HT'):
        return str(-3)
    if (tz1 == 'CT' and tz2 == 'HT') or (tz1 == 'ET' and tz2 == 'AKT'):
        return str(-4)
    if (tz1 == 'ET' and tz2 == 'HT'):
        return str(-5)



def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:                
                    data = conn.recv(1024).decode() 
                    data1 = data[:2] #first two letters
                    data2 = data[2:] #last two letters                           
                    conn.sendall(timeDifference(data1, data2).encode())

if __name__=="__main__":
    main()