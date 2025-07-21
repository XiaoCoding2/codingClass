
import cv2

for idx in range(4):
    cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
    if cap.isOpened():
        print(f"✓ Camera index {idx} opened on DirectShow")
        cap.release()
    else:
        print(f"✗ Index {idx} failed")