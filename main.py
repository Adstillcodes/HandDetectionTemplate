from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(maxHands=2, detectionCon=0.7)

while True:
    success, img = cap.read()

    img = detector.findHands(img)



    cv2.imshow("HandDetector", img[1])
    cv2.waitKey(1)