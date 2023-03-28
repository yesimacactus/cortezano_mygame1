# File created by: Joshua Cortezano

import pygame as pg

from pygame.sprite import Sprite

import random
from random import randint

from settings import *

vec = pg.math.Vector2


# create a player

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((50,50))
        # self.image = pg.transform.scale((50, 38))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        # if keystate[pg.K_s]:
        #    self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    def jump(self):
    #     # jump only if standing on a platform
    # checks left or right to see if actually on a platform
         self.rect.x += 1
         hits = pg.sprite.spritecollide(self, self.game.platforms, False)
         self.rect.x -= 1
         if hits:
             self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.rect.x > WIDTH:
            self.pos.x = 0
        if self.rect.x < 0:
            self.pos.x = WIDTH
        # if self.rect.y < 0:
            #self.pos.y = HEIGHT
        # if self.rect.y > HEIGHT:
           # self.pos.y = 0

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def behavior(self):
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
            self.vel *= -1

    def update(self):
        self.behavior()
        self.pos += self.vel
        self.rect.center = self.pos

class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 


        

