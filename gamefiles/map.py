import pygame as pg

_=False

class Map:
    def __init__(self, game):
        self.game = game
        self.bool_map = [
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
        self.walls = {}
        self.set_walls()

    def set_walls(self):
        for j, row in enumerate(self.bool_map):
            for i, boolvalue in enumerate(row):
                if boolvalue:
                    self.walls[(i, j)] = boolvalue

    def draw(self):
        for (i, j), value in self.walls.items():
            if value:
                pg.draw.rect(self.game.screen, 'darkgray', (i * 100, j * 100, 100, 100), 2)