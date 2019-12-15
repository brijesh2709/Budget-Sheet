from tkinter import *
# import os and controller
import os
import budgetsheet_controller as c


# class Expense model is created
class Expensemodel():

    # initializes the expenselist
    def __init__(self):
        self.expenselist = []

    # add new expense
    def add_expense(self, desc, amnt):

        expense = []
        expense.append(desc)
        expense.append(amnt)
        return expense

    # downloading the expenses
    def download_expense(self):
        x = os.getcwd()
        print(x)
        x += '\output.csv'
        f = open(x, 'w')
        for i in y:
            f.write(i[0]+','+str(i[1])+'\n')
        f.close()

    # return the total expense
    def total_expense(self):
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
