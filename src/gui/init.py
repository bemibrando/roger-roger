from tkinter import *
from src.components.settings.user import User

def __init_gui__(root):    
    #region FUNCTIONS
    def destroyAllObjects():
        helloLabel.destroy()
        button_quit.destroy()

    def createUser():
        destroyAllObjects()
    
    #endregion
    
    #region OBJECTS
    # Creating a Hello Label Widget
    helloLabel = Label(root, text="  Hello There!  ")
    # Shoving it onto the screen
    helloLabel.pack()

    # Select User

    # Creating a new User
    CreateUser = Button(root, text="Create New User", padx=50, pady=8, command=createUser)
    CreateUser.pack()

    button_quit = Button(root, text="Exit", command=root.quit, bd=1, relief=SUNKEN)
    button_quit.pack()

    #endregion