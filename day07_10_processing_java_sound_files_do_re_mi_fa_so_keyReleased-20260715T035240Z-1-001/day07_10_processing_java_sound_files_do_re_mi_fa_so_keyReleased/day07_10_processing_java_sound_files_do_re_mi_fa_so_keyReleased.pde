//day07_10_processing_java_sound_files_do_re_mi_fa_so_keyReleased
//修改自day07_09_processing_java_sound_files_do_re_mi_fa_so
import processing.sound.*; //使用Processing的Sound外掛
SoundFile sound1, sound2, sound3, sound4, sound5; //5個檔案
void setup(){ //設定
  size(500, 100);
  sound1 = new SoundFile(this, "do.wav");
  sound2 = new SoundFile(this, "re.wav");
  sound3 = new SoundFile(this, "mi.wav");
  sound4 = new SoundFile(this, "fa.wav");
  sound5 = new SoundFile(this, "so.wav");
} //要記得拉入 do re mi fa so 的 wav 檔進程式
int [] a = {0,0,0,0,0}; //a[i] 有沒有按下去?
void draw(){
  for(int i=0; i<5; i++){
    if(a[i]==1) fill(128); //有按下去, 灰色
    else fill(225); //沒有按下去, 白色
    rect(i*100,0,100,100);
  }
}
void keyReleased(){ //放開鍵盤的鍵
  if (key=='1') a[0]=0;
  if (key=='2') a[1]=0;
  if (key=='3') a[2]=0;
  if (key=='4') a[3]=0;
  if (key=='5') a[4]=0;
}

void keyPressed() { //按下鍵盤的1,2,3,4,5可發出聲音
  if (key=='1'){a[0]=1; sound1.play();} //小心切換輸入法
  if (key=='2'){a[1]=1; sound2.play();}
  if (key=='3'){a[2]=1; sound3.play();}
  if (key=='4'){a[3]=1; sound4.play();}
  if (key=='5'){a[4]=1; sound5.play();}
}
