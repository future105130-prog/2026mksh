#day07_08_processing_python_big_eye2
def setup():
    size(600,300)
    
def draw():
    background(255)
    fill(255) #白色的大眼睛
    ellipse(150,150,240,240)
    ellipse(450,150,240,240)
    
    fill(0) #黑色的瞳孔
    d = PVector( (mouseX-150), (mouseY-150) )
    if d.mag() > 60:
        d = d.normalize().mult(60)
    ellipse(150+d.x,150+d.y,120,120)
    d = PVector( (mouseX-450), (mouseY-150) )
    if d.mag() > 60:
        d = d.normalize().mult(60)
    ellipse(450+d.x,150+d.y,120,120)
