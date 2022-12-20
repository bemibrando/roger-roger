from tkinter import *
from src.gui import home
from src.components.update_finance import expenses

def finance_display(root):
    #region FUNCTIONS
    def destroyAllObjects():
        button_updateExpenses.destroy()
        button_return.destroy()

    def updateExpenses():
        destroyAllObjects()
        expenses.update_expenses(root)

    def returnHome():
        destroyAllObjects()
        home.home_display(root)

    #endregion

    #region OBJECTS
    button_updateExpenses = Button(root, text="Update Expenses", padx=50, pady=8, command=updateExpenses)
    button_updateExpenses.grid(row=3, column=1, columnspan=3)

    button_return = Button(root, text="<< Return", command=returnHome, bd=1, relief=SUNKEN)
    button_return.grid(row=5, column=0, columnspan=3, sticky=W+E)
    #endregion
