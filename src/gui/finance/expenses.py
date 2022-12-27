from tkinter import *
from src.gui.home import home
from src.components.camera import camera
from src.components.update_finance import receipt
from src.components.settings.system import destroyAllObjects, destroyButtons

def update_expenses(root: Tk):

    def returnHome():
        frame.destroy()
        home.home_display(root)

    def confirmUpdateFile():
        destroyAllObjects(frame)
        reportLabel = Label(frame, text="")

    def updateSheet():
        destroyAllObjects(frame)
        rec.updateSheets()
        
        reportLabel = Label(frame, text=" Successfully Updated")
        reportLabel.pack()

        buttonHome()
        buttonNewQRCode()
        
    def getQRCode():
        destroyAllObjects(frame)       
        readAddress = cam.read_qr_code()
        print(readAddress)

        if(readAddress):
            cam.close_camera()
            receipt_data = rec.getReceiptData(readAddress)

            if(receipt_data):
                rec.printReceiptData(frame)

                buttonHomeEditUpdate()
            else:
                reportLabel = Label(frame, text="QR Code not found")
                reportLabel.pack()

                buttonHomeNewQR()

    def cancelEditTable():
        destroyAllObjects(frame)
        
        if rec.getDataStatus() == 200:
            rec.printReceiptData(frame)

            buttonHomeEditUpdate()

        else:
            reportLabel = Label(frame, text="404 - Data not found")
            reportLabel.pack()

            buttonHomeNewQR()

    def editTable():
        destroyAllObjects(frame)

        rec.entryBoxes(frame)
        
        buttonCancelEditTable()
        buttonUpdateTable()

    def updateTable():
        destroyButtons(frame)

        rec.saveTable(frame)

        buttonHomeEditUpdate()

    #region BUTTONS
    def buttonHomeEditUpdate():
        buttonHome()
        buttonEditTable()
        buttonUpdateSheet()

    def buttonHomeNewQR():
        buttonHome()
        buttonNewQRCode()

    def buttonHome():
        button_return = Button(frame, text="<< Return", command=returnHome, bd=1, relief=SUNKEN)
        button_return.pack(side = LEFT, expand = True, fill=X)
    
    def buttonEditTable():        
        button_update = Button(frame, text="Edit Table", command=editTable, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=X)
        
    def buttonCancelEditTable():
        button_update = Button(frame, text="X Cancel", command=cancelEditTable, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=X)

    def buttonUpdateTable():
        button_update = Button(frame, text="Update Table", command=updateTable, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=X)

    def buttonUpdateSheet():
        button_update = Button(frame, text="Update", command=updateSheet, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=X)

    def buttonNewQRCode():
        button_update = Button(frame, text="New Receipt", command=getQRCode, bd=1, relief=SUNKEN)
        button_update.pack(side = LEFT, expand = True, fill=X)

    



    #endregion

    frame = Frame(root)
    frame.pack(side="top", expand=True, fill='both')
    
    cam = camera.Camera()
    rec = receipt.Receipt()    

    getQRCode()
    
    return