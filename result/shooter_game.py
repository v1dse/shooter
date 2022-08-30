#Создай собственный Шутер!
from time import time as timer 
from random import randint
from turtle import update, window_width
from pygame import *
from Enemy import Enemy
from GameSprite import GameSprite
from bullet import Bullet
from Player import Player


window = display.set_mode((1366,766))
display.set_caption('Shooter')
background = transform.scale(image.load('galaxy.jpg'), (1366,766))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire_sound = mixer.Sound('fire.ogg')

font.init()
font1 = font.SysFont('ariale', 35)
win = font1.render('YOU WIN!', True, (255,215,0))
lose = font1.render('YOU LOSE!', True, (180,0,0))

lost = 0
score = 0

y = randint(0,700)

win_width = 1366
win_height = 766


rocket = Player('rocket.png',500,650,8,60,90,1366,766,window)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png',randint(80, win_width - 80), -40,randint(1,5),80,50,win_width, win_height,window)
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(1,3):
    asteroid = Enemy('asteroid.png',randint(80,win_width-80),-40,randint(1,3),80,50,win_width,win_height,window)
    asteroids.add(asteroid)

bullet = 30
bullets = sprite.Group()
game = True
finish = False
clock = time.Clock()
FPS = 120
speed = 6 

old_time = 0
new_time = 0

new_time = timer() 

if bullet <= 0:
    old_time = timer
    if old_time - new_time >= 1:
        bullet = 30



while game:

    if not finish:
        window.blit(background,(0,0))
        rocket.reset()
        lost_text = font1.render('Пропущенно'+ str(lost), True, (255,215,0))
        window.blit(lost_text, (10,10))
        score_text = font1.render('Попадания'+ str(score), True, (255,215,0))
        window.blit(score_text, (10,40))
        rocket.update()
        monsters.update()
        bullets.update()
        asteroids.update()
        monsters.draw(window)
        asteroids.draw(window)
        bullets.draw(window)
        for m in monsters:
            lost += m.update()


        collides = sprite.groupcollide(monsters,bullets,True,True)
        for c in collides:
                score = score + 1
                monster = Enemy('ufo.png',randint(80, win_width - 80), -40,randint(1,5),80,50,win_width, win_height,window)
                monsters.add(monster)

        collide = sprite.groupcollide(asteroids,bullets,False,True)
            
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key ==  K_SPACE and bullet != 0:
                fire_sound.play()
                bullets.add(rocket.fire())
                bullet -= 1
                 

    if sprite.spritecollide(rocket,monsters,False) or lost >= 10 or sprite.spritecollide(rocket,asteroids,False):
        finish = True
        window.blit(lose,(600,400))

    if score >= 10:
        finish = True
        window.blit(win,(600,400))



    clock.tick(FPS)
    display.update()