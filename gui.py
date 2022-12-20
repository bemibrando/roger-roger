from tkinter import *
from src.gui import home
import global_setting as gs

root = Tk()
root.title("Roger Roger!")
root.iconbitmap(gs.__b2droid_icon__)
root.geometry(gs.__screen_size__)

home.home_display(root)

root.mainloop()