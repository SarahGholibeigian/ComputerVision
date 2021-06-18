import cv2
import numpy as np

# open Xming!
# first change environment to pycv
# second run <export DISPLAY=:0> in Ubuntu

cap = cv2.VideoCapture('./assets/video.mp4')

# webcam is not working in WSL
# cap = cv2.VideoCapture(-1)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'We are Great!', (10, height - 100), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("frame", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()