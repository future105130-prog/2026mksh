//day02_2_processing_java_void_setup_void_draw_image
PImage img;
void setup( ){//設定的函式
  size(500, 300);
  img=loadImage("cat.png");//要拉入cat.png進來
  imageMode(CENTER);//圖片的座標,設在正中心
}
void draw( ){//畫圖的函式
  background(#F0AE79);//白色背景
  image(img, mouseX,mouseY,100,100 );//秀圖片,放在mouse座標
}
