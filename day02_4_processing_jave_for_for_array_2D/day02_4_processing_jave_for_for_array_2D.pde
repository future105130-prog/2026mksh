//day02_4_processing_jave_for_for_array_2D
PImage img;
int [][] a = {
  {1,1,1,1,1},
  {1,1,1,1,1},
  {1,1,1,1,1}   };
void mousePressed(){
  int i = mouseY/100, j=mouseX/100;
  if(mouseButton==LEFT) a[i][j] = 0;//左鍵消失
  else a[i][j] = 1;//右鍵長回來
}
void setup(){
  size(500,300);
  img = loadImage("cat.png");
}//要記得,把cat.png圖檔,拉入程式裡
void draw( ){
  background(225);
  for(int i=0;i<3; i++){//左手i 對應y
    for(int j=0;j<5; j++ ){//右手j 對應x
      if(a[i][j]==1) image(img,j*100,i*100,100,100 );
    }         //x座標, y座標
  }
}
