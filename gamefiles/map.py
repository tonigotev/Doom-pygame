import pygame as pg

_=False

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1],
            [1, _, 1, 1, 1, _, _, 1, 1, _, _, 1, _, _, 1, 1],
            [1, _, _, _, 1, _, _, 1, _, _, _, 1, _, _, _, 1],
            [1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, 1, _, _, _, _, _, _, 1, _, _, _, 1],
            [1, _, _, _, _, _, 1, 1, 1, _, _, 1, 1, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def draw(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    pg.draw.rect(self.game.screen, 'darkgray', (i * 100, j * 100, 100, 100), 2)