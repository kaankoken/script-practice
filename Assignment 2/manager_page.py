from tkinter import *
from tkinter import messagebox as ms
from datetime import datetime
import re

# GUI for manager
class manager:    
    # To initialize the values of instance members
    def __init__(self,master,label, client, username):
        self.master = master
        self.date = StringVar(master) 
        self.totalVisitors = StringVar(master)
        self.maleVisitors = StringVar(master)
        self.femaleVisitors = StringVar(master)
        self.localVisitors = StringVar(master)
        self.touristVisitors = StringVar(master)
        self.client = client
        self.username = username
        self.widgets()

    # To enter statistics
    def statistics(self):
        # Just for daily statistics
        if self.checkDate(self.date.get()):
            if self.checkInput():
                self.client.send_one_message("Insert " + str(self.username) + " " + str(self.totalVisitors.get()) + " " + str(self.date.get())  + " " + str(self.localVisitors.get()) + " " + str(self.maleVisitors.get()) + " " + str(self.femaleVisitors.get()) + " " + str(self.touristVisitors.get()))
                result = self.client.recieve_messages()
                if result != None and result != "False":
                    ms.showinfo("Message", "Insertion Successfully!")
                else:
                    ms.showerror("Message", "The application failed to installation properly")
   
    # To after click cancel button
    def terminate(self):
        self.client.send_one_message("terminate")
        self.client.close_connection()
        sys.exit(0)

    # To check date format
    def checkDate(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            ms.showerror("Message", "Incorrect data format, should be DD/MM/YYYY or date is not valid.")
            return False    

    # To ensure that the values received from the user for statistical values are positive integer
    def checkInput(self):
        try:
            int(str(self.totalVisitors.get()))
            int(str(self.maleVisitors.get()))
            int(str(self.femaleVisitors.get()))
            int(str(self.localVisitors.get()))
            int(str(self.touristVisitors.get()))
            if int(str(self.totalVisitors.get())) >= 0 and int(str(self.maleVisitors.get())) >= 0 and int(str(self.femaleVisitors.get())) >= 0 and int(str(self.localVisitors.get())) >= 0 and int(str(self.touristVisitors.get())) >= 0:
                return True
            else:
                ms.showerror("Message", "You can not enter negative numbers. Try again.")
                return False
        except ValueError:
            ms.showerror("Message", "Please enter only numbers. Try again.")
            return False
            
    # To GUI widgets    
    def widgets(self):
        self.head = Label(self.master, text = "Manager Page", font = ("Calibri",35),pady=40)
        self.head.pack()
        self.managerf = Frame(self.master, padx=10, pady=10)
        Label(self.managerf,text="Date (DD/MM/YYYY): ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.managerf,textvariable = self.date,bd=8,font=("Calibri",15,"bold")).grid(row=0,column=1,sticky=E)
        Label(self.managerf,text="Total Number of Visitors: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.managerf,textvariable = self.totalVisitors,bd=8,font=("Calibri",15,"bold")).grid(row=1,column=1,sticky=E)
        Label(self.managerf,text="The Number of Male Visitors: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.managerf,textvariable = self.maleVisitors,bd=8,font=("Calibri",15,"bold")).grid(row=2,column=1,sticky=E)
        Label(self.managerf,text="The Number of Female Visitors: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.managerf,textvariable = self.femaleVisitors,bd=8,font=("Calibri",15,"bold")).grid(row=3,column=1,sticky=E)
        Label(self.managerf,text="The Number of Local Visitors: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.managerf,textvariable = self.localVisitors,bd=8,font=("Calibri",15,"bold")).grid(row=4,column=1,sticky=E)
        Label(self.managerf,text="The Number of Tourists: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
        Entry(self.managerf,textvariable = self.touristVisitors,bd=8,font=("Calibri",15,"bold")).grid(row=5,column=1,sticky=E)
        Button(self.managerf, text ="  OK  ",bd=8,font=("Calibri",15,"bold"),padx=5,pady=5,command=self.statistics).grid(row=7,column=1)
        Button(self.managerf, text ="  Cancel  ",bd=8,font=("Calibri",15,"bold"),padx=5,pady=5,command=self.terminate).grid(row=7,column=2)
        self.managerf.pack()

    