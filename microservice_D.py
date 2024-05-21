#receives a starting state, ending state, start/end time, and formats it into a sentence
#'When it is _ (time) in _ (state), it is _ (time) in _ (state)'

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
                    conn.sendall(stringFormat(data).encode())

if __name__=="__main__":
    main()