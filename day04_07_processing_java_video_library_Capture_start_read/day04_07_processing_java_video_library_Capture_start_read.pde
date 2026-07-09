//day04_07_processing_java_video_library_Capture_start_read
import processing.video.*;

Capture cam;

void setup(){
  size(640, 480);
  cam = new Capture(this, 640, 480);
  cam.start();
}
void draw(){
 if (cam.available()) cam.read();
 image(cam, 0, 0);
}
