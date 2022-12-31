from tkinter import *
from ..finance import finance
from src.components.settings import system

def home_display(root: Tk):    
    #region FUNCTIONS
    def destroyAllObjects():
        system.destroyAllObjects(frame)

    def financeClick():
        frame.destroy()
        finance.finance_display(root)
    
    #endregion
    
    #region OBJECTS
    frame = Frame(root)
    frame.pack(side="top", expand=True, fill='both')
    
    # Creating a Hello Label Widget
    helloLabel = Label(frame, text="Hello There!")
    # Shoving it onto the screen
    helloLabel.grid(row=1, column=1, columnspan=3)

    # Creating a Finance Button Widget
    financeButton = Button(frame, text="Finance", padx=50, pady=8, command=financeClick)
    financeButton.grid(row=3, column=1, columnspan=3)

    button_quit = Button(frame, text="Exit", command=root.quit, bd=1, relief=SUNKEN)
    button_quit.grid(row=5, column=0, columnspan=3, sticky=W+E)

    #endregion