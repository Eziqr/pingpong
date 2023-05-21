from pygame import*
from random import randint
from time import time as timer
from time import sleep
font.init()

class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_weight):
        super().__init__()
        self.player_height = player_height
        self.player_weight = player_weight
        self.image = transform.scale(image.load(player_image), (self.player_height, self.player_weight))
        self.player_speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(gameSprite):
    def update_first(self):
        pressed = key.get_pressed()
        if pressed [K_w] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if pressed [K_s] and self.rect.y < 650:
            self.rect.y += self.player_speed


    def update_second(self):
        pressed = key.get_pressed()
        if pressed [K_UP] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if pressed [K_DOWN] and self.rect.y < 650:
            self.rect.y += self.player_speed

class Ball(gameSprite):
    def update(self):
        if 



mw = display.set_mode((1000, 800))
display.set_caption('Ping-pong')
back = transform.scale(image.load('back.jpg'), (1000, 800))
FPS = 150
game = True
finish = False

#Создание спрайтов
player_first = Player('platform1.png', 50, 400, 5, 45, 150)
player_second = Player('platform2.png', 900, 400, 5, 45, 150)
ball = Ball('ball.png', 500, 400, 3, 200, 200 )

platforms = sprite.Group()
platforms.add(player_first, player_second)

while game:
    mw.blit(back, (0, 0))
    platforms.draw(mw)
    ball.blit(mw)

    if finish != True :
        player_first.update_first()
        player_second.update_second()
        ball.update()

    for a in event.get():
        if a.type == QUIT:
            game = False


    clock = time.Clock()
    clock.tick(FPS)
    display.update()
