#day05_06_processing_python_firework_arrow
#修改自day05_05_processing_python_firework_cos_sin
#花火節的煙花:黑背景
def setup(): #設定的函式
    size(500, 500) #視窗很大 500x500 中心 (250, 250)
    
def draw():  #畫圖的函式
    background(0) #背景黑色
    stroke(255, 255, 0) #線條的筆觸是黃色
    for i in range(40):
        R = 20 + mouseX #花火的爆炸半徑, 是 20 + mouseX
        a = (PI*2/40)*i #圓/7 * i 會有不同的角度
        #line(250, 250, 250+R*cos(a), 250+R*sin(a))
        #黑色的線, 從中心(250,250)往半徑R的大圓外面射出去
        line(250+(R-20)*cos(a), 250+(R-20)*sin(a), 250+R*cos(a), 250+R*sin(a))
        #黃色的線, 從(R-20)距離, 射到R距離(往外射出去)
