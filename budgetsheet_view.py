# imports tkinter, os and controller
from tkinter import *
import os
import budgetsheet_controller as c


# creates a new class called Main_GUI
class Main_GUI():

    # initializes the class
    def __init__(self):
        pass

    # method for the tkinter window
    def GUI_screen(self, wn):
        self.expenselist = []
        self.wn = wn
        self.wn.title('Expense Tracker')
        self.wn.geometry('330x450')

        # creates a frame
        self.fr1 = Frame(self.wn)
        self.fr1.pack()

        # creates a label
        self.labN = Label(self.fr1, text='Description')
        self.labN.grid(row=0, column=0)

        # gets the entry for description
        self.enN = Entry(self.fr1)
        self.enN.grid(row=0, column=1)

        # creates a label
        self.labT = Label(self.fr1, text='Amount($)')
        self.labT.grid(row=1, column=0)

        # gets the entry for amount
        self.enT = Entry(self.fr1)
        self.enT.grid(row=1, column=1)

        # creates a new frame
        self.fr2 = Frame(self.wn)
        self.fr2.pack()

        # add buttons
        self.addB = Button(self.fr2, text='Add expense', command=self.addF)
        self.addB.grid(row=0, column=0)

        self.delB = Button(self.fr2, text='Delete expense', command=self.delF)
        self.delB.grid(row=0, column=6)

        self.fr3 = Frame(self.wn)
        self.fr3.pack()

        # creates scroll bar
        self.scroll = Scrollbar(self.fr3)
        self.scroll.pack()

        # scroll bar setup
        self.expenses = Listbox(self.fr3, yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.expenses.yview)
        self.expenses.pack(side=LEFT)

        # labels
        self.labE = Label(self.fr3, text="", fg="red")
        self.labE.pack()

        # buttons
        self.quitB = Button(self.wn, text='Quit', command=self.wn.destroy)
        self.quitB.pack(side='bottom')

        self.downloadB = Button(self.wn, text='Download', 
                                command=self.download_csv)
        self.downloadB.pack(side='bottom')

        self.totalB = Button(self.wn, text='Total Expense', 
                             command=self.total_amount)
        self.totalB.pack(side='bottom')

    # a new mthod to add expenses
    def addF(self):
        desc = self.enN.get()
        amnt = self.enT.get()
        d = c.Expensecontroller()
        retexpenses = d.expense_add(desc, amnt)
        self.expenselist.append(retexpenses)
        if desc == "" or amnt == "":
            self.labE.configure(text="Fields are empty")
        else:
            self.expenses.insert(END, desc+'-'+amnt)
            self.enN.delete(0, END)
            self.enT.delete(0, END)
            self.labE.configure(text="")

    # delete expenses
    def delF(self):
        index = self.expenses.curselection()[0]
        self.expenses.delete(index)

    # download your expenses
    def download_csv(self):
        x = os.getcwd()
        print(x)
        x += '\output.csv'
        f = open(x, 'w')
        for i in self.expenselist:
            f.write(i[0]+','+str(i[1])+'\n')
        f.close()

    # total amount of the expenses
    def total_amount(self):
        amount = []
        for i in range(len(self.expenselist)):
            x = float(self.expenselist[i][1])
            amount.append(x)

        tot = sum(amount)
        master = Tk()
        # assigned to variable x like you showed
        x = tot 
        master.minsize(width=400, height=400)
        # shows as text in the window
        w = Label(master, text=x) 
        w.pack()
        mainloop()

    # main method to run
    def run(self):
        wn = Tk()
        my_gui = Main_GUI()
        my_gui.GUI_screen(wn)
        wn.mainloop()
