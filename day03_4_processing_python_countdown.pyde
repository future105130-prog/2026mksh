#day03_4_processing_python_countdown
#倒數計時,先把時間印出來囉
def setup():
    size(500,200)
    
def draw(): #畫圖的函式
    background(0) #背景黑色
    textSize(150) #字很大 150號字
    #text("00:00", 80, 150) #測式大小、位置用的
    mm = minute() #分鐘
    ss = second() #秒鐘
    text(str (mm) + ":" + str(ss), 80, 150) #接成數字
