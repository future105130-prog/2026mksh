//day01_processing_java_void_setup_void_draw_if_mousePressed
//互動的版本
void setup(){//設定的函式
  size(500,500);//視窗
}
void draw(){//圖畫的函式
  //如果mouse按下去,就將背景設紅色
  if(mousePressed)background(255,0,0);//紅色
  else background(0,255,0);//綠色
  //否則(沒有按下去),就將背景設成綠色
}
