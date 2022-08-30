from pygame import *
from GameSprite import *
from time import time as timer

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()   
            
        
