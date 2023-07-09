lst = [
    [2,3,4,5],
    ['a','b','x'],
    [True,4],
    [4,5,6.6,88,0.01]
]

# print(lst)
# print(lst[2])
# print(sum(lst[-1]))
# lst[2].append(5)
# print(lst[2])
# lst[2].insert(1,'Asad')
# print(lst[2])
# for i in lst:
#     print(i)
# print(max(lst[0]))
# for i in lst:
#     for x in i:
#         print(x)

        #HAND DETECTION
from cvzone.HandTrackingModule import HandDetector
import cv2
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)
while True:
    success,img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        # print(hand1)
        lmlist1 = hand1["lmList"]
        fingers1 = detector.fingersUp(hand1)
        s1 = str(sum(fingers1))
        cv2.putText(img,s1,(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225),4)
        pos = lmlist1[8]
        print(pos)
        if (pos[0] >= 50 and pos[0] <= 150 and pos[1] >= 50 and pos[1] <= 150):
            break


    cv2.circle(img,(120,80),50,(225,225,225),2)
    cv2.imshow("Image",img)
    if(cv2.waitKey(1)==27):
        break

#  BODY GESTURES DETECTION
from cvzone.PoseModule import PoseDetector
import cv2

# cap = cv2.VideoCapture(0)
# detector = PoseDetector()
# while True:
#     success, img = cap.read()
#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
#     if bboxInfo:
#         center = bboxInfo["center"]
#         cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
#         print(lmList)
#
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

      # ROCK,PAPER,SCISSOR GAME
# import cv2
# import mediapipe
# from cvzone.HandTrackingModule import HandDetector
#
# def start_video():
#     capture = cv2.VideoCapture(0)
#     drawing_module = mediapipe.resource_util
#     # hands_module = mediapipe.
#     detector = HandDetector(detectionCon=0.8, maxHands=2)
#
#     while True:
#         ret,frame=capture.read()
#         cv2.imshow("Rock,Paper,Scissor Game",frame)
#
#         if cv2.waitKey(1)==27:
#             break
#     cv2.destroyAllWindows()
#     capture.release()
#
#
# if __name__ == "__main__":
#     start_video()
