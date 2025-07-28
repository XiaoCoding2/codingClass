
import cv2 #type: ignore
import numpy as np #type: ignore
import time
import platform
from random import randint

#img=cv2.imread("plant_pic.jpeg")

#cv2.imshow("original",img)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray, 100, 200)

#cv2.imshow("gray",gray)

#cv2.imshow("edges",edges)

#cv2.imwrite("edges.jpeg",edges)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
WIN = "Corner‑Lab (Esc to quit)"
cv2.namedWindow(WIN)

fps=0
init_max_corners=200
init_quality_pct=2
init_min_dist=2
def nothing(_): pass
cv2.createTrackbar("maxCorners", WIN, init_max_corners, 400, nothing)
cv2.createTrackbar("quality (%)", WIN, init_quality_pct, 20, nothing)
cv2.createTrackbar("minDist", WIN, init_min_dist, 30, nothing)
lower = np.array([50, 100, 50])
upper = np.array([70, 255, 255])
while (True):
    start=time.perf_counter()
    (ret, frame)=cap.read() #ret=bool if can use webcam
    if (not ret):
        break
    cv2.imshow("webcam",frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #NOTE
    red_mask = cv2.inRange(hsv, lower, upper)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    max_corners = max(cv2.getTrackbarPos("maxCorners", WIN), 2)
    quality = max(cv2.getTrackbarPos("quality (%)", WIN), 1) / 100.0
    min_dist = max(cv2.getTrackbarPos("minDist", WIN), 1)
    #corners = np.int64(cv2.goodFeaturesToTrack(gray2,50,0.01,1))
    corners=cv2.goodFeaturesToTrack(
        gray2,
        maxCorners=max_corners,
        qualityLevel=quality,
        minDistance=min_dist
    )
    annotated = frame.copy()

    if corners is not None:
        for x,y in corners.reshape(-1,2).astype(int):
            cv2.circle(annotated,(x,y),3,255,-1)
    edges2 = cv2.Canny(gray2, 100, 200)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    c_count=0
    for cnt in contours:
        if c_count==2:break
        (x, y, w, h) = cv2.boundingRect(cnt)
        x_medium = int((x + x + w) / 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        c_count+=1

    txt=str(fps)
    cv2.putText(
        annotated, txt, (10, 25),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 4, cv2.LINE_AA
    )
    #HERSHEY_SIMPLEX
    #vis=np.hstack((gray2, edges2, corners))
    cv2.imshow("green", frame)
    cv2.imshow("gray2",gray2)
    cv2.imshow("edges2",edges2)
    cv2.imshow("corners",annotated)
    #cv2.imshow(WIN,vis)
    if (cv2.waitKey(1) & 0xFF == 27):
        break
    end=time.perf_counter()
    one_frame=end-start
    fps=1//one_frame

cap.release()
cv2.destroyAllWindows()