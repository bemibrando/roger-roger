from tkinter import *
from src.gui import home
from src.components.camera import camera
from src.components.update_finance import receipt

def update_expenses(root):
    def destroyAllObjects():
        button_update.destroy()
        button_return.destroy()

    def returnHome():
        destroyAllObjects()
        home.home_display(root)

    def updateSheet():
        print("toExcel")
        rec.updateSheets()

    cam = camera.Camera()
    rec = receipt.Receipt()

    readAddress = cam.read_qr_code()
    print(readAddress)

    if(readAddress):
        cam.close_camera()
        receipt_data = rec.getReceiptData(readAddress)

        if(receipt_data):
            rec.printReceiptData(root)            
        
        else:
            reportLabel = Label(root, text="QR Code not found")
            reportLabel.pack()

    button_return = Button(root, text="<< Return", command=returnHome, bd=1, relief=SUNKEN)
    button_return.pack(side = LEFT, expand = True, fill=BOTH)
    
    button_update = Button(root, text="Update", command=updateSheet, bd=1, relief=SUNKEN)
    button_update.pack(side = LEFT, expand = True, fill=BOTH)
    
    return