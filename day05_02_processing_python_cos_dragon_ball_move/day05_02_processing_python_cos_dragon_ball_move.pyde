#day05_02_processing_python_cos_dragon_ball_move
#想讓7顆龍珠會「轉動」
def setup(): #設定的函式
    size(400, 400)
    
def draw(): #畫圖的函式
    background(0) #背景 黑色
    for i in range(7): #七龍珠,跑7次迴圈
        # a = (PI*2/7)* i + mouseX/1000.0 #轉動, 增加角度
        a = (PI*2/7)* i + radians(frameCount)/5 #轉動
        ellipse(200+150*cos(a), 200+150*sin(a), 80, 80)
