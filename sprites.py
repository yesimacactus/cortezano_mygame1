import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

# player class

class Player1(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (200, HEIGHT/2)
        self.pos = vec(200, HEIGHT/2)
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
            # face to be accessed in the projectile classes to determine which way the projectile moves
            global face1
            face1 = "left"
        # if keystate[pg.K_s]:
        #     self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
            face1 = "right"
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        #cannot jump if in air
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                self.game.score += 1
                print(SCORE)
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
        # getting the coordinates of the player as a tuple from the indices of the vector 
        global p1
        p1 = (self.pos[0], self.pos[1] - 27)

# copied from player 1, change input keys, changed color 
class Player2(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (600, HEIGHT/2)
        self.pos = vec(600, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        global keystate
        keystate = pg.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC
        if keystate[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            global face2
            face2 = "left"
        # if keystate[pg.K_s]:
        #     self.acc.y = PLAYER_ACC
        if keystate[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            face2 = "right"
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.projectiles, True)
            if hits:
                print("you collided with an enemy...")
                self.game.HP2 += 1
                print(HP2)
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
        global p2
        p2 = (self.pos[0], self.pos[1] - 27)

# create a new platform class...

class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant


#  projectiles
class Projectile(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.width = 15
        self.height = 15
        self.image = pg.Surface((self.width,self.height))
        self.color = YELLOW
        self.image.fill(self.color)
            
        self.rect = self.image.get_rect()
        self.rect.center = p1
        self.vel = 1
        self.acc = 1
        self.cofric = 0.01

    def update(self):
        # moves
        self.rect.x += 3
        # if offscreen, death
        if self.rect.x > WIDTH:
            self.remove
        if self.rect.x < 0:
            self.remove

class Projectile2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.width = 15
        self.height = 15
        self.image = pg.Surface((self.width,self.height))
        self.color = YELLOW
        self.image.fill(self.color)
            
        self.rect = self.image.get_rect()
        self.rect.center = p2
        self.vel = 1
        self.acc = 1
        self.cofric = 0.01

    def update(self):
        self.rect.x -= 3

        if self.rect.x > WIDTH:
            self.remove
        if self.rect.x < 0:
            self.remove