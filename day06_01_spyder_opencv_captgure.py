#day06_01_spyder_opencv_captgure.py
#從ChatGPT 得到程式
#修改自day04_07_processing_java_video_library_Capture_start_read
import cv2

# 開啟第一台攝影機
cap = cv2.VideoCapture(0) #0:第一台 :第二台...


# 是否成功開啟
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

while True: #迴圈會一直跑,直到有break跳開結束

    # 取得一張影像
    ret, frame = cap.read()

    if not ret: #若沒有成功,就離開
        break

    # 顯示畫面
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) == 27: #按Esc 離開(改成按Esc 離開)
        break

   

cap.release() #把camera 正確關閉(收尾很重要)
cv2.destroyAllWindows() #把剛剛開啟的 OpenCV 視窗全部關掉