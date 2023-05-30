import pygame as pg
import math
from settings import *


class RayCasting:
    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.ray_casting_result = []
        self.objects_to_render = []
        self.wall_textures = self.game_instance.object_renderer.wall_textures

    def calculate_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, projected_height, texture_index, texture_offset = values

            if projected_height < HEIGHT:
                wall_column = self.wall_textures[texture_index].subsurface(
                    texture_offset * (TEXTURE_SIZE - PIXEL_SCALE), 0, PIXEL_SCALE, TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (PIXEL_SCALE, projected_height))
                wall_pos = (ray * PIXEL_SCALE, HALF_HEIGHT - projected_height // 2)
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / projected_height
                wall_column = self.wall_textures[texture_index].subsurface(
                    texture_offset * (TEXTURE_SIZE - PIXEL_SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    PIXEL_SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (PIXEL_SCALE, HEIGHT))
                wall_pos = (ray * PIXEL_SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def cast_ray(self):
        self.ray_casting_result = []
        vertical_texture_index, horizontal_texture_index = 1, 1
        player_x, player_y = self.game_instance.player.pos
        map_x, map_y = self.game_instance.player.map_position

        starting_ray_angle = self.game_instance.player.angle - HALF_FIELD_OF_VIEW + 0.0001
        for ray_index in range(NUMBER_OF_RAYS):
            sin_angle = math.sin(starting_ray_angle)
            cos_angle = math.cos(starting_ray_angle)

            # Horizontal raycast
            y_hor, dy = (map_y + 1, 1) if sin_angle > 0 else (map_y - 1e-6, -1)
            horizontal_depth = (y_hor - player_y) / sin_angle
            x_hor = player_x + horizontal_depth * cos_angle
            depth_delta = dy / sin_angle
            dx = depth_delta * cos_angle

            for i in range(MAXIMUM_RAYCAST_DISTANCE):
                horizontal_tile = int(x_hor), int(y_hor)
                if horizontal_tile in self.game_instance.map.walls:
                    horizontal_texture_index = self.game_instance.map.walls[horizontal_tile]
                    break
                x_hor += dx
                y_hor += dy
                horizontal_depth += depth_delta

            # Vertical raycast
            x_vert, dx = (map_x + 1, 1) if cos_angle > 0 else (map_x - 1e-6, -1)
            vertical_depth = (x_vert - player_x) / cos_angle
            y_vert = player_y + vertical_depth * sin_angle
            depth_delta = dx / cos_angle
            dy = depth_delta * sin_angle

            for i in range(MAXIMUM_RAYCAST_DISTANCE):
                vertical_tile = int(x_vert), int(y_vert)
                if vertical_tile in self.game_instance.map.walls:
                    vertical_texture_index = self.game_instance.map.walls[vertical_tile]
                    break
                x_vert += dx
                y_vert += dy
                vertical_depth += depth_delta

            # Choose depth and texture offset
            if vertical_depth < horizontal_depth:
                chosen_depth, chosen_texture_index = vertical_depth, vertical_texture_index
                y_vert %= 1
                texture_offset = y_vert if cos_angle > 0 else (1 - y_vert)
            else:
                chosen_depth, chosen_texture_index = horizontal_depth, horizontal_texture_index
                x_hor %= 1
                texture_offset = (1 - x_hor) if sin_angle > 0 else x_hor

            # Correct for "fishbowl effect" - https://en.wikipedia.org/wiki/Fisheye_lens#Mapping_function - yea I watched a video to fix it I am not a genius
            chosen_depth *= math.cos(self.game_instance.player.angle - starting_ray_angle)

            # Calculate projection height
            projected_height = SCREEN_DISTANCE / (chosen_depth + 0.0001)

            # Store the result of the raycast
            self.ray_casting_result.append((chosen_depth, projected_height, chosen_texture_index, texture_offset))

            starting_ray_angle += ANGLE_BETWEEN_RAYS

    def update(self):
        self.cast_ray()
        self.calculate_objects_to_render()