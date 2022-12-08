from tkinter import *
import home

root = Tk()
root.title("Roger Roger!")
root.iconbitmap('../assets/icons/b1droid2.ico')
root.geometry("400x400")

home.home_display(root)

root.mainloop()