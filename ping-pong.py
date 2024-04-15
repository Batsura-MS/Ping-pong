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
ball = GameSprite('ball.png',100,100,5,75,75)  
game = True
finish = False
speed_x = 5
speed_y = 5
font.init()
font1 = font.Font(None,100)
lose1 = font1.render('Player 1 lose!!!',True,(255,0,0))
lose2 = font1.render('Player 2 lose!!!',True,(255,0,0))
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
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= 425 or ball.rect.y < 0:
            speed_y*= -1
        if sprite.collide_rect(platform1,ball) or sprite.collide_rect(platform2,ball):
            speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(120,200))
    if ball.rect.x >= 630:
        finish = True
        window.blit(lose2,(120,200))
    clock.tick(Fps)
    display.update()
