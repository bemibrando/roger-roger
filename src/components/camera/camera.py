import cv2

class Camera:
    # Class attribute
    windowName = "B1 - Camera"
    cap = ""

    def __init__(self, name = "B1 - Camera"):
        self.windowName = name

    def open_camera(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not self.cap.isOpened():
            print("Camera did not open")
            exit()

    
    def just_open_camera(self):

        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Has no camera")
                break

            cv2.imshow(self.windowName, frame)

            # get user input key to close
            key = cv2.waitKey(1)
            if key == 27:
                break

            # when click at "x", close
            if cv2.getWindowProperty(self.windowName, cv2.WND_PROP_VISIBLE) < 1:
                break
        
        self.close_camera()
        return

    def close_camera(self):
        cv2.destroyAllWindows()
        self.cap.release()
        print("Camera closed")
        return

    def read_qr_code(self):
        self.windowName = "B1 - Read QR Code"
        
        self.open_camera()
        detector = cv2.QRCodeDetector()
        
        while True:
            _, frame = self.cap.read()
            cv2.imshow(self.windowName, frame)

            # detect and decode
            data, bbox, _ = detector.detectAndDecode(frame)

            # check if there is a QRCode in the image
            if data:
                return str(data)
            
            # get user input key to close
            key = cv2.waitKey(1)
            if key == 27:
                break

            # when click at "x", close
            if cv2.getWindowProperty(self.windowName, cv2.WND_PROP_VISIBLE) < 1:
                break
            
        return