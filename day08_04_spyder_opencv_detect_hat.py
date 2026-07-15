# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:21:03 2026

@author: user
"""

# day08_04_spyder_opencv_detect_hat
import cv2
import numpy as np

# ==========================
# 載入人臉模型
# ==========================
face = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# ==========================
# 載入帽子(PNG透明背景)
# ==========================
hat = cv2.imread("hat.png", cv2.IMREAD_UNCHANGED)

if hat is None:
    print("找不到 hat.png")
    exit()

# ==========================
# 開啟 Webcam
# ==========================
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80,80)
    )

    for (x, y, w, h) in faces:

        # ------------------------
        # 帽子大小
        # ------------------------
        hat_width = int(w * 1.3)

        ratio = hat.shape[0] / hat.shape[1]

        hat_height = int(hat_width * ratio)

        hat_resize = cv2.resize(
            hat,
            (hat_width, hat_height)
        )

        # ------------------------
        # 帽子位置
        # ------------------------
        hat_x = x - int(w * 0.15)
        hat_y = y - hat_height + int(h * 0.25)

        # 超出畫面就跳過
        if hat_y < 0:
            continue

        if hat_x < 0:
            continue

        if hat_x + hat_width > frame.shape[1]:
            continue

        if hat_y + hat_height > frame.shape[0]:
            continue

        # ------------------------
        # Alpha Blend
        # ------------------------

        roi = frame[
            hat_y:hat_y+hat_height,
            hat_x:hat_x+hat_width
        ]

        b = hat_resize[:,:,0]
        g = hat_resize[:,:,1]
        r = hat_resize[:,:,2]
        a = hat_resize[:,:,3] / 255.0

        roi[:,:,0] = (1-a)*roi[:,:,0] + a*b
        roi[:,:,1] = (1-a)*roi[:,:,1] + a*g
        roi[:,:,2] = (1-a)*roi[:,:,2] + a*r

        frame[
            hat_y:hat_y+hat_height,
            hat_x:hat_x+hat_width
        ] = roi

    cv2.imshow("Virtual Hat", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()