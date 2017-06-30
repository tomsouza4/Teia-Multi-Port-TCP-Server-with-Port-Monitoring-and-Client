import threading
import time
import SocketServer
import os.path

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "%s wrote: " % self.client_address[0]
        print self.data
        self.request.send(self.data.upper())

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

idm_ports = "/Users/tomsouza/idm_ports.txt"

if __name__ == "__main__":

    def initPorts(ports):
        HOST = 'localhost'
        PORT_A = ports

        server_A = ThreadedTCPServer((HOST, PORT_A), ThreadedTCPRequestHandler)

        server_A_thread = threading.Thread(target=server_A.serve_forever)

        #Sets the thread to run as a background process when is set to False
        server_A_thread.setDaemon(True)

        server_A_thread.start()

        print("Server loop running in thread:", server_A_thread.name)

    def acceptSocket(s):
        serversocket = s
        # establish a connection
        clientsocket, addr = serversocket.accept()
        clientsocket.settimeout(1)

        print("Got a connection from %s" % str(addr))
        currentTime = time.ctime(time.time()) + "\r\n"
        clientsocket.send(currentTime.encode('ascii'))
        clientsocket.close()

    if os.path.isfile(idm_ports):
        with open(idm_ports) as file:
            ports = file.read().strip().split(',')
            port = map(int, ports)

            for i in port:
                initPorts(i)

    else:
        print ("File not found: ")
