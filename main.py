import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class VideoGame:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.display = pg.display.set_mode(RESOLUTION)
        pg.event.set_grab(True)
        self.game_clock = pg.time.Clock()
        self.delta_time = 1
        self.trigger = False
        self.event = pg.USEREVENT + 0
        pg.time.set_timer(self.event, 40)
        self.start_new_game()

    def start_new_game(self):
        self.game_map = GameMap(self)
        self.player = PlayerController(self)
        self.object_rendering_engine = GameRenderingEngine(self)
        self.ray_casting = RayCaster(self)
        self.handler = GameObjectHandler(self)
        self.player_weapon = Weapon(self)
        self.game_sound = Sound(self)
        self.path_finder = PathfindingEngine(self)
        pg.mixer.music.play(-1)

    def game_update(self):
        self.player.update()
        self.ray_casting.update()
        self.handler.updateGameState()
        self.player_weapon.update()
        pg.display.flip()
        self.time_delta = self.game_clock.tick(FRAMES_PER_SECOND)
        pg.display.set_caption(f'{self.game_clock.get_fps() :.1f}')

    def game_draw(self):
        self.object_rendering_engine.draw()
        self.player_weapon.draw()

    def event_check(self):
        self.trigger = False
        for game_event in pg.event.get():
            if game_event.type == pg.QUIT or (game_event.type == pg.KEYDOWN and game_event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif game_event.type == self.event:
                self.trigger = True
            self.player.handleSingleFireEvent(game_event)

    def game_run(self):
        while True:
            self.event_check()
            self.game_update()
            self.game_draw()


if __name__ == '__main__':
    video_game = VideoGame()
    video_game.game_run()