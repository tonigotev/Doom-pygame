import pygame as pg

# Stole the idea of the map from this video: https://www.youtube.com/watch?v=HQYsFshbkYw
# It's actually just an open arena, but yea xd
_ = False
game_map_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 4, _, _, _, _, _, _, _, _, 5, _, _, 1],
    [1, _, _, 4, _, _, _, _, _, _, _, _, 5, _, _, 1],
    [1, _, _, 4, _, _, _, _, _, _, _, _, 5, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, 3, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, 3, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, 3, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class GameMap:
    def __init__(self, game_instance):
        self.game = game_instance
        self.map_layout = game_map_layout
        self.world_map = {}
        self.row_count = len(self.map_layout)
        self.column_count = len(self.map_layout[0])
        self.generate_map()

    def generate_map(self):
        for row_index, row in enumerate(self.map_layout):
            for col_index, value in enumerate(row):
                if value:
                    self.world_map[(col_index, row_index)] = value

    def draw_map(self):
        [pg.draw.rect(self.game.display, 'darkgray', (position[0] * 100, position[1] * 100, 100, 100), 2)
         for position in self.world_map]