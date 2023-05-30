from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POSITION 
        self.angle = PLAYER_VIEW_ANGLE

    def movement(self):
        keys = pg.key.get_pressed()

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        if keys[pg.K_LSHIFT]:
            speed = PLAYER_MOVE_SPEED  * self.game.frame_time * 2
        else:
            speed = PLAYER_MOVE_SPEED  * self.game.frame_time
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
        
        self.check_wall_collision(dx, dy)

        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROTATION_SPEED * self.game.frame_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROTATION_SPEED * self.game.frame_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.walls
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    # def draw(self):
        # pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + WIDTH * math.cos(self.angle),
        #             self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        # pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def draw_crosshair(self):
        pg.draw.line(self.game.screen, 'white', (WIDTH // 2 - 10, HEIGHT // 2),
                    (WIDTH // 2 + 10, HEIGHT // 2), 2)
        pg.draw.line(self.game.screen, 'white', (WIDTH // 2, HEIGHT // 2 - 10),
                    (WIDTH // 2, HEIGHT // 2 + 10), 2)

    # used a random website for that
    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([WIDTH // 2, HEIGHT // 2])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_MOVEMENT, min(MOUSE_MAX_MOVEMENT, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.frame_time
    
    def update(self):
        self.mouse_control()
        self.movement()
    

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_position(self):
        return int(self.x), int(self.y)