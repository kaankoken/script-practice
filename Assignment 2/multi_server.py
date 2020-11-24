import socket
import os

from database import Database
from query import Query

class Server(Database, Query):
    #local host address
    host: str = '127.0.0.1'
    #port number
    port: int = 8080
    #how many threads are in use
    thread_count: int = 0
    
    #Initialize the Database and server socket
    def __init__(self):
        Database.__init__(self)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #starts the server side and 
    #create table and insert data to database
    def start_server(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.create_connection()
            if self.connection is not None:
                self.create_table()
                self.insert_data()
                self.close_connection()
            else:
                print("Error! cannot create the database connection")
        except socket.error as e:
            print(str(e))

        #Listens the incoming connections
        print('Waiting for a Connection...')
        self.server_socket.listen(5)

    #Assigns threads to the users
    def threaded_client(self, conn):

        conn.send(str.encode('Welcome to the Server!!\n'))
        
        condition: bool = True
        while condition:
            try:
                data = conn.recv(1024)
            except Exception as e:
                print(e)
            #if terminate message comes terminate the connection
            if (str.lower(data.decode('utf-8')) == "terminate"):
                condition = False
            else:
                #Opens connection to database
                self.create_connection()
                #Decode incoming request
                message = data.decode('utf-8')
                
                #If data consist Login keyword, goes to login
                if "Login" in message: 
                    status = self.checkAuth(self.connection, message)

                    if status:
                        reply = "Login Succesfull!!"
                    else:
                        reply = "Login Failed!!"

                    #Replies to client
                    conn.send(str.encode(reply + "\n" +str(status)))
                #If data consist Insert keyword, goes to insert statistics
                elif "Insert" in message:
                    status = self.insertStatistics(self.connection, message)

                    if status:
                        reply = "Succesfully Inserted!!"
                    else:
                        reply = "Insertion Failed!!"
                    #Replies to client
                    conn.send(str.encode(reply))
                    conn.send(str.encode("\n"+str(status)))
                #If data consist Hpmax keyword, goes to Option A
                elif "Hpmax" in message:
                    status = self.getMaxVisitorOfHistoricalPlace(self.connection)
                   
                    if status != "":
                        reply = "Search Result!!"
                    else:
                        reply = "No data found!!"
                    #Replies to client
                    conn.send(str.encode(reply))
                    conn.send(str.encode("\n"+str(status)))
                #If data consist Citymax keyword, goes to Option B
                elif "Citymax" in message:
                    status = self.getMaxVisitorOfCity(self.connection)

                    if status != "":
                        reply = "Search Result!!"
                    else:
                        reply = "No data found!!"
                    #Replies to client
                    conn.send(str.encode(reply))
                    conn.send(str.encode("\n"+str(status)))
                #If data consist Totalcities keyword, goes to Option C
                elif "Totalcities" in message:
                    status = self.totalVisitorOfCities(self.connection)

                    if status != "":
                        reply = "Search Result!!"
                    else:
                        reply = "No data found!!"
                    #Replies to client
                    conn.send(str.encode(reply))
                    conn.send(str.encode("\n"+str(status)))
                #If data consist Totalgivencities keyword, goes to Option D
                elif "Totalgivencities" in message:
                    status = self.totalVisitorOfGivenCity(self.connection, message)

                    if status != "":
                        reply = "Search Result!!"
                    else:
                        reply = "No data found!!"
                    #Replies to client
                    conn.send(str.encode(reply))
                    conn.send(str.encode("\n"+str(status)))
                #If data consist Totalgivenhp keyword, goes to Option E
                elif "Totalgivenhp" in message:
                    status = self.totalVisitorOfGivenHp(self.connection, message)

                    if status != "":
                        reply = "Search Result!!"
                    else:
                        reply = "No data found!!"
                    #Replies to client
                    conn.send(str.encode(reply))
                    conn.send(str.encode("\n"+str(status)))
                
                else:
                    #Replies with Error message
                    conn.send(str.encode("Error"))
                    conn.send(str.encode("\n"+"Error"))
            if not data:
                break
        else:
            #close the conneciton
            conn.close()
            self.thread_count -= 1