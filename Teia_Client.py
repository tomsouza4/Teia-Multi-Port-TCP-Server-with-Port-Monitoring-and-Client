import socket
import os.path


def checkPortStatus(port):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
    host = 'localhost'
# connection to hostname on the port.
    s.connect((host, port))
# Receive no more than 1024 bytes
    #tm = s.recv(1024)
    s.close()
    #print("The time got from the server is %s" % tm.decode('ascii'))

    with open("/Users/tomsouza/ports.txt", "w") as myfile:
        myfile.write("Connected from: " + socket.gethostname() + " to: " + host + " on port: " + str(port) +"\n")

    if os.path.isfile("/Users/tomsouza/idm_ports.txt"):
        with open("/Users/tomsouza/idm_ports.txt") as file:
            ports = file.read().strip().split(',')
            port = map(int, ports)

            for i in port:
                checkPortStatus(i)