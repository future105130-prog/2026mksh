# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:39:54 2026

@author: user
"""

#day08_02_spyder_opencv_face_detection
#我想延伸剛剛的程式碼,讓鏡頭能夠偵測到人臉,用線條或圓形把臉框起來,請問要在做什麼修改?

import cv2

# 載入人臉模型
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # 轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉
    faces = face.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    # 畫框
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) == 27:   # Esc
        break

cap.release()
cv2.destroyAllWindows()