from tkinter import *
from rogerSystem import home
from src.gui.finance import expenses
from src.components.settings import system

def finance_display(root: Tk):
    #region FUNCTIONS
    def destroyAllObjects():
        system.destroyAllObjects(frame)

    def updateExpenses():
        frame.destroy()
        expenses.update_expenses(root)

    def returnHome():
        frame.destroy()
        home.home_display(root)

    #endregion

    #region OBJECTS
    frame = Frame(root)
    frame.pack(side="top", expand=True, fill='both')

    button_updateExpenses = Button(frame, text="Update Expenses", padx=50, pady=8, command=updateExpenses)
    button_updateExpenses.grid(row=3, column=1, columnspan=3)

    button_return = Button(frame, text="<< Return", command=returnHome, bd=1, relief=SUNKEN)
    button_return.grid(row=5, column=0, columnspan=3, sticky=W+E)
    #endregion
