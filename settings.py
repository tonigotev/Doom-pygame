import math

# Game settings
RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 960 #1920, 1080
HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
FRAMES_PER_SECOND = 0
PLAYER_POSITION = 1.5, 5
PLAYER_VIEW_ANGLE = 0
PLAYER_MOVEMENT_SPEED = 0.010
PLAYER_ROTATION_SPEED = 0.002
PLAYER_MODEL_SCALE = 60
PLAYER_HEALTH_CAP = 100
MOUSE_SENSITIVITY_FACTOR = 0.0010
MOUSE_MAX_MOVEMENT = 40
MOUSE_BORDER_START = 100
MOUSE_BORDER_END = SCREEN_WIDTH - MOUSE_BORDER_START
GROUND_COLOR = (30, 30, 30)
RAYCAST_COUNT = SCREEN_WIDTH // 2
HALF_RAYCAST_COUNT = RAYCAST_COUNT // 2
FIELD_OF_VIEW = math.pi / 3
HALF_FIELD_OF_VIEW = FIELD_OF_VIEW / 2
RAY_ANGLE_INCREMENT = FIELD_OF_VIEW / RAYCAST_COUNT
RENDER_DISTANCE = 20
RENDER_SCALE = SCREEN_WIDTH // RAYCAST_COUNT
SCREEN_DISTANCE = HALF_SCREEN_WIDTH / math.tan(HALF_FIELD_OF_VIEW)
PROJECTION_COEFFICIENT = SCREEN_DISTANCE * RENDER_SCALE
TEXTURE_RESOLUTION = 256
HALF_TEXTURE_RESOLUTION = TEXTURE_RESOLUTION // 2