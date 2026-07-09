# day_04_03_processing_python_countdown_mouseDragged
#修改自day_04_02_processing_python_countdown_start
#希望 mouse 左鍵  dragged 拖曳 改時間
def setup():
    size(400,400)
    
start = False #沒有開始
t = 10
def draw():
    global t
    background(0)
    textSize(300)
    textAlign(CENTER,CENTER)
    text(t,200,200)
    if start and frameCount%60==0 and t>0: t -= 1
    
def mousePressed():
    global start
    if mouseButton==RIGHT: start = not start #start = True
    
def mouseDragged(): #mouse往上滑、往下滑
    global t #會修改t的值
    t -= mouseY - pmouseY #向量的差
    t = max(0, min(59, t) ) #限制在 0...59之間
