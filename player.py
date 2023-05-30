from settings import *
import pygame as pg
import math

# did it by myself
class PlayerController:
    def __init__(self, gameInstance):
        self.gameInstance = gameInstance
        self.positionX, self.positionY = PLAYER_POSITION
        self.viewingAngle = PLAYER_VIEW_ANGLE
        self.isShooting = False
        self.health = PLAYER_HEALTH_CAP
        self.relativeMouseMovement = 0
        self.healthRecoveryDelayTime = 700
        self.previousTimestamp = pg.time.get_ticks()
        self.diagonalMovementCorrectionFactor = 1 / math.sqrt(2)

    def recoverPlayerHealth(self):
        if self.checkHealthRecoveryDelay() and self.health < PLAYER_HEALTH_CAP:
            self.health += 1

    def checkHealthRecoveryDelay(self):
        currentTimestamp = pg.time.get_ticks()
        if currentTimestamp - self.previousTimestamp > self.healthRecoveryDelayTime:
            self.previousTimestamp = currentTimestamp
            return True

    def checkGameOverCondition(self):
        if self.health < 1:
            self.gameInstance.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.gameInstance.startNewGame()

    def applyDamageToPlayer(self, damageValue):
        self.health -= damageValue
        self.gameInstance.object_renderer.player_damage()
        self.gameInstance.sound.player_pain.play()
        self.checkGameOverCondition()

    def handleSingleFireEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.isShooting and not self.gameInstance.player_weapon.isReloading:
                self.gameInstance.sound.shotgun.play()
                self.isShooting = True
                self.gameInstance.player_weapon.isReloading = True

    def processPlayerMovement(self):
        sinAngle = math.sin(self.viewingAngle)
        cosAngle = math.cos(self.viewingAngle)
        deltaPositionX, deltaPositionY = 0, 0
        movementSpeed = PLAYER_MOVEMENT_SPEED * self.gameInstance.delta_time
        speed_sin = movementSpeed * sinAngle
        speed_cos = movementSpeed * cosAngle

        keyPressedStatus = pg.key.get_pressed()
        numberOfKeysPressed = -1
        if keyPressedStatus[pg.K_w]:
            numberOfKeysPressed += 1
            deltaPositionX += speed_cos
            deltaPositionY += speed_sin
        if keyPressedStatus[pg.K_s]:
            numberOfKeysPressed += 1
            deltaPositionX += -speed_cos
            deltaPositionY += -speed_sin
        if keyPressedStatus[pg.K_a]:
            numberOfKeysPressed += 1
            deltaPositionX += speed_sin
            deltaPositionY += -speed_cos
        if keyPressedStatus[pg.K_d]:
            numberOfKeysPressed += 1
            deltaPositionX += -speed_sin
            deltaPositionY += speed_cos

        if numberOfKeysPressed:
            deltaPositionX *= self.diagonalMovementCorrectionFactor
            deltaPositionY *= self.diagonalMovementCorrectionFactor

        self.checkWallCollision(deltaPositionX, deltaPositionY)
        self.viewingAngle %= math.tau

    def checkForWall(self, x, y):
        return (x, y) not in self.gameInstance.game_map.world_map

    def checkWallCollision(self, deltaPositionX, deltaPositionY):
        scale = PLAYER_MODEL_SCALE / self.gameInstance.delta_time
        if self.checkForWall(int(self.positionX + deltaPositionX * scale), int(self.positionY)):
            self.positionX += deltaPositionX
        if self.checkForWall(int(self.positionX), int(self.positionY + deltaPositionY * scale)):
            self.positionY += deltaPositionY

    def handleMouseControl(self):
        mouseX, mouseY = pg.mouse.get_pos()
        if mouseX < MOUSE_BORDER_START or mouseX > MOUSE_BORDER_END:
            pg.mouse.set_pos([HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT])
        self.relativeMouseMovement = pg.mouse.get_rel()[0]
        self.relativeMouseMovement = max(-MOUSE_MAX_MOVEMENT, min(MOUSE_MAX_MOVEMENT, self.relativeMouseMovement))
        self.viewingAngle += self.relativeMouseMovement * MOUSE_SENSITIVITY_FACTOR * self.gameInstance.delta_time

    def update(self):
        self.processPlayerMovement()
        self.handleMouseControl()
        self.recoverPlayerHealth()

    @property
    def playerPosition(self):
        return self.positionX, self.positionY

    @property
    def mapPosition(self):
        return int(self.positionX), int(self.positionY)
