#day05_03_processing_python_cos_sin_pikmin
#抽獎勵(金色花苗) 會有轉轉的花苗
def setup():
    size(400, 300) #400x300 的一半 (200,150)
    #background(54, 39, 155)
    
def draw():
    background(54, 39, 155) #背景 深藍色
    for i in range(6):
        a = (PI*2/ 6) * i + radians(frameCount)*(mouseX/10+1)
        #rect(200+100*cos(a)-25 ,150+80*sin(a)-25, 50, 50) #手動移25
        rectMode(CENTER) #改成直接對齊「正中心」
        rect( 200+100*cos(a), 150+80*sin(a),  50,  50)
        
