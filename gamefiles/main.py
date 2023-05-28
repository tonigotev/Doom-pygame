import pygame as pg
import sys
from settings import *
from map import Map
from player import Player
pg.init()


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.frame_time = 1
        self.newgame()
        self.running = True

    def newgame(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        pg.display.flip()
        self.frame_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False
                pg.quit()
                sys.exit()
    
    def run(self):
        while self.running:
            self.check_events()
            self.draw()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()
