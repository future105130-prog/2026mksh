#day04_05_processing_python_sound_library_bad
#Help-Examples
add_library("sound")
music = None

def setup():
    global music
    size(400, 400)
    music = SoundFile(this, "music.mp3") #這行失敗了
    music.play()
    
def draw():
    background(255, 255, 242)
#程式沒有錯, 錯在「相容性」問題
