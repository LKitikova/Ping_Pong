
from pygame import *
from random import randint

w = 700
h = 500 

FPS = 60
clock = time.Clock()

game = True
finish = False

windows = display.set_mode((w,h))
display.set_caption("Game")

score = 0
lost = 0

#фон
backgraund = transform.scale(image.load("Background.png"),(w,h))

#единичная музыка
#music_fire = mixer.Sound("fire.ogg")

#подключить шрифты
font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 36)

#надпись победы 
win = font1.render("YOU WIN!", True, (255, 215, 0)) #желтый
#надпись поражения
lose = font1.render("YOU LOSE!", True, (255, 0, 0)) #красный
#надпись счетчика
scorelable = font2.render("Счет:" + str(score), 1, (255, 255, 255)) #белый
#надпись пропущенно
lostlable = font2.render("Пропущено:" + str(lost), 1, (255, 255, 255)) #белый

class GameSprite(sprite.Sprite):
    def __init__(self, playimage, x, y, speed, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(playimage),(self.size_x, self.size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))
    def move_x(self):
        self.rect.x += self.speed
    def move_y(self):
        self.rect.y += self.speed

class Player(GameSprite):
    def update_r(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y >= 0+30:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= h-30-165:
            self.rect.y += self.speed

    def update_l(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y >= 0+30:
            self.rect.y -= self.speed
        if key_pressed[K_s] and player.rect.y <= h-30-165:
            self.rect.y += self.speed

    

class Enemy(GameSprite):
    global finish
    
    
    def update(self):
        global lost
        if self.rect.y < h:
            self.rect.y += self.speed
        else:
            self.rect.y = 0 
            self.speed = randint(1, 3)
            self.rect.x = randint(0, w-65)
            lost = lost + 1
            
    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))       

player = Player("rocket_1.png", 30, h/2, 10, 41, 165)
player2 = Player("rocket_2.png", w-30-41, h/2, 10, 41, 165)

#money = GameSprite("treasure.png", 0.9*w, 0.9*h, 0)

#игровой цикл
while game:
    for e in event.get():
       if e.type == QUIT:
           game = False

    windows.blit(backgraund, (0,0))

    player.update_l()
    player2.update_r()
    #monsters.update()

    player.reset()
    player2.reset()
    #monsters.draw(windows)



    display.update()
    time.delay(50)
    clock.tick(FPS)