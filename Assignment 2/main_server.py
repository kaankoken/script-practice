from multi_server import Server
from _thread import *

def main():
    server = Server()
    server.start_server()

    while True:
        Client, address = server.server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(server.threaded_client, (Client, ))
        server.thread_count += 1
        print('Thread Number: ' + str(server.thread_count))
    server.server_socket.close()


if __name__ == "__main__":
    main()