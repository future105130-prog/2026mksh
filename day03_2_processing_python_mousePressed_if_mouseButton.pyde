#day03_2_processing_python_mousePressed_if_mouseButton
#修改自day03_1_processing_python_textSize_text
a = [99,88,77,66,55]

def mousePressed(): #mouse按下去,對應的函式
    i = mouseX//100 #i 跟 mouseX 換算關係
    if mouseButton==LEFT: a[i]+=1 #按左鍵,a[i]加1
    else:a[i]-=1 #按右鍵,a[i]加1

def setup(): #設定的函式
    size(500,100) #視窗大小 500x100
    
def draw(): #畫圖的函式
    for i in range(5): #迴圈跑5次
        fill(255,255,242) #淡黃色、米色
        rect(i*100,0,100,100) #畫格子
        
        fill(255,0,0) #紅色的字
        textSize(80)
        text(a[i],i*100,80) #畫出a[i]
        
