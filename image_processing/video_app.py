import cv2
import time

face_cascade = cv2.CascadeClassifier("../files/Files/haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(1)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0))
    cv2.imshow("Video", gray)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows