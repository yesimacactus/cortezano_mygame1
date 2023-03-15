# File created by: Joshua Cortezano

import pygame as pg

from pygame.sprite import Sprite

from settings import *

vec = pg.math.Vector2

# create a player

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    def behavior(self):
        if self.rect.x > WIDTH:
            self.pos.x = 0
        if self.rect.x < -1:
            self.pos.x = WIDTH
        if self.rect.y > HEIGHT:
            self.pos.y = 0
        if self.rect.y < -1:
            self.pos.y = HEIGHT
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.behavior()
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(1,1)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def behavior(self):
        #add velocity
        # self.pos.y += self.vel.y
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
            self.vel *= -1
    def update(self): 
        self.behavior()
        self.pos += self.vel
        self.rect.center = self.pos


        

