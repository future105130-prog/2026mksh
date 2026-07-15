#day07_07_processing_python_firework_life_random
# 修改自day06_06_processing_python_firework_stroke_line_line
# 每個火花, 都有自己的生命值
def setup():
    size(500,500)
    
life = [] #每顆火花, 都有自己的生命值
r, g, b = [], [], [] #每顆,都有自己的r[i] g[i] b[i]色彩
x,y = [], [] #一開始的座標
vx,vy = [], [] #一開始也沒有速度
gx,gy = 0, 0.0098 #加速度
N = 0 #現在有幾顆花火?

def draw():
    global N
    background(0)
    ellipse(mouseX,mouseY, 10, 10) #先寫到這裡為止
    for i in range(N-1,-1,-1):
        fill(r[i], g[i], b[i]) #加這行色彩
        #ellipse(x[i],y[i], 10, 10)
        stroke(r[i], g[i], b[i]) #改成彩色的線條
        strokeWeight(5) #粗一點的線條
        line(x[i],y[i],x[i]+vx[i],y[i]+vy[i]) #畫線到下一個位子
        x[i] += vx[i]
        y[i] += vy[i]
        vx[i] += gx
        vy[i] += gx
        line(x[i],y[i],x[i]+vx[i],y[i]+vy[i]) #畫線到下一個位子
        if life[i]>0: life[i] -= 1 #減掉1點生命值
        else:
            del life[i]
            del r[i]
            del g[i]
            del b[i]
            del x[i]
            del y[i]
            del vx[i]
            del vy[i]
            N -=1
            
def mousePressed(): #mouse按下去, 要射出花火
    global life,r,g,b,x,y,vx,vy,N #要修改外面的變數
    life += [random(120,240)]*20 #生命值介於 2秒-7秒
    r += [random(256)]*20
    g += [random(256)]*20
    b += [random(256)]*20
    x += [mouseX]*20
    y += [mouseY]*20
    vx += [2*cos(PI*2/20*i)for i in range(20)]
    vy += [2*sin(PI*2/20*i)for i in range(20)]
    N += 20
