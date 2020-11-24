from tkinter import *
from tkinter import messagebox as ms
from datetime import datetime
import re

# GUI for admin
class admin:    
    # To initialize the values of instance members
    def __init__(self,master,label, client):
        self.master = master
        self.cityName = StringVar(master) 
        self.historicalPlace = StringVar(master)
        self.date = StringVar(master)
        self.v = StringVar(self.master, "1")
        # Radio buttons texts
        self.values = {"The historical place with the maximum number of visitors" : "1", 
                "The number of visitors, the number of male visitors, the number of female visitors and the number of local visitors and the number of tourists for each city" : "2", 
                "The number of visitors, the number of male visitors, the number of female visitors and the number of local visitors and the number of tourists for each city 3" : "3", 
                "The number of visitors, the number of male visitors, the number of female visitors and the number of local visitors and the number of tourists for each historical place in a given city" : "4", 
                "The number of visitors, the number of male visitors, the number of female visitors and the number of local visitors and the number of tourists for a given historical place on a given date 5" : "5"} 
        self.client = client
        self.widgets(label)

    # To selected radio buttons
    def selection(self):
        if self.v.get() == "1":
            self.client.send_one_message("Hpmax ")
            result = self.client.recieve_messages()
            
            if self.showError(result) == False:
                hp, visitor = self.splitResponse(result)
                self.createResponseMessageSingle(visitor, hp)

        elif self.v.get() == "2":
            self.client.send_one_message("Citymax ")
            result = self.client.recieve_messages()
           
            if self.showError(result) == False:
                city, visitor = self.splitResponse(result)
                self.createResponseMessageSingle(visitor, city)

        elif self.v.get() == "3":
            self.client.send_one_message("Totalcities ")
            result = self.client.recieve_messages()
            
            if self.showError(result) == False:
                city, visitor = self.splitResponse(result)
                self.createResponseMessageMulti(visitor, city, True)

        elif self.v.get() == "4":
            root3 = Tk()
            root3.title("Administrator Page")
            root3.geometry("400x350")
            admin(root3, 2, self.client)
        
        else:
            root4 = Tk()
            root4.title("Administrator Page")
            root4.geometry("400x350")
            admin(root4, 3, self.client)

    # For the fourth option after entering the city name
    def clickcityName(self):
        if (len(self.cityName.get()) > 0):
            city = self.convertInput(self.cityName.get(), 0)
            self.client.send_one_message("Totalgivencities " + city)
            result = self.client.recieve_messages()

            if self.showError(result) == False:
                hp, visitor = self.splitResponse(result)
                self.createResponseMessageMulti(visitor, hp, True)
        else:
            ms.showinfo("Message", "Please do not leave empty field!") 

    # For the fifth option after entering the date
    def clickDate(self):
        if (len(self.historicalPlace.get()) > 0 and len(self.date.get())):
            hp = self.convertInput(self.historicalPlace.get(), 1)
            hp = hp.replace(" ", "-")

            if self.checkDate(self.date.get()):
                self.client.send_one_message("Totalgivenhp " + hp + " " + self.date.get())
                result = self.client.recieve_messages()

                if self.showError(result) == False:
                    visitor = re.findall(r"\d+", result)
                    self.createResponseMessageMulti(visitor, "", False)
        else:
            ms.showerror("Message", "Please do not leave empty field!") 

    # To GUI widgets
    def widgets(self, label):
        if label == 1:
            self.head = Label(self.master, text = "Administrator Page", font = ("Calibri",15),pady=40)
            self.head.pack()
            self.adminf = Frame(self.master, padx=10, pady=10)
            lbl3 = Label(self.adminf, text="You can request the following reports from the central system.\nYour choice: ",justify= LEFT, font=("Calibri", 12)).pack()
            for (text, value) in self.values.items(): 
                Radiobutton(self.adminf, text = text, variable = self.v,value = value,font=("Calibri Light", 11)).pack(side=TOP, anchor = W) 
            Button(self.adminf, text = "Cancel", font=("Calibri",15,"bold"),padx=5,pady=5, command=self.terminate).pack(side=RIGHT, anchor = W)
            Button(self.adminf, text = "OK", font=("Calibri",15,"bold"),padx=5,pady=5, command=self.selection).pack(side=RIGHT, anchor = W)
            self.adminf.pack()

        # For fourth options' widgets
        if label == 2:
            self.head = Label(self.master, text = "Administrator Page", font = ("Calibri",35),pady=40)
            self.head.pack()
            self.adminf = Frame(self.master, padx=10, pady=10)
            Label(self.adminf,text="City Name: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
            Entry(self.adminf,textvariable = self.cityName,bd=8,font=("Calibri",15,"bold")).grid(row=0,column=1,sticky=E)
            Button(self.adminf, text ="  OK  ",bd=7,font=("Calibri",15,"bold"),padx=5,pady=5,command=self.clickcityName).grid(row=2)
            self.adminf.pack()

        # For fifth options' widgets
        if label == 3:
            self.head = Label(self.master, text = "Administrator Page", font = ("Calibri",35),pady=40)
            self.head.pack()
            self.adminf = Frame(self.master, padx=10, pady=10)
            Label(self.adminf,text="Historical Place: ",font = ("Calibri Ligth",20),padx=5,pady=5).grid(sticky=W)
            Entry(self.adminf,textvariable = self.historicalPlace,bd=8,font=("Calibri",15,"bold")).grid(row=0,column=1,sticky=E)
            Label(self.adminf,text="Date: ",font = ("Calibri Ligth",20), padx=5,pady=5).grid(row=1,column=0,sticky=W)
            Entry(self.adminf,textvariable = self.date,bd=8,font=("Calibri",15,"bold")).grid(row=1,column=1,sticky=E)
            Button(self.adminf,text="  OK  ",bd=7,font=("Calibri",15,"bold"),padx=5,pady=5,command=self.clickDate).grid(row=2)
            self.adminf.pack()
    
    # To after click cancel button
    def terminate(self):
        self.client.send_one_message("terminate")
        self.client.close_connection()
        sys.exit(0)

    # To display error message
    def showError(self, s):
        if s == "" or s == None:
            ms.showerror("Message", "Data Not Found")
            return True
        else:
            return False

    # To capitalise only the first letter of input and send it to query
    def convertInput(self, input, mode):
        if "İ" in str(input):
            input = str(input).replace("İ", "i")
        input = str(input).lower()
        
        if mode == 1:
            inputList = input.split()
            input = ""
            for i in range(0, len(inputList)):
                input += inputList[i].capitalize()
                if (i < len(inputList) - 1):
                    input += " "
        else:
            input = input.capitalize()

        return input

    # To check date format
    def checkDate(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            ms.showinfo("Message", "Incorrect data format, should be DD/MM/YYYY or date is not valid.")
            return False

    # To split response
    def splitResponse(self, result):
        hp = re.findall(r"'(.*?)'", result)
        visitor = re.findall(r"\d+", result)
        return hp, visitor

    # To create single response message 
    def createResponseMessageSingle(self, visitor, hp):
            message = ""
            for i in range(len(hp)):
                message += hp[i] + " \nTotal number of visitor = " + str(visitor[i]) + "\n\n"
            ms.showinfo("Message", message)

    # To create multiple response message 
    def createResponseMessageMulti(self, visitor, hp, isOptional):
        values = []
        c = ""

        tag = ["V: ", "M: ", "F: ", "L: ", "T: "]
        for i in range(len(visitor)):    
            if i % 5 == 0 and i != 0:
                values.append(c)
                c = tag[i%5] + visitor[i] + " "
            else:
                c += tag[i%5] + visitor[i] + " "
        values.append(c)
        
        message = ""

        for i in range(len(values)):
            if isOptional:
                message += hp[i] + " \n" + str(values[i]) + "\n\n"
            else:
                message += str(values[i]) + "\n\n"
        ms.showinfo("Message", message + "\n\nV = The number of visitors\nM = The number of male visitors\nF = The number of female visitors\nL = The number of local visitors\nT = The number of tourists")