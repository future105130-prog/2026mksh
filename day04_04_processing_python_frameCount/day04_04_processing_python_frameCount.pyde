#day04_04_processing_python_frameCount
#希望了解day04_03 的 frameCount 是什麼意思

def setup():
    size(400, 400)
    #frameRate(5) #希望 draw() 跑慢一點, 1秒5次
    #等一下會刪掉 正常是1秒畫60次
    
#如果想知道現在是第幾次執行 void draw() 要用 t 來數
t = 1 # 第1行, 宣告 t 變數
def draw():
    global t # 第2行, 要認識外面的 t
    
    background(0)
    textSize(100)
    textAlign(CENTER, CENTER)
    text(frameCount, 200, 100) #值會跟4行的t一樣
    
    text(t, 200, 200) #第3行, 試著畫出 t 的值
    t += 1 #第4行, 每次結束時 t 會「加1」
    
    text(frameCount//60, 200, 300) #每秒60次, //60變秒
