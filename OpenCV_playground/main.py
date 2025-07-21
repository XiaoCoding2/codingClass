
import cv2 #type: ignore
import numpy as np #type: ignore

img=cv2.imread("plant_pic.jpeg")

cv2.imshow("original",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("gray",gray)

cv2.imshow("edges",edges)

cv2.imwrite("edges.jpeg",edges)

cv2.waitKey(0)

cv2.destroyAllWindows()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while (True):
    (ret, frame)=cap.read() #ret=bool if can use webcam
    if (not ret):
        break
    cv2.imshow("webcam",frame)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = np.int64(cv2.goodFeaturesToTrack(gray2,50,0.01,10))
    for i in corners:
        (x,y)=i.ravel()
        cv2.circle(frame,(x,y),3,255,-1)
    edges2 = cv2.Canny(gray2, 100, 200)
    cv2.imshow("gray2",gray2)
    cv2.imshow("edges2",edges2)
    cv2.imshow("corners",frame)
    if (cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()