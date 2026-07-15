#day08_05_processing_python_firework_del
#想了解day07_07_processing_python_firework_life_random 的 del
#想了解 del 的意思

a = [10, 20, 30, 40] # 空白的陣列 裡面空空的

def setup(): #設定的函式
    size(600,100)
    frameRate(1) #每秒畫draw() 1次
    
def draw():
    background(0) #背景黑色
    # for i in range(len(a)): # 迴圈,把每個a[i]走一次
    for i in range(len(a)-1, -1, -1): #改成倒過來的迴圈
        fill(255) # 白色的方塊
        rect(i*80, 0, 80, 80)
        fill(255, 0, 0) # 紅色的字
        text( a[i],  i*80+40, 40)
        a[i] -= 1 # 數值慢慢變少
        if a[i] < 0: del a[i] # 要把變成0的刪掉
        
def mousePressed(): # mouse每次按下一次, 就增加1格
    a,append( int(random(5,30))) # 用 append() 加1格的數值
