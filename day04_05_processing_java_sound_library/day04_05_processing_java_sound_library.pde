//day04_05_processing_java_sound_library
import processing.sound.*; //使用 Sound 外掛

void setup(){ //設定的函式
  size(400, 400); //視窗大小
  //記得, 把你的 sound_files 目錄裡的 music.mp3 拉到程式裡
  SoundFile music = new SoundFile(this, "music.mp3");
  music.play(); //播放
}

void draw(){
  background(255, 255, 242);  
}
