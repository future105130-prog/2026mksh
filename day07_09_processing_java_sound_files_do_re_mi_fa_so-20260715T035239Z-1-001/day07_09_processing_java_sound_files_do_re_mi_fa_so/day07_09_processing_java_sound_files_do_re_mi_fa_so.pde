//day07_09_processing_java_sound_files_do_re_mi_fa_so
import processing.sound.*; //使用Processing的Sound外掛
SoundFile sound1, sound2, sound3, sound4, sound5; //5個檔案
void setup(){ //設定
  size(500, 100);
  sound1 = new SoundFile(this, "do.wav");
  sound2 = new SoundFile(this, "re.wav");
  sound3 = new SoundFile(this, "mi.wav");
  sound4 = new SoundFile(this, "fa.wav");
  sound5 = new SoundFile(this, "so.wav");
}
void draw(){
  //...
}
void keyPressed() { //按下鍵盤的1,2,3,4,5可發出聲音
  if (key=='1') sound1.play(); //小心切換輸入法
  if (key=='2') sound2.play();
  if (key=='3') sound3.play();
  if (key=='4') sound4.play();
  if (key=='5') sound5.play();
}
