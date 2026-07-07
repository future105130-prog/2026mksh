#day02_7b_processing_python_PImage_for
img = None #沒有東西,但有名字
def setup():
    global img #小心這一行！！！
    size(500,100)
    img = loadImage("cat.png")
    
def draw():
    for i in range(5):
        image(img, i*100,0,100,100)
