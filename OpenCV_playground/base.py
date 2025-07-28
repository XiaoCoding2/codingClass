
import cv2 # type: ignore

CAP_IDX   = 0
BACKEND   = cv2.CAP_DSHOW           # use CAP_AVFOUNDATION on macOS
WINDOW    = "Stage‑1 Demo (Esc to quit)"

cap = cv2.VideoCapture(CAP_IDX, BACKEND)
if not cap.isOpened():
    raise RuntimeError(f"Camera {CAP_IDX} failed")

cv2.namedWindow(WINDOW)

# ---------------------- YOUR CODE STARTS HERE ----------------------
# Paste only the processing portion for each lesson below this line
while True:
    ok, frame = cap.read()
    if not ok:
        break

    # … add processing & drawing here, call cv2.imshow() …

    h, w = frame.shape[:2]
    cv2.rectangle(frame, (10, 10), (w-10, h-10), (0, 0, 255), 2)

    # Cross‑hair in the center
    center = (w // 2, h // 2)
    cv2.line(frame, (center[0]-40, center[1]), (center[0]+40, center[1]), (0,255,0), 2)
    cv2.line(frame, (center[0], center[1]-40), (center[0], center[1]+40), (0,255,0), 2)

    # Circle around your head‑ish area (adjust radius)
    cv2.circle(frame, center, 120, (255, 0, 0), 2)

    # Label text
    cv2.putText(frame, "Live HUD Demo", (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

    cv2.imshow(WINDOW, frame)

    if cv2.waitKey(1) & 0xFF == 27:          # Esc
        break

cap.release()
cv2.destroyAllWindows()