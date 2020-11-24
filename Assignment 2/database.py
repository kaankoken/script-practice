import os
import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        #Initialize the connection variable
        self.connection = None
        #gets the path of current directory 
        self.path = os.getcwd() + "/db"

    def __create_database_folder(self):
        #Creates DB folder if it is not exist
        if (not os.path.isdir(self.path)):
            os.mkdir(path=self.path)
        #Creates db.sqlite file if it is not exist
        if (not os.path.isfile(self.path + "/db.sqlite")):
            file = open(self.path + "/db.sqlite", "w")
            file.close()

    def create_connection(self):
        try:
            self.__create_database_folder()
            #Connects to database file
            self.connection = sqlite3.connect(self.path + "/db.sqlite")
            print("Connected")
        except Error as e:
            print(e)
    #Creates necessary table
    def create_table(self):
        city = '''CREATE TABLE IF NOT EXISTS city(
                            citycode integer PRIMARY KEY,
                            cityname text NOT NULL);'''

        historical_place = '''CREATE TABLE IF NOT EXISTS historical_place(
                                        hpcode integer PRIMARY KEY,
                                        hpname text NOT NULL,
                                        citycode integer NOT NULL,
                                        staffid integer NOT NULL,
                                        FOREIGN KEY (citycode) REFERENCES city (citycode)
                                        FOREIGN KEY (staffid) REFERENCES staff (staffid));'''

        visitor = '''CREATE TABLE IF NOT EXISTS visitor(
                                        date integer NOT NULL,
                                        hpcode integer NOT NULL,
                                        numberofLocalVisitor integer NOT NULL,
                                        numberofMaleVisitor integer NOT NULL,
                                        numberofFemaleVisitor integer NOT NULL,
                                        numberofTourists integer NOT NULL,
                                        PRIMARY KEY (hpcode, date)
                                        FOREIGN KEY (hpcode) REFERENCES historical_place (hpcode));'''

        staff = '''CREATE TABLE IF NOT EXISTS staff(
                                        staffid integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL);'''   

        table_array = [city, staff, historical_place, visitor]

        for i in table_array:
            try:
                cursor = self.connection.cursor()
                cursor.execute(i)
                cursor.close()
            except Error as e:
                print(e)
    #Inserts the data to existing tables
    def insert_data(self):
        cursor = self.connection.cursor()

        city = [(1, "Gazimagusa"),
                (2, "Girne"),
                (3, "Guzelyurt"),
                (4, "Iskele"),
                (5, "Lefke"),
                (6,  "Lefkosa")]

        staff = [(1001, "1001HPM", 1234),
                 (1002, "1002HPM", 5678),
                 (1003, "1003HPM", 9123),
                 (1004, "1004HPM", 4567),
                 (1005, "1005HPM", 8912),
                 (1006, "1006HPM", 3456),
                 (1007, "1007HPM", 7891),
                 (1008, "1008HPM", 2345),
                 (1009, "1009HPM", 6789),
                 (1010, "1010HPM", 1234),
                 (1011, "1011HPM", 5678),
                 (1012, "1012HPM", 9123),
                 (1013, "1013A", 4567),
                 (1014, "1014A", 8912),
                 (1015, "1015A", 3456)]

        historical_place = [(1, "Othello Castle", 1, 1001),
                            (2, "St. Barnabas Monastery", 1, 1002),
                            (3, "St. Hilarion Castle", 2, 1003),
                            (4, "Bellapais Abbey", 2, 1004),
                            (5, "Guzelyurt Museum", 3, 1005),
                            (6, "St. Mamas Monastery", 3, 1006),
                            (7, "Apostolos Andreas Monastery", 4, 1007),
                            (8, "Kantara Castle", 4, 1008),
                            (9, "Soli", 5, 1009),
                            (10, "Vouni Palace", 5, 1010),
                            (11, "St. Sophia Cathedral", 6, 1011),
                            (12, "Dervis Pasa Mansion", 6, 1012)]

        try:
            cursor.executemany('INSERT OR IGNORE INTO city VALUES(?,?)', city)
            cursor.executemany('INSERT OR IGNORE INTO staff VALUES(?,?,?)', staff)
            cursor.executemany('INSERT OR IGNORE INTO historical_place VALUES(?,?,?,?)', historical_place)
        except Error as e:
            print(e)

        self.connection.commit()
    #Close connection of database
    def close_connection(self):
        self.connection.close()