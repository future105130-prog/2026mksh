#day03_6_processing_
#修改自day03_5_processing_python_countdown
#有時候變負數,而且太快開始,而且不能暫停
#(1)小鹿:用max()找最大值max(負數,0)
#(2)鬧鐘要可以修改用mousseDragged來滑動
#(3)要可以暫停
target = 0 #我們的目標時間
target0 = 0 #現在設定 要倒數的秒數
def mouseDragged(): #左鍵用來改時間
    global target0
    target0 -= mouseY - pmouseY
    target0 = min(59, target0) #不能超過59
    target0 = max(0, target0) #不能小於0
    
def setup(): #設定的函式
    global target #要可以修改外面的target變數
    size(500,200) #視窗大小

play = False #一開始,沒有play    
def mousePressed(): #右鍵用來開始、暫停
    if mouseButton==RIGHT: play = not play

    
def draw(): #畫圖的函式
    background(0) #背景黑色
    textSize(150) #字很大 150號字
    remain = max(0,target - minute()*60 - second()) #剩下的秒數
    mm = remain // 60 #分鐘
    ss = remain % 60 #秒鐘
    text(nf (mm,2) + ":" + nf(ss,2), 80, 150) #接成數字
