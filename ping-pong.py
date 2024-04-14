from pygame import *

window = display.set_mode([700,500])
back = (0,255,0)
window.fill(back)
display.set_caption('Ping-pong')
Fps = 60
class GameSprite():
    def __init__(self,x,y,weight,height,speed,image_file):
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height






game = True
while game:
    display.update()