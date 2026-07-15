# day08_06_processing_python_black_white-go
# 黑白棋

def setup():
    size(300, 300)
    
    
a = [ [0,0,0], [0,0,0], [0,0,0] ]
def draw():
    background(188, 136, 38) # 木頭色
    line(0, 100, 300, 100) # 橫線1
    line(0, 200, 300, 200) # 橫線2
    line(100, 0, 100, 300) # 橫線1
    line(200, 0, 200, 300) # 橫線2
    for i in range(3): # 左手i 對應y座標
        for j in range(3): # 右手j 對應x座標
            if a[i][j]>0: # 黑色
                fill(0)
                ellipse( j*100+50, i*100+50, 80, 80)
            if a[i][j]<0: # 白色
                fill(255)
                ellipse( j*100+50, i*100+50, 80, 80)
                
def mousePressed():
    i = mouseY//100
    j = mouseX//100
    if mouseButton==LEFT: a[i][j] = 1 # 左鍵:黑色
    if mouseButton==RIGHT: a[i][j] = -1 # 右鍵:白色
    if mouseButton==CENTER: a[i][j] = 0 # 沒有旗子
    
    
