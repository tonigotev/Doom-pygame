import math

# Resolution
RESOLUTION = WIDTH, HEIGHT = 1920, 1080  # or 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# Frame rate
FRAMES_PER_SECOND = 0

# Player settings
PLAYER_POSITION = 1.5, 5  # Position in the mini map
PLAYER_VIEW_ANGLE = 0
PLAYER_MOVE_SPEED = 0.006
PLAYER_ROTATION_SPEED = 0.005
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100

# Mouse settings
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_MOVEMENT = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

# Color settings
FLOOR_COLOR = (30, 30, 30)

# Field of view
FIELD_OF_VIEW = math.pi / 3
HALF_FIELD_OF_VIEW = FIELD_OF_VIEW / 2

# Raycasting settings
NUMBER_OF_RAYS = WIDTH // 2
HALF_NUMBER_OF_RAYS = NUMBER_OF_RAYS // 2
ANGLE_BETWEEN_RAYS = FIELD_OF_VIEW / NUMBER_OF_RAYS
MAXIMUM_RAYCAST_DISTANCE = 20

# Projection settings
SCREEN_DISTANCE = HALF_WIDTH / math.tan(HALF_FIELD_OF_VIEW)
PIXEL_SCALE = WIDTH // NUMBER_OF_RAYS

# Texture settings
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2