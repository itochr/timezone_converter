#Written by Walter Downing (waltdowning)
#receives a 2-letter state code and returns the time zone

import socket

# Change PORT to match the port called by the main program
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7200  # Port to listen on (non-privileged ports are > 1023)


# Time zones are sets of state code strings
alaskaTime = {'AK'}
pacificTime = {'CA', 'OR', 'NV', 'WA'}
mountainTime = {'AZ', 'CO', 'ID', 'MT', 'NM', 'UT', 'WY'}
centralTime = {'AL', 'AR', 'IL', 'IA', 'KS', 'LA', 'MN',
               'MN', 'MS', 'MO', 'NE', 'ND', 'OK', 'SD',
               'TN', 'TX', 'WI'}
easternTime = {'CT', 'DE', 'FL', 'GA', 'IN', 'KY', 'ME', 
               'MD', 'MA', 'MI', 'NH', 'NJ', 'NY', 'NC', 
               'OH', 'PA', 'RI', 'SC', 'VT', 'VA', 'WV'}
hawaiiTime = {'HI'}

# timeZones is a dictionary of sets with time zone abbreviation strings as keys
timeZones = {'AKT': alaskaTime,
             'PT': pacificTime,
             'MT': mountainTime,
             'CT': centralTime,
             'ET': easternTime,
             'HT': hawaiiTime}

# Given a two-letter state code, returns a string of the time zone that state is in
def findTimeZone(requestedState):
    for timeZone in timeZones:
        if requestedState in timeZones[timeZone]:
            return timeZone
    return "Not Found"


def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:                
                    data = conn.recv(1024).decode()               
                    if not data:
                        break                
                    conn.sendall(findTimeZone(data).encode())

if __name__=="__main__":
    main()
