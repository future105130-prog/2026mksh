//day01_processing_java_painter_line_mouseX,mouseY,mouseX,mouseY
//簡單的小畫家
void setup(){//設定的函式
  size(500,500);//視窗500 x 500
}
void draw(){//畫圖的函式
  //如果mouse按下去
  if(mousePressed)
    line(mouseX,mouseY,mouseX,mouseY);
    //畫線 從mouse座標 到pmouse座標
}
