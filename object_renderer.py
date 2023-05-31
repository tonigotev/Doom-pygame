import pygame as pg
from settings import *

# watched a video to understand it and implemented it on my own, also I made the most mistakes there xd
class GameRenderingEngine:
    def __init__(self, gameInstance):
        self.gameInstance = gameInstance
        self.screen = gameInstance.display
        self.wallTextures = self.loadWallTextures()
        self.skyTexture = self.loadTexture('resources/textures/sky.png', (SCREEN_WIDTH, HALF_SCREEN_HEIGHT))
        self.skyScrollOffset = 0
        self.bloodOverlay = self.loadTexture('resources/textures/blood_screen.png', RESOLUTION)
        self.digitImageSize = 90
        self.digitImages = [self.loadTexture(f'resources/textures/digits/{i}.png', [self.digitImageSize] * 2)
                             for i in range(11)]
        self.digitDict = dict(zip(map(str, range(11)), self.digitImages))
        self.gameOverImage = self.loadTexture('resources/textures/game_over.png', RESOLUTION)
        self.winImage = self.loadTexture('resources/textures/win.png', RESOLUTION)

    # draw crosshair
    def drawCrosshair(self):
        pg.draw.line(self.screen, "white", (HALF_SCREEN_WIDTH - 10, HALF_SCREEN_HEIGHT),
                     (HALF_SCREEN_WIDTH + 10, HALF_SCREEN_HEIGHT), 2)
        pg.draw.line(self.screen, "white", (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT - 10),
                     (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 10), 2)

    def draw(self):
        self.drawBackground()
        self.renderGameObjects()
        self.drawCrosshair()
        self.drawPlayerHealth()

    def win(self):
        self.screen.blit(self.winImage, (0, 0))

    def gameOver(self):
        self.screen.blit(self.gameOverImage, (0, 0))

    def drawPlayerHealth(self):
        health = str(self.gameInstance.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digitDict[char], (i * self.digitImageSize, 0))
        self.screen.blit(self.digitDict['10'], ((i + 1) * self.digitImageSize, 0))

    def applyPlayerDamageOverlay(self):
        self.screen.blit(self.bloodOverlay, (0, 0))

    def drawBackground(self):
        self.skyScrollOffset = (self.skyScrollOffset + 4.5 * self.gameInstance.player.relativeMouseMovement) % SCREEN_WIDTH
        self.screen.blit(self.skyTexture, (-self.skyScrollOffset, 0))
        self.screen.blit(self.skyTexture, (-self.skyScrollOffset + SCREEN_WIDTH, 0))
        pg.draw.rect(self.screen, "gray", (0, HALF_SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT))

    def renderGameObjects(self):
        listObjectsToRender = sorted(self.gameInstance.ray_casting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, position in listObjectsToRender:
            self.screen.blit(image, position)

    @staticmethod
    def loadTexture(path, resolution=(TEXTURE_RESOLUTION, TEXTURE_RESOLUTION)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, resolution)

    def loadWallTextures(self):
        return {
            1: self.loadTexture('resources/textures/1.png'),
            2: self.loadTexture('resources/textures/2.png'),
            3: self.loadTexture('resources/textures/3.png'),
            4: self.loadTexture('resources/textures/4.png'),
            5: self.loadTexture('resources/textures/5.png'),
        }
