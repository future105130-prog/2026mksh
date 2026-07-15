#day07_08_processing_python_big_eye
def setup():
    size(600,300)
    
def draw():
    background(255)
    fill(255) #白色的大眼睛
    ellipse(150,150,240,240)
    ellipse(450,150,240,240)
    
    #PVector( (mouseX-150), (mouseY-150) )
    fill(0) #黑色的瞳孔
    ellipse(150,150,120,120)
    ellipse(450,150,120,120)
