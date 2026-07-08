#day03_5_processing_python_countdown
#修改自day03_4_processing_python_countdown
#倒數計時,先把時間印出來囉
target = 0 #我們的目標時間
def setup(): #設定的函式
    global target #要可以修改外面的target變數
    size(500,200) #視窗大小
    mm = minute() #分鐘（現在的時間）
    ss = second() #秒鐘（現在的時間）
    target = (mm+5)*60 + ss #我們的target目標時間
    
def draw(): #畫圖的函式
    background(0) #背景黑色
    textSize(150) #字很大 150號字
    remain = target - minute()*60 - second() #剩下的秒數
    mm = remain // 60 #分鐘
    ss = remain % 60 #秒鐘
    text(nf (mm,2) + ":" + nf(ss,2), 80, 150) #接成數字
