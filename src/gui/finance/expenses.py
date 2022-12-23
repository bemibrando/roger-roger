from tkinter import *
from src.gui.home import home
from src.components.camera import camera
from src.components.update_finance import receipt
from src.components.settings import system

def update_expenses(root: Tk):
    def destroyAllObjects():
        system.destroyAllObjects(frame)

    def returnHome():
        frame.destroy()
        home.home_display(root)

    def confirmUpdateFile():
        destroyAllObjects()
        reportLabel = Label(frame, text="")

    def updateSheet():
        destroyAllObjects()
        rec.updateSheets()
        
        reportLabel = Label(frame, text=" Successfully Updated")
        reportLabel.pack()

        button_return = Button(frame, text="<< Return", command=returnHome, bd=1, relief=SUNKEN)
        button_return.pack(side = LEFT, expand = True, fill=BOTH)
        
        button_update = Button(frame, text="New Receipt", command=getQRCode, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=BOTH)

    def getQRCode():
        destroyAllObjects()       
        readAddress = cam.read_qr_code()
        print(readAddress)

        if(readAddress):
            cam.close_camera()
            receipt_data = rec.getReceiptData(readAddress)

            if(receipt_data):
                rec.printReceiptData(frame)
            
            else:
                reportLabel = Label(frame, text="QR Code not found")
                reportLabel.pack()

            createButtons()

    def createButtons():
        button_return = Button(frame, text="<< Return", command=returnHome, bd=1, relief=SUNKEN)
        button_return.pack(side = LEFT, expand = True, fill=BOTH)
        
        button_update = Button(frame, text="Update", command=updateSheet, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=BOTH)


    frame = Frame(root)
    frame.pack(side="top", expand=True, fill='both')
    
    cam = camera.Camera()
    rec = receipt.Receipt()    

    getQRCode()
    
    return