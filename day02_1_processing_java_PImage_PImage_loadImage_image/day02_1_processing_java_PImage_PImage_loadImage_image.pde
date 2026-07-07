//day02_1_processing_java_PImage_PImage_loadImage_image
size(600,300);//視窗大小 600x300
PImage img;//宣告圖片的變數
//上網找圖片,存檔 penghu.jpg 放桌面or下載,再「拉到程式裡」
img = loadImage("penghu.jpg");//讀出圖片
image(img,0,0,600,300);//畫出圖片,在(0,0) 大小600x300
