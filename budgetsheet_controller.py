# imports model and view
import budgetsheet_model as m
import budgetsheet_view as v


# creates a new class 
class Expensecontroller():

    # initializes the expensemodel and view
    def __init__(self):
        self.x = m.Expensemodel()
        self.y = v.Main_GUI()

    # calls the delete method
    def expense_delete(self):
        self.x.delete_expense()

    # links the add new expense method
    def expense_add(self, desc, amnt):
        addret = self.x.add_expense(desc, amnt)
        return addret

    # links the download
    def expense_download(self, y):
        self.x.download_expense(y)

    # links the total expense
    def expense_total(self):
        self.x.total_expense()

    # return main screen
    def main_screen(self):
        self.y.run()

# main functionality of the program
if __name__ == '__main__':
    u = Expensecontroller()
    u.main_screen()
