import cv2
import threading
import webbrowser as wb

class VideoCamera(object):
    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.data = False
        
        # check if the camera is open
        if not self.cap.isOpened():
            raise Exception("Camera did not open")
            
        else:
            print("Open camera")

        (self.grabbed, self.frame) = self.cap.read()

        if not self.grabbed:
            raise Exception("Has no camera")
        else:
            print("Camera Exist")

        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpeg', image)

        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.cap.read()

    def detect_qr_code(self):
        self.data = False
        detector = cv2.QRCodeDetector()

        _, img = self.cap.read()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)

        # check if there is a QRCode in the image
        if data:
            self.data = str(data)
            print("detect: " + self.data)
            

    def get_qr_code(self):
        if self.data:
            print(self.data)
            return self.data
        else:
            return False

def gen(camera: VideoCamera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        camera.detect_qr_code()
