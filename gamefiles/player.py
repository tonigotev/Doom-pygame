from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        keys = pg.key.get_pressed()

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        if keys[pg.K_LSHIFT]:
            speed = PLAYER_SPEED * self.game.frame_time * 2
        else:
            speed = PLAYER_SPEED * self.game.frame_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        self.x += dx
        self.y += dy

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.frame_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.frame_time
        self.angle %= math.tau

        # # diag move correction
        # if num_key_pressed:
        #     dx *= self.diag_move_corr
        #     dy *= self.diag_move_corr

        # self.check_wall_collision(dx, dy)

        # # if keys[pg.K_LEFT]:
        # #     self.angle -= PLAYER_ROT_SPEED * self.game.frame_time
        # # if keys[pg.K_RIGHT]:
        # #     self.angle += PLAYER_ROT_SPEED * self.game.frame_time
        # self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angle),
                    self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)
    
    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def mapposition(self):
        return int(self.x), int(self.y)