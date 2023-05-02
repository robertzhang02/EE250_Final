import socket

def Main():
    host = '192.168.191.3' # set the server IP address
    port = 5000 # set the port number

    s = socket.socket() # create a socket object
    s.bind((host,port)) # bind the socket to the IP address and port number
    s.listen(1) # listen for incoming connections

    print('Server ready to receive data...')

    conn, addr = s.accept() # accept the connection request
    print('Connection from: ' + str(addr))

    with open('output.txt', 'rb') as f: # open the file to be transferred in binary mode
        data = f.read(1024) # read the file in chunks of 1024 bytes
        while data:
            conn.send(data) # send the data to the client
            data = f.read(1024) # read the next chunk of data

    print('Data transfer complete')
    conn.close() # close the connection

if __name__ == '__main__':
    Main()
