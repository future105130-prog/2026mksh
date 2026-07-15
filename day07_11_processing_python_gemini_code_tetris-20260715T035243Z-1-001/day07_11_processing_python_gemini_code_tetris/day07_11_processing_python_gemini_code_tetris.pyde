#day07_11_processing_python_gemini_code_tetris
#gemini:想要寫一個 Processing 的 Python Mode 的程式, 可以模仿「俄羅斯方塊」的遊戲,請給我程式
#遊戲視窗與網格設定
import random

# 遊戲地圖常數
COLS = 10
ROWS = 20
BLOCK_SIZE = 30

# 7 種經典方塊形狀 (以 2D 矩陣表示)
SHAPES = [
    [[1, 1, 1, 1]],                         # I
    [[1, 1, 1], [0, 1, 0]],                 # T
    [[1, 1, 1], [1, 0, 0]],                 # L
    [[1, 1, 1], [0, 0, 1]],                 # J
    [[1, 1], [1, 1]],                       # O
    [[1, 1, 0], [0, 1, 1]],                 # Z
    [[0, 1, 1], [1, 1, 0]]                  # S
]

# 對應方塊的 RGB 顏色
COLORS = [
    (0, 255, 255),   # Cyan
    (160, 32, 240),  # Purple
    (255, 165, 0),   # Orange
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 0, 0),     # Red
    (0, 255, 0)      # Green
]

def setup():
    size(300, 650) # 寬 300 (10格 * 30px)，高 650 (其中 50 留給分數顯示)
    frameRate(60)
    reset_game()

def reset_game():
    global grid, current_shape, current_color, px, py, score, game_over, fall_delay, last_fall_time
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)] # 0 代表空白，非 0 儲存該格顏色 RGB 元組
    score = 0
    game_over = False
    fall_delay = 500 # 方塊自動下落的時間間隔 (毫秒)
    last_fall_time = millis()
    spawn_piece()

def spawn_piece():
    global current_shape, current_color, px, py, game_over
    idx = random.randint(0, len(SHAPES) - 1)
    current_shape = SHAPES[idx]
    current_color = COLORS[idx]
    # 設定新方塊初始位置 (畫面上方中間)
    px = COLS // 2 - len(current_shape[0]) // 2
    py = 0
    
    # 如果一生成就碰撞，代表方塊堆滿，遊戲結束
    if check_collision(current_shape, px, py):
        game_over = True

def draw():
    global last_fall_time, game_over
    background(40)
    
    # 畫出遊戲邊界線
    stroke(100)
    line(0, ROWS * BLOCK_SIZE, width, ROWS * BLOCK_SIZE)
    
    if not game_over:
        # 自動下落計時
        if millis() - last_fall_time > fall_delay:
            move_down()
            last_fall_time = millis()
    
    draw_grid()
    draw_current_piece()
    draw_score()
    
    if game_over:
        draw_game_over()

# 繪製已經固定在地圖上的方塊與背景網格
def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r][c]
            if val != 0:
                fill(val[0], val[1], val[2])
                stroke(0)
                rect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            else:
                noFill()
                stroke(50)
                rect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

# 繪製目前操控中的下落方塊
def draw_current_piece():
    if game_over:
        return
    fill(current_color[0], current_color[1], current_color[2])
    stroke(0)
    for r in range(len(current_shape)):
        for c in range(len(current_shape[r])):
            if current_shape[r][c] != 0:
                rect((px + c) * BLOCK_SIZE, (py + r) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

# 繪製底部得分板
def draw_score():
    fill(255)
    textSize(20)
    textAlign(CENTER, CENTER)
    text("Score: " + str(score), width / 2, ROWS * BLOCK_SIZE + 25)

# 繪製遊戲結束畫面
def draw_game_over():
    fill(0, 0, 0, 180)
    rect(0, 0, width, height)
    fill(255, 0, 0)
    textSize(32)
    textAlign(CENTER, CENTER)
    text("GAME OVER", width / 2, height / 2 - 20)
    fill(255)
    textSize(16)
    text("Press 'R' to Restart", width / 2, height / 2 + 30)

# 碰撞偵測函式
def check_collision(shape, x_offset, y_offset):
    for r in range(len(shape)):
        for c in range(len(shape[r])):
            if shape[r][c] != 0:
                grid_x = x_offset + c
                grid_y = y_offset + r
                
                # 檢查是否超出左右或底部邊界
                if grid_x < 0 or grid_x >= COLS or grid_y >= ROWS:
                    return True
                # 檢查是否與地圖上已固定的方塊碰撞
                if grid_y >= 0 and grid[grid_y][grid_x] != 0:
                    return True
    return False

# 讓方塊往下移動一格
def move_down():
    global py
    if not check_collision(current_shape, px, py + 1):
        py += 1
    else:
        lock_piece()
        clear_lines()
        spawn_piece()

# 將當前方塊固定到地圖網格中
def lock_piece():
    for r in range(len(current_shape)):
        for c in range(len(current_shape[r])):
            if current_shape[r][c] != 0:
                grid_y = py + r
                grid_x = px + c
                if 0 <= grid_y < ROWS and 0 <= grid_x < COLS:
                    grid[grid_y][grid_x] = current_color

# 消行檢測與得分
def clear_lines():
    global grid, score
    # 過濾掉填滿 10 格的行
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    cleared = ROWS - len(new_grid)
    if cleared > 0:
        score += cleared * 100
        # 在頂部補上新的空行
        for _ in range(cleared):
            new_grid.insert(0, [0 for _ in range(COLS)])
        grid = new_grid

# 旋轉矩陣 (將方塊順時針旋轉 90 度)
def rotate_shape(shape):
    return [list(x) for x in zip(*shape[::-1])]

# 鍵盤控制監聽
def keyPressed():
    global px, py, current_shape, game_over
    if game_over:
        if key == 'r' or key == 'R':
            reset_game()
        return
        
    if keyCode == LEFT:
        if not check_collision(current_shape, px - 1, py):
            px -= 1
    elif keyCode == RIGHT:
        if not check_collision(current_shape, px + 1, py):
            px += 1
    elif keyCode == DOWN:
        move_down()
    elif keyCode == UP:
        # 嘗試旋轉，並檢查旋轉後是否會碰撞，不會碰撞才套用
        rotated = rotate_shape(current_shape)
        if not check_collision(rotated, px, py):
            current
