import pygame

# Screen settings
WIDTH, HEIGHT = 1200, 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font for ASCII rendering
pygame.init()
FONT = pygame.font.SysFont("Courier", 20)

# ASCII characters for shading
ASCII_CHARS = ".,-~:;=!*#$@"
MERCURY_CHARS = ".,-~:=!*"

# Sphere parameters (Sun)
RADIUS = 150
SCALE = 200
Z_OFFSET = 300

# Mercury parameters
MERCURY_RADIUS = 20
MERCURY_SCALE = 80
MERCURY_DISTANCE = 500
MERCURY_SPEED = 0.002
