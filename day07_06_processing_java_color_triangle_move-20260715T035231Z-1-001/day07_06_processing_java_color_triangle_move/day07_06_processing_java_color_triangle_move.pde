//day07_06_processing_java_color_triangle_move
void setup(){
  size(500,500,P2D); //中心點 250,250
}

void draw(){
  background(0);
  beginShape();
  float a = radians(frameCount);
  fill(255, 0, 0);
  vertex(250+cos(a)*200, 250+sin(a)*200);
  
  fill(0,255,0);
  vertex(250+cos(a+PI*2/3)*200,250+sin(a+PI*2/3)*200);
  
  fill(0,0,255);
  vertex(250+cos(a+PI*2/3*2)*200,250+sin(a+PI*2/3*2)*200);
  endShape();
}
