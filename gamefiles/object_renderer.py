import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_texture = self.get_texture('resources/textures/sky.png', (WIDTH, HEIGHT))

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        self.screen.blit(self.sky_texture, (0, 0))
        self.screen.fill((128, 128, 128), (0, HEIGHT // 2, WIDTH, HEIGHT))
        objects = self.game.raycasting.objects_to_render
        for depth, image, position in objects:
            self.screen.blit(image, position)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }