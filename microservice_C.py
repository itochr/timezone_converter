#receives a starting time and a +/- time difference value to determine the new time

def newTime(start, timeDif):
    """determines the new time after accounting for time difference, including day roll over"""
    if start + timeDif >= 24:
        newTime = (start + timeDif) - 24
        newString = str('00:' + newTime + 'the next day')
    elif start + timeDif < 0:
        newTime = 24 - (start + timeDif)
        newString = str(newTime + 'the previous day')
    else:
        newString = str(start + timeDif)
    return newString


def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:                
                    data = conn.recv(1024).decode()                            
                    conn.sendall(newTime(data).encode())

if __name__=="__main__":
    main()