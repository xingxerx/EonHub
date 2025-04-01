import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # 0 is usually the default camera
        if not self.cap.isOpened():
            raise Exception("Could not open camera")

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def __del__(self):
        self.cap.release()
