from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from database import Database
from multi_client import Client
from admin_page import admin
from manager_page import manager
import sys
import re

# GUI for login page
class main():
    # To initialize the values of instance members
    def __init__(self,master):
        self.master = master
        self.username = StringVar(master)
        self.password = StringVar(master)
        self.widgets()

    # To check if user is admin    
    def checkAdmin(self, s):
        return(True if s.endswith('A') else False)

    # To after click login button
    def login(self):
        client.send_one_message("Login " + str(self.username.get()) + " " + str(self.password.get()))
        results = client.recieve_messages()
        
        if results != "False":
            self.logf.pack_forget()
            # For admin page
            if self.checkAdmin(self.username.get()):
                root1.destroy()  
                self.root2 = Tk()
                self.root2.title("Administrator Page")
                self.root2.geometry("1120x350")
                admin(self.root2, 1, client)
                self.root2.protocol('WM_DELETE_WINDOW', self.close_button_r2) 
                self.root2.mainloop()
            # For manager page   
            else:
                root1.destroy()  
                self.root2 = Tk()
                self.root2.title("Manager Page")
                self.root2.geometry("1120x450")
                manager(self.root2, 1, client, self.username.get())
                self.root2.protocol('WM_DELETE_WINDOW', self.close_button_r2) 
                self.root2.mainloop()
        else:
            ms.showerror("Message", "Invalid username or password.")

    # To GUI widgets
    def widgets(self):
        self.head = Label(self.master, text = "Login", font = ("Calibri",35),pady=40)
        self.head.pack()

        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf,text="Username: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.logf,textvariable = self.username,bd=8,font=("Calibri",15,"bold")).grid(row=0,column=1,sticky=E)
        Label(self.logf,text="Password: ",font = ("Calibri Ligth",20), padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.logf,textvariable = self.password,bd=8,font=("Calibri",15,"bold"),show="*").grid(row=1,column=1,sticky=E)
        Button(self.logf,text="  Login  ",bd=7,font=("Calibri",15,"bold"),padx=5,pady=5,command=self.login).grid(row=2)
        self.logf.pack()
    
    #Overrides the closing behavior of root 2
    def close_button_r2(self):
        self.root2.destroy()
        client.send_one_message("terminate")
        client.close_connection()
    
#Overrides the closing behavior of root 1
def close_button_r1():
    root1.destroy()
    client.send_one_message("terminate")
    client.close_connection()

# To client connection
client = Client()
client.create_connection()
# To create login page
root1 = Tk()
main(root1)
root1.title("Login Page")
root1.geometry("400x350")
root1.protocol('WM_DELETE_WINDOW', close_button_r1) 
root1.mainloop()