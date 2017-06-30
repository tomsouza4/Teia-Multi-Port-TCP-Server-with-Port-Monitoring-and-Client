import threading
import SocketServer


class Datahandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(2048)

        if self.data:
            self.request.sendall(self.data)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def main():
    global TDC_servers
    global TDC_server_threads

    TDC_servers = []
    TDC_server_threads =[]

    TDC_servers.append(ThreadedTCPServer(('', 1520), Datahandler))
    TDC_servers.append(ThreadedTCPServer(('', 1525), Datahandler))

    for TDC_server in TDC_servers:
        TDC_server_threads.append(threading.Thread(target=TDC_server.serve_forever))

    for TDC_server_thread in TDC_server_threads:
        TDC_server_thread.setDaemon(True)
        TDC_server_thread.start()

    while True:
        continue

if __name__ == '__main__':
    try:
        main()


    finally:
        print('quitting servers')

        for TDC_server in TDC_servers:
            TDC_server.server_close()