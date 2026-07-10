#day05_01_processing_python_cos_sin_dragon_ball
#國中教 cos() sin() 陳冠宏問: 學cos()sin()有什麼用? 
#Q: 上市場,會說:老闆,我要買冬瓜 cos(60) 西瓜 sin(30)嗎?
#A: 老師在大學 3D 電腦圖學 很有用
size(400,400) #視窗大小 400x400, 正中心 (200,200)
ellipse(200, 200, 300, 300) #圓 正中心(200,200) 圓的大小 300x300

for i in range(7): #七龍珠 有7個龍珠
    a = (PI*2/7)*i #對應的角度 a 是1/7 個圓*i
    ellipse(200+150*cos(a), 200+150*sin(a), 80, 80) #畫出 80x80 的小圓
    #圓心 200 半徑 150 x座標對應 cos(a)
    #圓心 200 半徑 150 y座標對應 sin(a)
