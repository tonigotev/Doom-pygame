import pygame as pg
from settings import *
import os
from collections import deque


class Sprite:
    def __init__(self, game_instance, sprite_path='resources/sprites/static_sprites',
                 sprite_position=(10.5, 3.5), scale_factor=0.7, vertical_shift=0.27):
        self.game = game_instance
        self.player = game_instance.player
        self.sprite_x, self.sprite_y = sprite_position
        self.sprite_image = pg.image.load(sprite_path).convert_alpha()
        self.image_width = self.sprite_image.get_width()
        self.image_half_width = self.image_width // 2
        self.image_ratio = self.image_width / self.sprite_image.get_height()
        self.delta_x, self.delta_y, self.angle_to_player, self.screen_x, self.distance, self.normalized_distance = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.sprite_scale = scale_factor
        self.sprite_height_shift = vertical_shift 

    def calculate_sprite_projection(self):
        projection = SCREEN_DISTANCE / self.normalized_distance * self.sprite_scale
        projection_width, projection_height = projection * self.image_ratio, projection

        scaled_image = pg.transform.scale(self.sprite_image, (projection_width, projection_height))

        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.sprite_height_shift
        position_on_screen = self.screen_x - self.sprite_half_width, HALF_HEIGHT - projection_height // 2 + height_shift

        self.game.raycasting.objects_to_render.append((self.normalized_distance, scaled_image, position_on_screen))

    def calculate_sprite_parameters(self):
        self.delta_x = self.sprite_x - self.player.x
        self.delta_y = self.sprite_y - self.player.y
        self.angle_to_player = math.atan2(self.delta_y, self.delta_x)

        delta_angle = self.angle_to_player - self.player.angle
        # fix the angle if it's out of the player's FOV - youtube tutorial helped me with this
        if (self.delta_x > 0 and self.player.angle > math.pi) or (self.delta_x < 0 and self.delta_y < 0):
            delta_angle += math.tau

        delta_in_rays = delta_angle / ANGLE_BETWEEN_RAYS
        self.screen_x = (HALF_NUMBER_OF_RAYS + delta_in_rays) * PIXEL_SCALE

        # fix the fisheye effect - GPT helped me with this
        self.distance = math.hypot(self.delta_x, self.delta_y)
        self.normalized_distance = self.distance * math.cos(delta_angle)
        if -self.image_half_width < self.screen_x < (WIDTH + self.image_half_width) and self.normalized_distance > 0.5:
            self.calculate_sprite_projection()

    def update(self):
        self.calculate_sprite_parameters()


class AnimatedSprite(Sprite):
    def __init__(self, game_instance, sprite_path='resources/sprites/animated_sprites/green_light/0.png',
                 sprite_position=(11.5, 3.5), scale_factor=0.8, vertical_shift=0.16, animation_duration=120):
        super().__init__(game_instance, sprite_path, sprite_position, scale_factor, vertical_shift)
        self.animation_duration = animation_duration
        self.sprite_folder_path = sprite_path.rsplit('/', 1)[0]
        self.sprite_frames = self.load_images(self.sprite_folder_path)
        self.previous_animation_time = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.update_animation_time()
        self.play_animation(self.sprite_frames)

    def play_animation(self, frames):
        if self.animation_trigger:
            frames.rotate(-1)
            self.sprite_image = frames[0]

    def update_animation_time(self):
        self.animation_trigger = False
        current_time = pg.time.get_ticks()
        if current_time - self.previous_animation_time > self.animation_duration:
            self.previous_animation_time = current_time
            self.animation_trigger = True

    def load_images(self, folder_path):
        sprite_images = deque()
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                image = pg.image.load(folder_path + '/' + file_name).convert_alpha()
                sprite_images.append(image)
        return sprite_images

print(os.getcwd())
import os
print(os.path.isfile('d:/hacktues9/Doom-pygame/resources/sprites/static/candlebra.png'))