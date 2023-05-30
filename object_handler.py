from sprite_object import *
from npc import *
from random import choices, randrange

# used GPT to help me implement it on my own
class GameObjectHandler:
    def __init__(self, gameInstance):
        self.gameInstance = gameInstance
        self.spriteObjectsList = []
        self.nonPlayerCharacterList = []
        self.nonPlayerCharacterSpritePath = 'resources/sprites/npc/'
        self.staticSpritePath = 'resources/sprites/static_sprites/'
        self.animatedSpritePath = 'resources/sprites/animated_sprites/'
        addSpriteObject = self.addSpriteObject
        addNonPlayerCharacter = self.addNonPlayerCharacter
        self.nonPlayerCharacterPositions = {}

        # spawn nonPlayerCharacters
        self.totalEnemies = 20 
        self.nonPlayerCharacterTypes = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.spawnProbabilities = [70, 20, 10]
        self.restrictedSpawnArea = {(i, j) for i in range(10) for j in range(10)}
        self.spawnNonPlayerCharacters()

    def spawnNonPlayerCharacters(self):
        for i in range(self.totalEnemies):
                chosenNonPlayerCharacter = choices(self.nonPlayerCharacterTypes, self.spawnProbabilities)[0]
                spawnPosition = x, y = randrange(self.gameInstance.game_map.column_count), randrange(self.gameInstance.game_map.row_count)
                while (spawnPosition in self.gameInstance.game_map.world_map) or (spawnPosition in self.restrictedSpawnArea):
                    spawnPosition = x, y = randrange(self.gameInstance.game_map.column_count), randrange(self.gameInstance.game_map.row_count)
                self.addNonPlayerCharacter(chosenNonPlayerCharacter(self.gameInstance, position=(x + 0.5, y + 0.5)))

    def checkForWinCondition(self):
        if not len(self.nonPlayerCharacterPositions):
            self.gameInstance.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.gameInstance.startNewGame()

    def updateGameState(self):
        self.nonPlayerCharacterPositions = {nonPlayerCharacter.position for nonPlayerCharacter in self.nonPlayerCharacterList if nonPlayerCharacter.alive}
        [spriteObject.update() for spriteObject in self.spriteObjectsList]
        [nonPlayerCharacter.update() for nonPlayerCharacter in self.nonPlayerCharacterList]
        self.checkForWinCondition()

    def addNonPlayerCharacter(self, nonPlayerCharacter):
        self.nonPlayerCharacterList.append(nonPlayerCharacter)

    def addSpriteObject(self, spriteObject):
        self.spriteObjectsList.append(spriteObject)
