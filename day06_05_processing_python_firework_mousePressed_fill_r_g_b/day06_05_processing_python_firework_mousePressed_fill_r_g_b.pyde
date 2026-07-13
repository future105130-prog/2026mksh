#day06_05_processing_python_firework_mousePressed_fill_r_g_b
#修改自day06_04_processing_python_firework_mousePressed_many
#想要做出互動的花火(煙火), 而且mouse 可點很多次
def setup():
    size(500,500)
    
r, g, b = [], [], [] #每顆,都有自己的r[i] g[i] b[i]色彩
x,y = [], [] #一開始的座標
vx,vy = [], [] #一開始也沒有速度
gx,gy = 0, 0.0098 #加速度
N = 0 #現在有幾顆花火?

def draw():
    background(0)
    ellipse(mouseX,mouseY, 10, 10) #先寫到這裡為止
    for i in range(N):
        fill(r[i], g[i], b[i]) #加這行色彩
        ellipse(x[i],y[i], 10, 10)
        x[i] += vx[i]
        y[i] += vy[i]
        vx[i] += gx
        vy[i] += gx
            
def mousePressed(): #mouse按下去, 要射出花火
    global r,g,b,x,y,vx,vy,N #要修改外面的變數
    r += [random(256)]*20
    g += [random(256)]*20
    b += [random(256)]*20
    x += [mouseX]*20
    y += [mouseY]*20
    vx += [3*cos(PI*2/20*i)for i in range(20)]
    vy += [3*sin(PI*2/20*i)for i in range(20)]
    N += 20
