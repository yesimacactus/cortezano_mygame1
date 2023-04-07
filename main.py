# File created by: Joshua Cortezano
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# GOALS!!!!!!!!!!!!!!!!!!!!!
# make 2 players and shoot at each other so that if shot too many times, death happens

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.player1 = Player1(self)
        self.player2 = Player2(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        #self.proj1 = Projectile()

        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)
        
        # for wall in WALL_LIST:
          #  w = Wall(*wall)
            #self.all_sprites.add(w)
            # self.walls.add(w)







        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player1.jump()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player2.jump()
# adding projectiles if either s or down is pressed, but only if they are pressed
            global fired

            fired = False
            keystate = pg.key.get_pressed()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    fired = True
            if keystate[pg.K_DOWN]:
                if event.key == pg.K_DOWN:
                    fired = True

            if fired:
                proj = Projectile()
                self.projectiles.add(proj)
                self.all_sprites.add(proj)

               
                    

    def update(self):
        self.all_sprites.update()
        if self.player1.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player1, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player1.pos.y = hits[0].rect.top
                    self.player1.vel.y = -PLAYER_JUMP
                else:
                    self.player1.pos.y = hits[0].rect.top
                    self.player1.vel.y = 0
        if self.player2.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player2.pos.y = hits[0].rect.top
                    self.player2.vel.y = -PLAYER_JUMP
                else:
                    self.player2.pos.y = hits[0].rect.top
                    self.player2.vel.y = 0

    


    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()