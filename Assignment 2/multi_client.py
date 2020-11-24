import socket
import struct
import time

class Client:
    #initialize the host
    host: str = '127.0.0.1'
    #initialize the port number
    port: int = 8080

    def __init__(self):
        #Creates the connection to socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.response = ""

    def create_connection(self):
        print('Waiting for connection')
        connection_stat = 1
        
        #tries to connect to given host and port until server is up
        while connection_stat != 0:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection_stat = self.client_socket.connect_ex((self.host, self.port))

    #close the connection
    def close_connection(self):
        self.client_socket.close()

    #Send request to server side
    def send_one_message(self, data):
        time.sleep(0.5)
        self.client_socket.send(str.encode(data))
    
    #Receive response from server side
    def recieve_messages(self):
        message = []
        time.sleep(0.5)

        self.response = self.client_socket.recv(1024)
        self.response = self.split_message(self.response.decode('utf-8'))

        for i in self.response:
            msg = self.analyzeText(i)
            if len(msg) > 0:
                return msg
    #Splits incoming response from server side
    def split_message(self, message):
        messages = message.split("\n")
        return messages

    #Checks whether incoming response printable or
    #needs to return client side
    def analyzeText(self, text):
        if "!" in text: 
            print(text.replace("!", ""))
        else:
            return text
        return ""