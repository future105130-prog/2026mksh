#day02_8b_processing_python_PImage_array
#修改自day02_8a_processing_java_PImage_array
img = None
img2 = None

a = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

def setup():
    global img, img2
    size(500, 300)
    img = loadImage("cat.png")
    img2 = loadImage("cat2.png")

def draw():
    background(225)

    for i in range(3):      # 列(y)
        for j in range(5):  # 行(x)
            if a[i][j] == 1:
                image(img, j * 100, i * 100, 100, 100)
            elif a[i][j] == 2:
                image(img2, j * 100, i * 100, 100, 100)

def mousePressed():
    i = mouseY // 100
    j = mouseX // 100

    # 避免滑鼠點到視窗外造成索引錯誤
    if 0 <= i < 3 and 0 <= j < 5:
        a[i][j] = (a[i][j] + 1) % 3
