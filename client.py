import socket

def Main():
    host = '192.168.191.3' # set the server IP address
    port = 5000 # set the port number

    s = socket.socket() # create a socket object
    s.connect((host,port)) # connect to the server

    with open('speech.txt', 'wb') as f: # create a new file to store the received data in binary mode
        while True:
            data = s.recv(1024) # receive the data from the server in chunks of 1024 bytes
            if not data:
                break
            f.write(data) # write the received data to the file

    print('Data received successfully')
    s.close() # close the socket

if __name__ == '__main__':
    Main()
