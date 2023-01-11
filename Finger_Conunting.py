import cv2
import time
import Hand_Tracking_Module_ as htm

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 420)
cTime = 0
pTime = 0

detector = htm.handDetector(detectionCon=0.8)

tiIds = [4, 8, 12, 16, 20]

while True:
    Success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPositon(img)

    if lmList:
        fingers = []

        # Thumb
        if lmList[tiIds[0]][1] > lmList[tiIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):

            if lmList[tiIds[id]][2] < lmList[tiIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        totalFingers = fingers.count(1)
        # print(totalFingers)
        cv2.rectangle(img, (435, 220), (580, 410), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (460, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS:{int(fps)}", (10, 25), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 255), 2)

    cv2.imshow("Finger Counting", img)
    key = cv2.waitKey(1)

    if key == 80 or key == 113:
        break

cap.release()
cv2.destroyAllWindows()

print("Code Completed!")