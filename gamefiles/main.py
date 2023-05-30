from sprite import *
from raycasting import RayCasting
from object_renderer import *
from player import Player
from settings import *
import pygame as pg
from map import Map
import sys
pg.init()


class Game():
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.frame_time = 1
        self.running = True
        self.newgame()

    def newgame(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.sprite = Sprite(self)

    def update(self):
        self.frame_time = self.clock.tick(FRAMES_PER_SECOND)
        pg.display.set_caption(f'{self.clock.get_fps()}')
        self.sprite.update()
        self.raycasting.update()
        self.player.update()
        pg.display.flip()

    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        self.player.draw_crosshair()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
                sys.exit()
                pg.quit()
    
    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()  

if __name__ == '__main__':
    game = Game()
    game.run()
