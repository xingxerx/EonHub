import cv2

def capture_frame():
    cap = cv2.VideoCapture(0)  # 0 is usually the default camera
    ret, frame = cap.read()
    cap.release()
    return frame
