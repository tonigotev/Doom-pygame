import pygame as pg
import sys
from settings import *
from map import Map
pg.init()


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.newgame()
        self.running = True

    def newgame(self):
        self.map = Map(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()

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
