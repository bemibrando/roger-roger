from tkinter import *
from src.gui import finance

def home_display(root):    
    #region FUNCTIONS
    def destroyAllObjects():
        helloLabel.destroy()
        financeButton.destroy()
        button_quit.destroy()

    def financeClick():
        destroyAllObjects()
        finance.finance_display(root)
    
    #endregion
    
    #region OBJECTS
    # Creating a Hello Label Widget
    helloLabel = Label(root, text="Hello There!")
    # Shoving it onto the screen
    helloLabel.grid(row=1, column=1, columnspan=3)

    # Creating a Finance Button Widget
    financeButton = Button(root, text="Finance", padx=50, pady=8, command=financeClick)
    financeButton.grid(row=3, column=1, columnspan=3)

    button_quit = Button(root, text="Exit", command=root.quit, bd=1, relief=SUNKEN)
    button_quit.grid(row=5, column=0, columnspan=3, sticky=W+E)

    #endregion