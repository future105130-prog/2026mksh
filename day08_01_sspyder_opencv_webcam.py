# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#day08_01_sspyder_opencv_webcam
#我們想在spyder裡使用opencv讀入webcam視訊鏡頭的畫面,即時更新。要做哪些步驟?有哪些可能卡住的地方?
#因為中文的注音輸入法會卡住q的鍵,可以改成按Esc鍵嗎
import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("讀不到影像")
        break

    cv2.imshow("My Webcam", frame)

    key = cv2.waitKey(1)

    # 按 Esc 離開
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()