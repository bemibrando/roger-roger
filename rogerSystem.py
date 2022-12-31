from tkinter import *
from src.gui.home import home
import global_settings as gs

def main():
    root = Tk()
    root.title("Roger Roger!")
    root.iconbitmap(gs.__b2droid_icon__)
    root.geometry(gs.__screen_size__)

    home.home_display(root)

    root.mainloop()

if __name__ == "__main__":
    main()