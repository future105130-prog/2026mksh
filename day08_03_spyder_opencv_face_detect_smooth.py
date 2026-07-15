# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:04:01 2026

@author: user
"""

#day08_03_spyder_opencv_face_detect_smooth
#prompt:延伸前面偵測人臉畫線條的版本。偵測face detect出來的人臉會有點抖動,為什麼?請問要如何改成沒有抖動的版本

import cv2

# -----------------------------
# 載入 Haar Cascade 人臉模型
# -----------------------------
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -----------------------------
# 開啟 Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

# -----------------------------
# 儲存上一幀的人臉位置
# -----------------------------
last_x = None
last_y = None
last_w = None
last_h = None

# 平滑係數
alpha = 0.2

# -----------------------------
# 主迴圈
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("讀不到影像")
        break

    # 轉成灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉
    faces = face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80, 80)
    )

    # 若有偵測到人臉
    if len(faces) > 0:

        # 只取第一張人臉
        (x, y, w, h) = faces[0]

        # 第一次偵測
        if last_x is None:
            last_x = x
            last_y = y
            last_w = w
            last_h = h

        # EMA 平滑
        last_x = int((1 - alpha) * last_x + alpha * x)
        last_y = int((1 - alpha) * last_y + alpha * y)
        last_w = int((1 - alpha) * last_w + alpha * w)
        last_h = int((1 - alpha) * last_h + alpha * h)

        # 畫矩形
        cv2.rectangle(
            frame,
            (last_x, last_y),
            (last_x + last_w, last_y + last_h),
            (0, 255, 0),
            2
        )

    # 顯示畫面
    cv2.imshow("Face Detection (Smooth)", frame)

    # Esc 離開
    if cv2.waitKey(1) == 27:
        break

# -----------------------------
# 結束
# -----------------------------
cap.release()
cv2.destroyAllWindows()
