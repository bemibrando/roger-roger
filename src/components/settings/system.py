from tkinter import *
import os

def checkDirectoryExist(dicPath: str):
    return os.path.exists(dicPath)        

def createDirectory(dicPath: str):
    os.mkdir(dicPath)

def checkFileExist(dicPath: str):
    return os.path.isfile(dicPath)

def destroyAllObjects(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()