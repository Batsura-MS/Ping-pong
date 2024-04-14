from pygame import *

window = display.set_mode([700,500])
back = (0,255,0)
window.fill(back)
display.set_caption('Ping-pong')
Fps = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,image_file,x,y,speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(image_file),(width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed   
platform1 = Player('platform1.png',20,150,5,44,196)  
platform2 = Player('platform2.png',640,150,5,44,196)  
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        platform1.reset()
        platform2.reset()
        platform1.update_l()
        platform2.update_r()
    clock.tick(Fps)
    display.update()
