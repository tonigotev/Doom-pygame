from collections import deque

# This class is responsible for finding the shortest path between two points on the map.
# It uses a breadth-first search algorithm to find the shortest path between two points.
# GPT gave the idea and helped me implement it
class PathfindingEngine:
    def __init__(self, gameInstance):
        self.gameInstance = gameInstance
        self.mapLayout = gameInstance.game_map.map_layout
        self.directions = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.graphRepresentation = {}
        self.buildGraphRepresentation()

    def findPath(self, startNode, goalNode):
        self.visitedNodes = self.breadthFirstSearch(startNode, goalNode, self.graphRepresentation)
        path = [goalNode]
        step = self.visitedNodes.get(goalNode, startNode)

        while step and step != startNode:
            path.append(step)
            step = self.visitedNodes[step]
        return path[-1]

    def breadthFirstSearch(self, startNode, goalNode, graph):
        nodeQueue = deque([startNode])
        visitedNodes = {startNode: None}

        while nodeQueue:
            currentNode = nodeQueue.popleft()
            if currentNode == goalNode:
                break
            adjacentNodes = graph[currentNode]

            for adjacentNode in adjacentNodes:
                if adjacentNode not in visitedNodes and adjacentNode not in self.gameInstance.handler.nonPlayerCharacterPositions:
                    nodeQueue.append(adjacentNode)
                    visitedNodes[adjacentNode] = currentNode
        return visitedNodes

    def findAdjacentNodes(self, xCoordinate, yCoordinate):
        return [(xCoordinate + dx, yCoordinate + dy) for dx, dy in self.directions if (xCoordinate + dx, yCoordinate + dy) not in self.gameInstance.game_map.world_map]

    def buildGraphRepresentation(self):
        for yIndex, row in enumerate(self.mapLayout):
            for xIndex, cell in enumerate(row):
                if not cell:
                    self.graphRepresentation[(xIndex, yIndex)] = self.graphRepresentation.get((xIndex, yIndex), []) + self.findAdjacentNodes(xIndex, yIndex)